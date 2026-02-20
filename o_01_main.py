from pathlib import Path
import os


print(f" Here comes the current path: {Path.cwd()}")
print(f"Here come the files in the current directory.")

for i, x in enumerate(Path.cwd().iterdir()):
    print(f"{i+1}: {x}")
    print(type(str(x)))
    print(x.name)

for i, x in enumerate((Path.home() / "Desktop").iterdir()):
    print(f"{i+1}: {x}")


home = Path.home() / "Desktop"

(home / "2026").mkdir(exist_ok=True)
save = Path

system_drive = os.getenv("SystemDrive")
system_drive = system_drive + "\\"





safe_directory = Path(system_drive + "\\- Safe --")
safe_directory.mkdir(exist_ok=True)









