.. meta::
   :theme-color: #3eaf7c

.. _cha_installation:

Installation
************
Diese Schritt für Schritt Anleitung ist für Computer mit Microsoft 
Windows-Betriebssystem.
Neben Windows wird prinzipiell auch Linux unterstützt. 
Siehe `<https://www.norbit.de/68/>`_ für die Linux-Installation.

Für die Erstellung eines Jagdkatasters mit QGIS werden einige 
Programme und Programmerweiterungen (Plugins) benötigt. 
Die vollständige Programmstruktur ist in der untenstehenden Grafik abgebildet.

Alle benötigten Programme und Programmkomponenten sind aktuell als Freie-Software 
(oder vergleichbar) lizenziert und können somit kosten- und werbefrei verwendet werden. Genauere Informationen finden Sie in den jeweiligen Lizenzbedingungen.

.. _img_inst1:

.. image:: _static/png/inst1.png

.. _sec_qgis:

QGIS & norGIS ALKIS Import
==========================

QGIS kann von `<https://qgis.org/de/site/forusers/download.html>`_ heruntergeladen 
werden. Es wird die Netzwerkinstallation benötigt um eine erweiterte 
Installation mit zusätzlichen Komponenten durchzuführen.

.. _img_inst2:

.. image:: _static/png/inst2.png


Starten Sie die Installation nachdem der Download abgeschlossen ist.

|

.. _img_inst3:

.. container:: fleft mw700

   .. image:: _static/png/inst3.png

``Fortgeschrittene Installation`` auswählen und mit Formulartaste 
``Weiter >`` bestätigen.


.. raw:: html
   
   <p class="clear"><p>

.. _img_inst4:

.. container:: fleft mw700

   .. image:: _static/png/inst4.png

Dateien ``Aus dem Internet installieren...`` auswählen und mit 
Formulartaste ``Weiter >`` bestätigen.


.. raw:: html
   
   <p class="clear"><p>

.. _img_inst5:

.. container:: fleft mw700

   .. image:: _static/png/inst5.png

Installationsverzeichnis und weitere Präferenzen auswählen 
und mit Formulartaste ``Weiter >`` bestätigen.

.. raw:: html
   
   <p class="clear"><p>

.. _img_inst6:

.. container:: fleft mw700

   .. image:: _static/png/inst6.png

Speicherort für Installationspakete wählen oder Standard 
beibehalten und mit  Formulartaste ``Weiter >`` bestätigen.


.. raw:: html
   
   <p class="clear"><p>

.. _img_inst7:

.. container:: fleft mw700

   .. image:: _static/png/inst7.png

``Direkte Verbindung`` auswählen und mit Formulartaste 
``Weiter >`` bestätigen.


.. raw:: html
   
   <p class="clear"><p>

.. _img_inst8:

.. container:: fleft mw700

   .. image:: _static/png/inst8.png

Eine der verfügbaren Downloadseiten wählen und mit Formulartaste 
``Weiter >`` bestätigen.


.. raw:: html
   
   <p class="clear"><p>

.. _img_inst9:

.. container:: fleft mw700

   .. image:: _static/png/inst9.png

Standard ``Default`` bei allen Gruppen beibehalten 
und die ``Desktop`` Gruppe aufklappen.


.. raw:: html
   
   <p class="clear"><p>

.. _img_inst10:

.. container:: fleft mw700

   .. image:: _static/png/inst10.png

``Skip`` für ``alkis-import: norGIS ALKIS Import`` einmal anklicken 
um die aktuellste Version für die Installation auszuwählen.  

Das Gleiche für ``qgis-ltr: QGIS Desktop (long term release)`` durchführen.


.. raw:: html
   
   <p class="clear"><p>

.. _img_inst11:

.. container:: fleft mw1000

   .. image:: _static/png/inst11.png

Installation von ``alkis-import: norGIS ALKIS Import`` und
``qgis-ltr: QGIS Desktop (long term release)`` mit Formulartaste ``Weiter >`` 
bestätigen.


.. raw:: html
   
   <p class="clear"><p>

.. _img_inst12:

.. container:: fleft mw700

   .. image:: _static/png/inst12.png

Akzeptieren Sie die Installation aller Notwendigen Abhängigkeiten 
und bestätigen Sie die Installation mit Formulartaste ``Weiter >``.

Bestätigen Sie anschließend alle zusätzlichen Lizenzbedingungen um 
die Installation zu starten.


.. raw:: html
   
   <p class="clear"><p>

.. _img_inst13:

.. container:: fleft mw1000

   .. image:: _static/png/inst13.png

