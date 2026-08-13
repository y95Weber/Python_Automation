# Automatic Backup
 
Ein Python-Skript, das einen Ordner zeitgesteuert (via Windows Task Scheduler) als ZIP-Datei sichert, ältere Backups automatisch aufräumt und alles protokolliert.
 
## Funktionsweise
 
1. Erstellt eine ZIP-Kopie des Quellordners
2. Speichert sie im Backup-Ordner mit Zeitstempel im Namen (`Backup_<Ordnername>_<Datum>_<Uhrzeit>.zip`)
3. Prüft, wie viele Backups bereits vorhanden sind
4. Löscht automatisch das/die älteste(n) Backup(s), falls mehr als die konfigurierte Anzahl vorhanden sind
5. Schreibt jeden Schritt (Erfolg oder Fehler) in eine Log-Datei (`backup_log.txt`)
## Voraussetzungen
 
- Windows
- [Python 3](https://www.python.org/downloads/) installiert (mit aktivierter Option "Add Python to PATH" während der Installation)
- [Git](https://git-scm.com/downloads) installiert
- Keine externen Pakete nötig – alle verwendeten Module (`os`, `shutil`, `glob`, `logging`, `datetime`) gehören zur Python-Standardbibliothek
## Installation
 
### 1. Repository klonen
 
Öffne die Eingabeaufforderung (CMD) oder PowerShell an dem Ort, wo du das Projekt ablegen möchtest, und führe aus:
 
```bash
git clone https://github.com/y95Weber/Python_Automation.git
```
 
### 2. In den Projektordner wechseln
 
```bash
cd Python_Automation\Automatic_Backup
```
 
### 3. Python-Installation prüfen
 
```bash
python --version
```
 
Falls dieser Befehl einen Fehler ausgibt, ist Python nicht korrekt installiert oder nicht im PATH.
 
## Konfiguration
 
Bevor du das Skript ausführst, öffne die Datei `Backup_to_zip.py` in einem Editor (z. B. VS Code, PyCharm, Notepad++) und passe die folgenden Variablen im Abschnitt **Konsistent Variables** an deine Umgebung an:
 
```python
SOURCE_FOLDER = r"C:\Pfad\zu\deinem\Ordner"
BACKUP_FOLDER = r"C:\Backups"
MAX_BACKUPS = 3
```
 
| Variable | Bedeutung | Beispiel |
|---|---|---|
| `SOURCE_FOLDER` | Ordner, der gesichert werden soll | `r"C:\Users\Name\Dokumente\Projekt"` |
| `BACKUP_FOLDER` | Zielordner für ZIP-Dateien und Log. Wird automatisch erstellt, falls nicht vorhanden | `r"D:\Backups"` |
| `MAX_BACKUPS` | Maximale Anzahl an Backups, die aufbewahrt werden | `3`, `5`, `10` |
 
**Wichtig:** Pfade müssen mit `r"..."` (Raw String) geschrieben werden, wegen der Backslashes `\` in Windows-Pfaden.
 
## Manuelles Testen
 
Führe das Skript einmal manuell aus, um sicherzustellen, dass alles funktioniert, bevor du es automatisierst:
 
```bash
python Backup_to_zip.py
```
 
Prüfe danach:
- Ob im `BACKUP_FOLDER` eine neue ZIP-Datei mit Zeitstempel im Namen aufgetaucht ist
- Ob eine `backup_log.txt` mit einer Erfolgsmeldung erstellt wurde
## Automatisierung mit dem Windows Task Scheduler
 
1. **Aufgabenplanung** öffnen (Windows-Suche → "Aufgabenplanung" bzw. "Task Scheduler")
2. Im rechten Menü **Einfache Aufgabe erstellen...** wählen
3. Namen vergeben, z. B. `Automatic Backup`
4. Zeitpunkt/Häufigkeit festlegen (z. B. täglich um 20:00 Uhr)
5. Als Aktion **"Programm starten"** wählen
6. Bei **Programm/Skript**: Pfad zur Python-Installation eintragen
   Den Pfad findest du mit:
```bash
   where python
```
   Beispiel: `C:\Users\Name\AppData\Local\Programs\Python\Python312\python.exe`
 
7. Bei **Argumente hinzufügen (optional)**: Pfad zum Skript eintragen, z. B.:
```
   C:\Pfad\zu\Python_Automation\Automatic_Backup\Backup_to_zip.py
```
8. Fertigstellen und testen: Aufgabe im Task Scheduler rechtsklicken → **Ausführen**
## Kontrolle, ob die Automatisierung funktioniert
 
- Im `BACKUP_FOLDER` sollten regelmäßig neue ZIP-Dateien mit Zeitstempel im Namen auftauchen
- In `backup_log.txt` (im selben Ordner) erscheint pro Durchlauf eine Zeile, z. B.:
```
  2026-08-13 20:00:01 - INFO - Backup created: C:\Backups\Backup_Projekt_2026-08-13_20h00m01s.zip
  2026-08-13 20:00:02 - INFO - Backup process completed successfully =)
```
- Bei Fehlern erscheint stattdessen eine `ERROR`-Zeile mit der genauen Fehlermeldung
## Typische Fehlerquellen
 
| Problem | Mögliche Ursache |
|---|---|
| Skript startet nicht über Task Scheduler | Falscher Python-Pfad im Task Scheduler hinterlegt |
| `FileNotFoundError` | `SOURCE_FOLDER` existiert nicht oder ist falsch geschrieben |
| Kein Backup wird erstellt | Keine Schreibrechte im `BACKUP_FOLDER` |
| Skript läuft manuell, aber nicht automatisch | Task Scheduler-Aufgabe nicht korrekt konfiguriert (falscher Pfad, falscher Trigger) |
 
## Repository-Struktur
 
```
Python_Automation/
└── Automatic_Backup/
    ├── Backup_to_zip.py
    └── README.md
```
 
## Lizenz / Nutzung
 
Dieses Skript dient zu Lern- und Automatisierungszwecken. Vor dem produktiven Einsatz empfiehlt sich ein Test mit einem unwichtigen Beispielordner.