# -*- coding: utf-8 -*-
"""
/***************************************************************************
 huntregister.py
                                 Ein QGIS plugin
 Dieses Plugin kann in Kombination mit dem alkisplugin zur Erstellung eines
 Jagdkatasters verwendet werden. Die Datengrundlage sind die in Deutschland
 üblichen ALKIS-Daten (NAS-Format)

 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2020-03-26
        git sha              : $Format:%H$
        copyright            : (C) 2020 by Simon Hodrus
        email                : s.hodrus@gmx.de
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os.path

from typing import List, Sequence

from qgis.PyQt.QtCore import QSettings, QDir, Qt, QTranslator, QCoreApplication, QTimer
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QToolBar, QMessageBox

qgisAvailable = False
alkisAvailable = False

try:
    import qgis.core
    qgisAvailable = True
except ImportError:
    qgisAvailable = False

try:
    import alkisplugin
    alkisAvailable = True
except ImportError:
    alkisAvailable = False

if qgisAvailable:
    from qgis.core import (
        QgsApplication,
        QgsProject,
        Qgis,
        QgsVectorLayer,
        QgsSingleSymbolRenderer,
        QgsWkbTypes,
        QgsSymbol,
    )

if alkisAvailable:
    import alkisplugin as Alkis

thdir = os.path.dirname(__file__)
# used to get a short link representation for resourcces with the same culture
# otherwise a qrc-File and compilation is needed
QDir.addSearchPath("hunt", os.path.join(thdir, "svg"))


from .huntcore import HuntCore
from .huntuiclasses import HAdd


class HuntRegister:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)

        # Check if plugin was started the first time in current QGIS session
        # Must be set in initGui() to survive plugin reloads
        self.first_start = None

        # This plugin depends on alkisplugin
        self.alkisplugin = None

        # Members
        self.alkisToolBar = None                                                                # the toolbar instance where the alkisplugin and huntplugin QAction symbols are placed

        self.alkisSelectAreaLayer = None                                                        # QgsVectorLayer selected parcels of alkisplugin
        self.huntSelectAreaLayer = None                                                         # QgsVectorLayer selected parcels of huntplugin

        # All actions are assigned to alter self.huntSelectAreaLayer
        self.hswapAction = None                                                                 # single QAction copy selected parcels from alkisplugin to huntplugin
        self.hAddMarkAction = None                                                              # checkable QAction select and unselect parcels
        self.hlistAction = None                                                                 # single QAction select parcels by parcel attributes
        self.hclearAction = None                                                                # single QAction unselect all selected parcels
        self.hownerAction = None                                                                # single QAction get parcel certificates for all selected parcels
        self.hhuntAction = None                                                                 # single QAction create a hunt register
        self.hinfoAction = None                                                                 # single QAction get a basic summary of all selected parcels
        # self.testAction = None                                                                # single QAction used for testing program fragments

        self.hAddMarkTool = None                                                                # click recognizing map tool for self.hAddMarkAction
        self.core = None                                                                        # function core for this plugin
        self.initTimer = QTimer(self.iface)                                                     # timer used to init self.huntSelectAreaLayer dynamically when alkis layers are added
        self.initTimer.setInterval(1000)                                                        # 1 sec interval
        self.initTimer.timeout.connect(self.initLayers)
        self.init()                                                                             # init main instances

    def init(self):
        """init main instances"""

        if(alkisAvailable):
            try:
                self.alkisplugin = Alkis.alkisplugin.alkisplugin(self.iface)                    # create alkisplugin object
                self.alkisplugin.queryOwnerAction = QAction(None)                               # this is used in akisplugin "opendb" and must therefore be set to prevent runtime errors
            except AttributeError:
                QMessageBox.critical(None, "Fehler", "norGIS ALKIS-Einbindung zuerst aktivieren und \"JagdKataster\" erneut aktivieren")
                raise AttributeError("alkisplugin not active")
        else:
            QMessageBox.critical(None, "Fehler", "norGIS ALKIS-Einbindung installieren und zuerst aktivieren. Dann \"JagdKataster\" erneut aktivieren")
            raise AttributeError("alkisplugin not installed")

        self.core = HuntCore(self)                                                              # function core for this plugin

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        # will be set False in run()
        self.first_start = True

        # the toolbar entries of this plugin should be placed alongside the alkisplugin entries
        # therefore the alkisplugin toolbar is derived
        tBars = self.iface.mainWindow().findChildren(QToolBar)                                                                  # get all toolbars from main window
        self.alkisToolBar = next((n for n in tBars if n.objectName() == "norGIS_ALKIS_Toolbar"), None)                          # find the instance of alkisplugin toolbar by its static name

        if self.alkisToolBar is None:                                                                                           # in case the toolbar is not yet loaded create the instance with its static name
            # create alkis toolbar in case it is not yet loaded
            self.alkisToolBar = self.iface.addToolBar(u"norGIS: ALKIS")
            self.alkisToolBar.setObjectName("norGIS_ALKIS_Toolbar")

        #create toolbar items
        self.hswapAction = QAction(QIcon("hunt:mark_transfer.svg"), "Flächenmarkierung übertragen", self.iface.mainWindow())
        self.hswapAction.setWhatsThis("Flächenmarkierung (gelb) nach Jagd-Flächenmarkierung (blau) übertragen")
        self.hswapAction.setStatusTip("Flächenmarkierung (gelb) nach Jagd-Flächenmarkierung (blau) übertragen")
        self.hswapAction.triggered.connect(lambda: self.core.swapAlkisToHunt())
        self.alkisToolBar.addAction(self.hswapAction)

        self.hAddMarkAction = QAction(QIcon("hunt:mark_add.svg"), u"Flurstück (de)selektieren", self.iface.mainWindow())
        self.hAddMarkAction.setWhatsThis("Flurstück in Jagd-Flächenmarkierung selektieren oder deselektieren")
        self.hAddMarkAction.setStatusTip("Flurstück in Jagd-Flächenmarkierung selektieren oder deselektieren")
        self.hAddMarkAction.setCheckable(True)
        self.hAddMarkAction.triggered.connect(lambda: self.iface.mapCanvas().setMapTool(self.hAddMarkTool))
        self.alkisToolBar.addAction(self.hAddMarkAction)
        self.hAddMarkTool = HAdd(self)
        self.hAddMarkTool.setAction(self.hAddMarkAction)

        self.hlistAction = QAction(QIcon("hunt:mark_list.svg"), "Selektieren nach Flurstückseigenschaft", self.iface.mainWindow())
        self.hlistAction.setWhatsThis("Selektierung der Flurstücke in Jagd-Flächenmarkierung anhand Flurstückseigenschaften")
        self.hlistAction.setStatusTip("Selektierung der Flurstücke in Jagd-Flächenmarkierung anhand Flurstückseigenschaften")
        self.hlistAction.triggered.connect(lambda: self.core.showListSelection())
        self.alkisToolBar.addAction(self.hlistAction)

        self.hclearAction = QAction(QIcon("hunt:mark_clear.svg"), "Alle deselektieren", self.iface.mainWindow())
        self.hclearAction.setWhatsThis("Alle Flurstücke in Jagd-Flächenmarkierung deselektieren")
        self.hclearAction.setStatusTip("Alle Flurstücke in Jagd-Flächenmarkierung deselektieren")
        self.hclearAction.triggered.connect(lambda: self.core.clearHighlight())
        self.alkisToolBar.addAction(self.hclearAction)

        self.hownerAction = QAction(QIcon("hunt:mark_own.svg"), "Flurstücksnachweise anzeigen", self.iface.mainWindow())
        self.hownerAction.setWhatsThis("Flurstücksnachweise für selektierte Flurstücke in Jagd-Flächenmarkierung anzeigen")
        self.hownerAction.setStatusTip("Flurstücksnachweise für selektierte Flurstücke in Jagd-Flächenmarkierung anzeigen")
        self.hownerAction.triggered.connect(lambda: self.core.showParcelCerts())
        self.alkisToolBar.addAction(self.hownerAction)

        self.hhuntAction = QAction(QIcon("hunt:mark_hunt.svg"), "Jagdkataster erstellen", self.iface.mainWindow())
        self.hhuntAction.setWhatsThis("Jagdkataster für selektierte Flurstücke in Jagd-Flächenmarkierung erstellen")
        self.hhuntAction.setStatusTip("Jagdkataster für selektierte Flurstücke in Jagd-Flächenmarkierung erstellen")
        self.hhuntAction.triggered.connect(lambda: self.core.showHuntReg())
        self.alkisToolBar.addAction(self.hhuntAction)

        self.hinfoAction = QAction(QIcon("hunt:mark_info.svg"), "Flurstückszusammenfassung anzeigen", self.iface.mainWindow())
        self.hinfoAction.setWhatsThis("Flurstückszusammenfassung für selektierte Flurstücke in Jagd-Flächenmarkierung anzeigen")
        self.hinfoAction.setStatusTip("Flurstückszusammenfassung für selektierte Flurstücke in Jagd-Flächenmarkierung anzeigen")
        self.hinfoAction.triggered.connect(lambda: self.core.showSummaryDialog())
        self.alkisToolBar.addAction(self.hinfoAction)

        # self.testAction = QAction(QIcon("hunt:test.svg"), "Test", self.iface.mainWindow())
        # self.testAction.setWhatsThis("Test action")
        # self.testAction.setStatusTip("Test action")
        # self.testAction.triggered.connect(lambda: self.core.test(self.huntSelectAreaLayer))
        # self.alkisToolBar.addAction(self.testAction)

        QgsProject.instance().layersAdded.connect(self.initTimer.start)                                                         # react to changes in the layer tree. Maybe the alkis layers were added
        QgsProject.instance().layersWillBeRemoved.connect(self.layersRemoved)                                                   # remove entries in case this plugin layers are to be removed

    def initLayers(self):
        """init self.huntSelectAreaLayer in case the alkis layers from alkisplugin are loaded"""
        self.initTimer.stop()                                                                                                   # this methode may be called by a timer started when layers are added => stop the timer after first timeout event
        if self.alkisSelectAreaLayer is None:                                                                                   # are alkisplugin layers loaded ad readable from entry?
            (layerId, res) = QgsProject.instance().readEntry("alkis", "/areaMarkerLayer")
            if res and layerId:
                self.alkisSelectAreaLayer = QgsProject.instance().mapLayer(layerId)
        if self.huntSelectAreaLayer is None:                                                                                    # is the huntplugin layer already loaded?
            (layerId, res) = QgsProject.instance().readEntry("hunt", "/areaMarkerLayer")
            if res and layerId:
                self.huntSelectAreaLayer = QgsProject.instance().mapLayer(layerId)
        if self.huntSelectAreaLayer is None and self.alkisSelectAreaLayer is not None:                                          # alkisplugin layers are loaded but huntplugin layer is not
            self.createLayer()                                                                                                  # create huntplugin layer

    def layersRemoved(self, layersIds):
        """remove entries and references in case this plugin layers are to be removed"""
        if self.alkisSelectAreaLayer is not None and self.alkisSelectAreaLayer.id() in layersIds:
            self.alkisSelectAreaLayer = None
        if self.huntSelectAreaLayer is not None and self.huntSelectAreaLayer.id() in layersIds:
            QgsProject.instance().removeEntry("hunt", "/areaMarkerLayer")
            self.core.hlayer = None
            self.huntSelectAreaLayer = None

    def createLayer(self):
        """create and add huntplugin layer to the layer tree"""
        if(self.alkisSelectAreaLayer is not None):
            parent = QgsProject.instance().layerTreeRoot().findLayer(self.alkisSelectAreaLayer).parent()
            layeropts = QgsVectorLayer.LayerOptions(False, False)

            self.init()                                                                                                         # reinit main instances because alkis instance conninfo might have changed
            (db, conninfo) = self.core.openDB()
            if db is None:
                return

            self.huntSelectAreaLayer = QgsVectorLayer(
                u"%s estimatedmetadata=true checkPrimaryKeyUnicity=0 key='ogc_fid' type=MULTIPOLYGON srid=%d table=%s.po_polygons (polygon) sql=false" % (conninfo, self.alkisplugin.epsg, self.alkisplugin.quotedschema()),
                u"Jagd-Flächenmarkierung",
                "postgres", layeropts
            )

            sym = QgsSymbol.defaultSymbol(QgsWkbTypes.PolygonGeometry)
            sym.setColor(Qt.blue)
            sym.setOpacity(0.3)

            self.huntSelectAreaLayer.setRenderer(QgsSingleSymbolRenderer(sym))
            QgsProject.instance().addMapLayer(self.huntSelectAreaLayer, False)
            parent.insertLayer(0, self.huntSelectAreaLayer)

            self.core.hlayer = None
            QgsProject.instance().writeEntry("hunt", "/areaMarkerLayer", self.huntSelectAreaLayer.id())

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        if self.hswapAction:
            self.hswapAction.deleteLater()
            self.hswapAction = None
        if self.hAddMarkAction:
            self.hAddMarkAction.deleteLater()
            self.hAddMarkAction = None
        if self.hlistAction:
            self.hlistAction.deleteLater()
            self.hlistAction = None
        if self.hclearAction:
            self.hclearAction.deleteLater()
            self.hclearAction = None
        if self.hownerAction:
            self.hownerAction.deleteLater()
            self.hownerAction = None
        if self.hhuntAction:
            self.hhuntAction.deleteLater()
            self.hhuntAction = None
        if self.hinfoAction:
            self.hinfoAction.deleteLater()
            self.hinfoAction = None
        # if self.testAction:
        #     self.testAction.deleteLater()
        #     self.testAction = None

        QgsProject.instance().layersAdded.disconnect(self.initTimer.start)
        QgsProject.instance().layersWillBeRemoved.disconnect(self.layersRemoved)

    def run(self):
        """Run method"""
        if self.first_start:
            self.first_start = False
