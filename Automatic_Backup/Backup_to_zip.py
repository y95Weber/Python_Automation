import os
import shutil
import glob
import logging
from datetime import datetime

# Konsistent Variables
SOURCE_FOLDER = r"C:\Users\Administrator\Desktop\IPLIS"
BACKUP_FOLDER = r"C:\Backups_TEST"
MAX_BACKUPS = 3
LOG_FILE = os.path.join(BACKUP_FOLDER, "backup_log.txt")


# --- Function 1: Logging Setup ---
def setup_logging():
    """
    Configures logging so that all messages (success/errors)
    are written to a log file with timestamp and severity level.
    """
    # Falls Backup Folder nicht vorhanden erstellen
    os.makedirs(BACKUP_FOLDER, exist_ok=True)

    # Logging wird eingerichtet
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8",
    )


# --- Function 2: Create Backup ---
def create_backup(source, backup_folder):
    """
    Creates a zip backup of the source folder and saves it
    in the backup folder. The filename includes a timestamp.
    Returns the full path of the created zip file.
    """

    # Falls Source Folder nicht vorhanden wird er erstellt
    os.makedirs(BACKUP_FOLDER, exist_ok=True)

    # Timestamp erstellen und filename
    date_str = datetime.now().strftime("%Y-%m-%d_%Hh%Mm%Ss")
    folder_name = os.path.basename(source)
    zip_name = f"Backup_{folder_name}_{date_str}"

    # Ganzer Pfad des Backup-Ordners speichern
    target_path = os.path.join(backup_folder, zip_name)

    # Zip Ordner erstellen
    shutil.make_archive(target_path, 'zip', source)

    # In Logdatei Speichern
    logging.info(f"Backup created: {target_path}.zip")

    return f"{target_path}.zip"




# --- Function 3: Cleanup Old Backups ---
def cleanup_old_backups(backup_folder, max_backups):
    """
    Checks how many backup zip files exist in the backup folder.
    If there are more than max_backups, the oldest ones are deleted
    until only max_backups remain.
    """

    # Alle Zip-Dateien finden, die dem Backup-Namensmuster entsprechen
    search_pattern = os.path.join(backup_folder, "Backup_*.zip")
    backup_files = glob.glob(search_pattern)

    # Nach Erstellungsdatum sortieren (älteste zuerst)
    backup_files.sort(key=os.path.getctime)

    # Falls mehr als max_backups vorhanden sind, älteste löschen
    while len(backup_files) > max_backups:
        oldest_file = backup_files.pop(0)
        os.remove(oldest_file)
        logging.info(f"Old backup deleted: {oldest_file}")



# Main Programm zum Ausführen
def main():
    """
    Orchestrates the backup process:
    sets up logging, creates a backup, and cleans up old backups.
    Handles errors so the script doesn't crash silently.
    """
    # Loggs Starten
    setup_logging()

    try:

        # Backup Erstellen starten
        print("---Backup---")
        create_backup(SOURCE_FOLDER, BACKUP_FOLDER)

        # Cleanup Starten
        print("---Cleanup---")
        cleanup_old_backups(BACKUP_FOLDER, MAX_BACKUPS)

        # Logging das alles funktioniert hat
        logging.info("Backup process completed successfully.")

    except Exception as e:
        logging.error(f"Backup process failed: {e}")

    print("Programm finished")

if __name__== "__main__":
    main()