Nach abgeschlossener Installation sind **norGIS ALKIS Import** 
und **QGIS Desktop** über das Startmenü oder die Windows-Suchleiste aufrufbar.

.. raw:: html
   
   <p class="clear"><p>

.. _sec_qgisext:

QGIS Erweiterungen (Plugins)
============================

QGIS Erweiterungen werden direkt aus **QGIS Desktop** installiert. 
Es soll die **norGIS ALKIS Einbindung** und **JagdKataster** installiert 
und aktiviert werden. Installieren Sie die **norGIS ALKIS Einbindung** 
am besten zuerst, denn diese muss zuerst aktiviert werden.


.. _img_inst14:

.. container:: fleft mw500

   .. image:: _static/png/inst14.png


Über den Reiter ``Erweiterungen`` ``Erweiterungen verwalten und installieren...`` 
auswählen.

.. raw:: html
   
   <p class="clear"><p>

Finden Sie die Erweiterungen mittels der Suchleiste und starten Sie die 
Installation mit Formulartaste ``Erweiterung installieren``.

.. _img_inst15:

.. image:: _static/png/inst15.png

.. _img_inst16:

.. image:: _static/png/inst16.png

|

Unter ``Installiert`` sind die aktivierten Erweiterungen mit einem Haken 
markiert. Achten Sie darauf, dass **norGIS ALKIS Einbindung** und 
**JagdKataster** aktiv sind.

.. _img_inst17:

.. image:: _static/png/inst17.png

|

.. _sec_postgresql:

PostgreSQL, pgAdmin und PostGIS
===============================

Die PostgreSQL und PostGIS Versionen müssen vollständig kompatibel sein. 
Eine Kompatibilitätsmatrix ist unter 
`<https://trac.osgeo.org/postgis/wiki/UsersWikiPostgreSQLPostGIS>`_ zu finden. 
In dieser Anleitung installieren wir **PostgreSQL** in der Version 12 
und **PostGIS** 3.0.

Der Downloadlink ist `<https://www.postgresql.org/download/windows/>`_.


.. _img_inst18:

.. container:: fleft mw500

   .. image:: _static/png/inst18.png

Wählen Sie den Link ``Dowwnload the installer`` um zur Downloadseite zu 
gelangen.

.. raw:: html
   
   <p class="clear"><p>

|

Laden Sie **PostgreSQL** Version12.X herunter und starten die Installation.

.. _img_inst19:

.. image:: _static/png/inst19.png

|
|

.. _img_inst20:

.. container:: fleft mw700

   .. image:: _static/png/inst20.png

Installationsverzeichnis wählen oder Standard beibehalten und mit 
Formulartaste ``Next >`` bestätigen.

.. raw:: html
   
   <p class="clear"><p>


.. _img_inst21:

.. container:: fleft mw700

   .. image:: _static/png/inst21.png

Es werden alle Komponenten benötig. Alle Komponenten auswählen 
und mit Formulartaste ``Next >`` bestätigen.

.. raw:: html
   
   <p class="clear"><p>


.. _img_inst22:

.. container:: fleft mw700

   .. image:: _static/png/inst22.png

Datenverzeichnis wählen oder Standard beibehalten und 
mit Formulartaste ``Next >`` bestätigen.

.. raw:: html
   
   <p class="clear"><p>


.. _img_inst23:

.. container:: fleft mw700

   .. image:: _static/png/inst23.png

Passwort für das Benutzerprofil des Datenbankadministrators 
festlegen und notieren!

Eingaben mit Formulartaste ``Next >`` bestätigen.

.. raw:: html
   
   <p class="clear"><p>

.. warning:: Passwort notieren!
   
   Das Passwort des Datenbankadministrators wird später häufig benötig.


.. _img_inst24:

.. container:: fleft mw700

   .. image:: _static/png/inst24.png

Zugangsport wählen oder Standard beibehalten und mit Formulartaste ``Next >`` bestätigen.

.. raw:: html
   
   <p class="clear"><p>


.. _img_inst25:

.. container:: fleft mw700

   .. image:: _static/png/inst25.png

Standard beibehalten und mit Formulartaste ``Next >`` bestätigen.

Nachfolgende Schritte bestätigen und installieren.

.. raw:: html
   
   <p class="clear"><p>


.. _img_inst26:

.. container:: fleft mw700

   .. image:: _static/png/inst26.png

Durch setzen des Hakens wird das Programm **Application Stack Builder** 
automatisch gestartet. Dieses Programm wird in den folgenden Schritten benötigt.

**PostgreSQL** Installation mit Formulartaste ``Finish`` abschließen.

.. raw:: html
   
   <p class="clear"><p>


.. _img_inst27:

