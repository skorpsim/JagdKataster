.. meta::
   :theme-color: #3eaf7c

.. _cha_dimport:

Datenimport
***********

Diese Anleitung setzt eine vollständige Installation aller Programme und 
Programmkomponenten, sowie eine vorhandene **PostGIS**-Datenbank voraus. 
Siehe hierzu die Anleitungen :ref:`cha_installation` und :ref:`cha_dbbereitstellung`.

|

.. _sec_beispieldaten:

Beispieldaten
=============

Fall Sie noch keinen ALKIS-Datensatz (NAS-Daten) besitzen, 
können Sie zum Testen einen Test-Datensatz verwenden. LGL-BW stellt unter 
`<https://www.lgl-bw.de/unsere-themen/Geoinformation/AFIS-ALKIS-ATKIS/ALKIS/Testdaten/#alkis_06>`_ 
Testdaten bereit.

.. _img_dimp1:

.. container:: fleft mw500

   .. image:: _static/png/dimp1.png


Testdaten herunterladen und zip-komprimierter Ordner entpacken oder 
eigene ALKIS-Daten verwenden. 

.. raw:: html
   
   <p class="clear"><p>


.. _sec_norgisimport:

Datensatz einlesen
==================

Starten Sie das Programm **norGIS ALKIS Import** aus dem Startmenü 
oder der Windows-Suchleiste.

.. _img_dimp2:

.. image:: _static/png/dimp2.png

|

Füllen Sie die Eingabefelder, bis auf die von Ihnen festgelegten Werte, wie im obigen 
Beispiel aus. Geben Sie den bei Anleitung :ref:`cha_dbbereitstellung` vergebenen 
Datenbanknamen ein. Geben Sie die bei Anleitung :ref:`cha_installation` 
vergebenen Zugangsdaten für das Benutzerprofil des Serveradministrators (postgres) an.
(Siehe `Installation Abbildung_23 <installation.html#img-inst23>`_)

Setzen Sie den Haken bei ``Datenbestand (neu)anlegen`` wenn Sie einen Datenbestand 
neu anlegen oder einen bestehenden Bestand vollständig überschreiben möchten. 
Wählen Sie das Ihren ALKIS-Daten zugrundliegende Koordinatensystem. 
Das Koordinatensystem ist allerdings nur wichtig, wenn Ihre Kartendaten die 
richtige globale Referenz aufweisen sollen. Z.B. wenn Sie die Karte mit 
Satellitenfotos überlagern wollen. ALKIS-Datensätze sind meistens UTM32N referenziert. 
Siehe hierzu `<https://www.ldbv.bayern.de/file/png/10317/o/UTM_Zonen.png>`_  

.. _img_dimp3:

.. image:: _static/png/dimp3.png

|

Fügen Sie über die Schaltfläche ``Datei hinzufügen...`` oder 
``Verzeichnis hinzufügen...`` die zu importierenden Datensätze der 
``Dateiliste`` hinzu. Die ALKIS-Daten, auch NAS-Daten genannt, 
haben ein XML-Dateiformat und somit die Dateiendung XML.

.. _img_dimp4:

.. image:: _static/png/dimp4.png

|

Starten Sie den Datenimport, in die festgelegte Datenbank, 
mit der Formulartaste ``Starten``.
Sobald der Import erfolgreich abgeschlossen wurde, 
kann über die Formulartaste „Schließen“ das Programm beendet werden.

Sie können nun mit Anleitung :ref:`cha_projekterstellung` fortfahren 
und ein QGIS-Projekt erstellen.