import os
import shutil
import platform
import time
from pathlib import Path

FILENAME = "ouvre_moi.txt"

def copy_to_usb(drive_path):
    source_file = Path.home() / FILENAME
    marker_file = drive_path / f".{FILENAME}.copied"

    print(f"➡️ Vérification de {drive_path}")

    if not source_file.exists():
        print(f"❌ Le fichier source n'existe pas : {source_file}")
        return

    if not os.access(drive_path, os.W_OK):
        print(f"❌ Pas de permission d’écriture sur {drive_path}")
        return

    try:
        with open(source_file, 'r') as f:
            f.read(1)
    except Exception as e:
        print(f"❌ Impossible de lire le fichier source : {e}")
        return

    try:
        if not marker_file.exists():
            shutil.copy(source_file, drive_path)
            marker_file.touch()
            print(f"✅ Fichier copié sur {drive_path}")
        else:
            print(f"ℹ️ Fichier déjà copié sur {drive_path}")
    except Exception as e:
        print(f"❌ Erreur lors de la copie sur {drive_path} : {e}")


# Windows only: vérifie si un lecteur est amovible
def is_removable(drive_letter):
    import ctypes
    DRIVE_REMOVABLE = 2
    drive_type = ctypes.windll.kernel32.GetDriveTypeW(f"{drive_letter}:\\")
    return drive_type == DRIVE_REMOVABLE

def windows_mode():
    print("🟢 Mode Windows : Surveillance des clés USB")
    seen = set()
    while True:
        for letter in "DEFGHIJKLMNOPQRSTUVWXYZ":
            drive = Path(f"{letter}:\\")
            if drive.exists() and drive not in seen and is_removable(letter):
                copy_to_usb(drive)
                seen.add(drive)
        time.sleep(5)

def linux_mode():
    print("🟢 Mode Linux : Surveillance des montages dans /media/$USER")
    mount_dir = Path(f"/media/{os.getenv('USER')}")
    if not mount_dir.exists():
        print(f"❌ Dossier de montage introuvable : {mount_dir}")
        return

    while True:
        current_volumes = set(vol for vol in mount_dir.glob("*") if vol.is_dir())
        for vol in current_volumes:
            print(f"📦 Détection d’un volume : {vol}")
            copy_to_usb(vol)
        time.sleep(5)

if __name__ == "__main__":
    system = platform.system()
    if system == "Windows":
        windows_mode()
    elif system == "Linux":
        linux_mode()
    else:
        print("❌ Système non pris en charge.")
