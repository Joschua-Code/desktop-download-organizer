from pathlib import Path
import os
import time


def get_path(de_or_do):
    system_drive = os.getenv("SystemDrive")
    system_drive = system_drive + "\\"
    system_drive = Path(system_drive)
   
    if de_or_do == "de":
        return Path(system_drive / "- Safe -" / "Desktop")

    elif de_or_do == "do":
        return Path(system_drive / "- Safe -" / "Downloads")

    else:
        raise ValueError

#Create a Safe directory under the main disk and Desktop/Download directory in the Safe directory
def create_directorys():
    get_path("de").mkdir(parents=True, exist_ok=True) 
    get_path("do").mkdir(parents=True, exist_ok=True)

#Put everything from desktop into Save\Desktop - if its already there it will append a (Number) to the name
def move_desktop():
    desktop = Path.home() / "Desktop"
    desktop_not_to_move = {"thisonestays.txt"}

    for src in desktop.iterdir():
        if src in desktop_not_to_move: continue
        if src.name.lower() == "desktop.ini": continue

        move = get_path("de") / src.name

        for i in range(2, 100):
            if not move.exists():
                src.rename(move)
                break
            else:
                src_adjusted = src.with_stem(f"{src.stem} ({i})")
                move = get_path("de") / src_adjusted.name
                if not move.exists():
                    src.rename(move)
                    break

#Put everything from download into Save\Download
def move_download():
    download = Path.home() / "Downloads"
    download_not_to_move = {"thisonestays.txt"}

    for src in download.iterdir():
        if src in download_not_to_move: continue

        move = get_path("do") / src.name

        for i in range(2, 100):
            if not move.exists():
                src.rename(move)
                break
            else:
                src_adjusted = src.with_stem(f"{src.stem} ({i})")
                move = get_path("do") / src_adjusted.name
                if not move.exists():
                    src.rename(move)
                    break


#Check if there is already this exe in autostart if not copy it there

#Create an Uninstaller.exe that checks if this is in autostart and if yes it deletes it otherwise it says there is nothing to uninstall

#Create an .exe


if __name__ == "__main__":
    create_directorys() 

    for i in range(5):
        move_desktop()
        move_download()
        time.sleep(0.2)