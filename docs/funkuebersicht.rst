.. meta::
   :theme-color: #3eaf7c

.. _cha_funkuebersicht:

Funktionsübersicht
*******************

Das in den Bildern gezeigte Setup setzt eine vollständige Installation aller 
Programme und Programmkomponenten, sowie ein geladenes und aktives QGIS-ALKIS-Projekt 
voraus. Siehe hierzu die Anleitungen :ref:`cha_installation`, :ref:`cha_dbbereitstellung`,
:ref:`cha_dimport`, und :ref:`cha_projekterstellung`.

Übersicht erweiterte Programmoberfläche
=========================================

.. _img_fueb1:

.. container:: fleft mw500

   .. image:: _static/png/fueb1.png

Verwaltung von **norGIS ALKIS-Einbindung** unter dem ``Datenbank``-Reiter. 

.. raw:: html
   
   <p class="clear"><p>


.. _img_fueb2:

.. container:: fleft mw500

   .. image:: _static/png/fueb2.png

Plugin-Funktionen in der Werkzeugleiste.

.. raw:: html
   
   <p class="clear"><p>


.. _img_fueb3:

.. container:: fleft mw500

   .. image:: _static/png/fueb3.png

Markierungslayer des geöffneten ALKIS-Datensatzes.

``Jagd-Flächenmarkierung`` beinhaltet die selektierten Flurstücke des **JagdKataster**-Plugins. 
Diese Flurstücke werden blau dargestellt.

Markierte Flurstücke der **norGIS ALKIS-Einbindung** werden in Layer 
``Flächenmarkierung`` gelb dargestellt. 

.. raw:: html
   
   <p class="clear"><p>


Erläuterung der Plugin-Funktionen
===================================

+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| |fico1| Layer einbinden  | ALKIS-Datensatz von konfigurierter Serverdatenbank beziehen und in Projekt einfügen.                                                      |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| |fico1| Konfiguration... | Konfiguration der Bezugsquelle (Server, Zugangsdaten, Zieldatenbank) für Bezug der ALKIS-Daten. Auswahl der zu beziehenden ALKIS-Modelle. |
+--------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+

|

+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Symbol   | Funktionsbeschreibung                                                                                                                                                                                                            |
+==========+==================================================================================================================================================================================================================================+
| |fico2|  | Flurstücksuche nach Beschriftungen, Flurstückskennzeichen, Straße/Hausnummer und Eigentümer. [Gelbe Anzeige in ``Flächenmarkierung``]                                                                                            |
+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          | Auswahlwerkzeug Flurstücksnachweis: Anzeige des Flurstücksnachweis, wenn ein Flurstück mit einer :kbd:`Maustaste` angeklickt wird. [Gelbe Anzeige in ``Flächenmarkierung``]                                                      |
| |fico3|  |                                                                                                                                                                                                                                  |
|          | Der Nachweis kann über das Kontextmenü (:kbd:`Rechtsklick` auf Flurstücksnachweis) gedruckt werden.                                                                                                                              |
+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |fico4|  | Deselektierung aller Flurstücke in ``Flächenmarkierung``. [Gelbe Anzeige in ``Flächenmarkierung``]                                                                                                                               |
+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |fico5|  | Selektierte Flurstücke in ``Flächenmarkierung`` [Gelbe Anzeige] den Flurstücken in ``Jagd-Flächenmarkierung`` [Blaue Anzeige] hinzufügen.                                                                                        |
+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |fico6|  | Auswahlwerkzeug An/Abwählen: Ein mit einer der Maustasten angeklicktes Flurstück wird in ``Jagd-Flächenmarkierung`` selektiert, oder deselektiert falls vorher bereits selektiert. [Blaue Anzeige in ``Jagd-Flächenmarkierung``] |
+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|          | Ergänzende Selektierung der Flurstücke in ``Jagd-Flächenmarkierung`` anhand von Flurstücksnutzungen und Gemarkungsnummern. [Blaue Anzeige in ``Jagd-Flächenmarkierung``]                                                         |
| |fico7|  |                                                                                                                                                                                                                                  |
|          | Bei angewählter Formular-Liste kann die Tastenkombination :kbd:`Strg + a` und die Formulartaste ``Anwählen`` genutzt werden um alle Listenelemente anzuwählen.                                                                   |
+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |fico8|  | Deselektierung aller Flurstücke in ``Jagd-Flächenmarkierung``. [Blaue Anzeige in ``Jagd-Flächenmarkierung``]                                                                                                                     |
+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |fico9|  | Listet Flurstücksnachweise für alle in ``Jagd-Flächenmarkierung`` selektierten Flurstücke. [Blaue Anzeige in ``Jagd-Flächenmarkierung``]                                                                                         |
+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |fico10| | Erstellung eines Jagdkatasters für alle in ``Jagd-Flächenmarkierung`` selektierten Flurstücke. [Blaue Anzeige in ``Jagd-Flächenmarkierung``]                                                                                     |
+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |fico11| | Zeigt Flurstückszusammenfassung für alle in   ``Jagd-Flächenmarkierung`` selektierten Flurstücke. [Blaue Anzeige in ``Jagd-Flächenmarkierung``]                                                                                  |
+----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. container:: minisource

   „QGIS Logo“ qgis.org/en/site/getinvolved/styleguide is licensed under Creative Commons Attribution-ShareAlike 3.0 licence (CC BY-SA)

   “norBIT Logo” norbit.de/68

.. |fico1| image:: _static/png/fico1.png
.. |fico2| image:: _static/png/fico2.png
.. |fico3| image:: _static/png/fico3.png
.. |fico4| image:: _static/png/fico4.png
.. |fico5| image:: _static/png/fico5.png
.. |fico6| image:: _static/png/fico6.png
.. |fico7| image:: _static/png/fico7.png
.. |fico8| image:: _static/png/fico8.png
.. |fico9| image:: _static/png/fico9.png
.. |fico10| image:: _static/png/fico10.png
.. |fico11| image:: _static/png/fico11.png





