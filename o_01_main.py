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


#Moves Private/Public/OneDrive Desktop files and moves them to there respective directories in the Save directory.
def move():
    #   private desktop
    move_all((Path.home() / "Desktop"), get_path("de"))
    #   public desktop
    move_all((Path.home().parent / "Public" / "Desktop"), get_path("de"))
    #   OneDrive desktop
    one_drive_path = (Path.home() / "OneDrive" / "Desktop")
    if one_drive_path.is_dir():
        move_all((Path.home() / "OneDrive" / "Desktop"), get_path("de"))

    #   downloads
    move_all((Path.home() / "Downloads"), get_path("do"))


#Put everything from src_folder to dest_folder. If its already there it will append a (Number) to the name.
def move_all(src_folder: Path, dest_folder: Path) -> None:
    not_to_move = {"thisonestays.txt"}

    for src in src_folder.iterdir():
        if src in not_to_move: continue
        if src.name.lower() == "desktop.ini": continue

        move = dest_folder / src.name

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


#Create an .exe

#Check if there is already this exe in autostart if not copy it there

#Create an Uninstaller.exe that checks if this is in autostart and if yes it deletes it otherwise it says there is nothing to uninstall


if __name__ == "__main__":
    create_directorys() 

    for i in range(5):
        move()
        time.sleep(0.2)