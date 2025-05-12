import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["tkinter", "os", "re", "datetime"],
    "excludes": ["tkinter.test", "tkinter.ttk.test"],
    "include_files": [
        # Add your icon file here
        ("app_icon.ico", "app_icon.ico")
    ]
}

# GUI applications require a different base on Windows
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="SRT Word-Level Slicer",
    version="1.0",
    description="SRT File Word-Level Timestamp Generator",
    options={"build_exe": build_exe_options},
    executables=[Executable(
        "srt_slicer.py",
        base=base,
        icon="app_icon.ico",
        shortcut_name="SRT Word-Level Slicer",
        shortcut_dir="DesktopFolder"
    )]
)

# Detailed Usage Instructions:
# 1. Prepare an icon file named 'app_icon.ico'
# 2. Place the icon in the same directory as this script
# 3. Install cx_Freeze: pip install cx_Freeze
# 4. Run this script: python setup.py build