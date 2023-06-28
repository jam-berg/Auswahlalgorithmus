# Auswahlalgorithmus
## Zweck
Dieses Program dient dazu die Gruppen möglichst fair zuzuteilen, damit es im Durchschnitt eine hohe Zufriedenheit gibt. 

## Verwendung
Als erstes werden die Präferenzen der Gruppen in das InputProjektePräferenz.csv eingetragen. Darin kann auch die Anzahl der Gruppen und Projekte ergänzt oder verringert werden. 
Anschliessend wird das Main.py Skript ausgeführt. Danach werden die Resultate in der Konsole ausgegeben und werden im resulting_constellation.txt Textfile gespeichert.   

## Modifizierung
Im Python Skript kann die Anzahl der Iterationen angepasst werden, was aber auch die Laufzeit erhöht.
Ein mehreres durchführen des Programmes kann dazu führen, dass es einen höheren Zufriedenheitswert gibt, falls sich der Zufriedenheitwert der vorherigen Durchführung in einem lokalen Minimum befand. 