.. container:: fleft mw700

   .. image:: _static/png/inst27.png

Das Programm **Application Stack Builder** sollte am Ende der **PostgreSQL**
Installation automatisch gestartet werden. Ansonsten ist das Programm zusammen 
mit **pgAdmin** über den nebenstehenden Startmenüeintrag aufrufbar.

.. raw:: html
   
   <p class="clear"><p>

Mit dem **Application Stack Builder** wird **PostGIS** für **PostgreSQL** installiert.

|

.. _img_inst28:

.. container:: fleft mw700

   .. image:: _static/png/inst28.png

Die installierte **PostgreSQL**-Version auswählen und mit Formulartaste ``Weiter >`` bestätigen.

.. raw:: html
   
   <p class="clear"><p>


.. _img_inst29:

.. container:: fleft mw700

   .. image:: _static/png/inst29.png

Menübaum bei ``Spatial Extensions`` öffnen und Haken bei ``PostGIS`` setzen. 
Eingabe mit Formulartaste ``Weiter >`` bestätigen.

.. raw:: html
   
   <p class="clear"><p>


.. _img_inst30:

.. container:: fleft mw700

   .. image:: _static/png/inst30.png

Speicherort für Installationspakete wählen oder Standard beibehalten und
mit Formulartaste ``Weiter >`` bestätigen.

.. raw:: html
   
   <p class="clear"><p>


.. _img_inst31:

.. container:: fleft mw700

   .. image:: _static/png/inst31.png

Hinweis beachten und Formular mit Formulartaste ``Weiter >`` bestätigen.

Lizenzbedingungen annehmen und **PostGIS**-Installation starten.

.. raw:: html
   
   <p class="clear"><p>


.. _img_inst32:

.. container:: fleft mw700

   .. image:: _static/png/inst32.png

Beide Komponenten anwählen. ``Create spatial database`` richtet uns eine Vorlage 
ein die wir benötigen.

Eingabe mit Formulartaste ``Next >`` bestätigen.

.. raw:: html
   
   <p class="clear"><p>


.. _img_inst33:

.. container:: fleft mw700

   .. image:: _static/png/inst33.png

Installationsverzeichnis wählen oder Standard beibehalten und mit Formulartaste ``Next >`` bestätigen.

Das Standardverzeichnis ist das Installationsverzeichnis von **PostgreSQL**.

.. raw:: html
   
   <p class="clear"><p>


.. _img_inst34:

.. container:: fleft mw700

   .. image:: _static/png/inst34.png

Geben Sie die **PostgreSQL**-Verbindungsdaten ein die Sie bei der **PostgreSQL**-Installation für das 
Benutzerprofil des Serveradministrators vergeben haben. (Siehe `Abbildung_23 <img_inst23_>`_)

Eingabe mit Formulartaste ``Next >`` bestätigen.

.. raw:: html
   
   <p class="clear"><p>


.. _img_inst35:

.. container:: fleft mw700

   .. image:: _static/png/inst35.png

Name für die Datenbankvorlage vergeben oder Standard beibehalten und mit Formulartaste ``Install``
die **PostGIS**-Installation starten.

.. raw:: html
   
   <p class="clear"><p>


.. _img_inst36:

.. container:: fleft mw500

   .. image:: _static/png/inst36.png

Die drei nachfolgenden Dialoge mit Formulartaste ``Ja`` bestätigen.

.. _img_inst37:

.. container:: fleft mw500

   .. image:: _static/png/inst37.png

.. _img_inst38:

.. container:: fleft mw500

   .. image:: _static/png/inst38.png

.. raw:: html
   
   <p class="clear"><p>


.. _img_inst39:

.. container:: fleft mw700

   .. image:: _static/png/inst39.png

Warten bis die Installation vollständig abgeschlossen ist. Formular mit Formulartaste ``Close`` schließen.

.. raw:: html
   
   <p class="clear"><p>


.. _img_inst40:

.. container:: fleft mw700

   .. image:: _static/png/inst40.png

Das Fenster von **Application Stack Builder** mit Formulartaste ``Fertigstellen`` schließen.

.. raw:: html
   
   <p class="clear"><p>

Glückwunsch, die Installation aller Programme und Programmkomponenten wurden erfolgreich abgeschlossen! 

|

.. container:: minisource

   „QGIS Logo“ qgis.org/en/site/getinvolved/styleguide is licensed under Creative Commons Attribution-ShareAlike 3.0 licence (CC BY-SA)

   „PostgreSQL Logo” wiki.postgresql.org/wiki/Logo „PostGIS Logo“ osgeo.org/projects/postgis

   “norBIT Logo” norbit.de/68