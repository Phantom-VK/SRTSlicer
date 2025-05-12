import sys
from cx_Freeze import setup, Executable
import os

# Dependencies that are common across all platforms
base_packages = [
    "tkinter",
    "os",
    "re",
    "datetime"
]

# Platform-specific configurations
if sys.platform == "win32":
    base = "Win32GUI"  # For Windows GUI apps
    include_files = [
        ("app_icon.ico", "app_icon.ico"),
    ]
    # Windows-specific dependencies
    packages = base_packages + []
elif sys.platform.startswith('linux'):
    base = None  # Console application
    include_files = []
    # Linux-specific dependencies
    packages = base_packages + []
else:
    raise RuntimeError("Unsupported platform")

# Build options
build_exe_options = {
    "packages": packages,
    "excludes": [
        "tkinter.test",
        "tkinter.ttk.test",
        "unittest",
        "email",
        "http",
        "urllib",
        "logging",
        "numpy"  # Often causes issues if not needed
    ],
    "include_files": include_files,
    "zip_include_packages": ["*"],
    "zip_exclude_packages": [],
    "optimize": 2,  # Maximum optimization
    # Important for Windows compatibility
    "include_msvcr": True if sys.platform == "win32" else False
}

# Executable configuration
executables = [
    Executable(
        "srt_slicer.py",
        base=base,
        target_name="srt_slicer" + (".exe" if sys.platform == "win32" else ""),
        icon="app_icon.ico" if sys.platform == "win32" else None,  # Linux doesn't use .ico
        copyright="Your Copyright Here",
        trademarks="Your Trademarks Here"
    )
]

setup(
    name="SRT Word-Level Timestamp Slicer",
    version="1.0.0",
    description="SRT File Word-Level Timestamp Generator",
    options={"build_exe": build_exe_options},
    executables=executables
)