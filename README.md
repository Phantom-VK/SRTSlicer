

# 🎬 SRT Word-Level Timestamp Slicer

## Overview
A powerful desktop utility that generates **word-level timestamps** from SRT subtitle files. Includes a sleek, customizable Tkinter UI with smart options for input/output, filename handling, and time distribution.

---

## 🚀 Features

- 🧠 Word-level timestamp slicing
- 🛠️ Two distribution methods:
  - Equal Time
  - Word Length-based
- 🗂️ Flexible input/output file selection
- ✍️ Custom prefix & suffix for output
- ⚙️ Auto-generate filenames toggle
- 🖼️ User-friendly GUI

---

## 🧩 UI Components

### 📂 Input File Section
- File path entry
- Browse file button
- File type filters (SRT, TXT, All Files)

### 💾 Output File Section
- Output path entry
- Auto-generate toggle
- Custom prefix and suffix fields

### 📊 Distribution Method
- Equal Time Distribution
- Word Length-based Distribution

### ✅ Extra Options
- Preserve subtitle structure
- File type selection for output

---

## 🗂️ Project Structure

```

SRT\_Slicer/
├── main.py                  ← Entry point
├── main.spec                ← PyInstaller spec file
├── app_icon1.ico            ← App icon for .exe
├── srt_slicer_logic.py      ← Core logic
├── srt_slicer_ui.py         ← GUI logic (Tkinter)
├── srt_slicer.iss           ← Inno Setup script
├── dist/
│   └── SRTSlicer.exe        ← Generated executable
├── output/
│   └── SRT_Slicer_Installer.exe ← Final installer
└── README.md

````

---

## 📥 For Users: How to Install & Use

### 🔧 Installation

1. Download the latest version of `SRT_Slicer_Installer.exe` from the [Releases](#).
2. Run the installer and follow the setup wizard.
3. Launch the app from the Desktop shortcut or Start Menu.

### 🧪 Using the App

1. Open the app.
2. Select your SRT or TXT input file.
3. Customize output filename or use auto-generate.
4. Pick the desired timestamp distribution method.
5. Click **"Process SRT"** – your new subtitle file will be generated.

---

## 🧑‍💻 For Developers: Build Instructions

### 📦 Prerequisites

- Python 3.7+
- PyInstaller
- Inno Setup (for installer creation)

### 🐍 Step 1: Build `.exe` with PyInstaller

```bash
pip install pyinstaller
pyinstaller main.spec
````

> ✅ Output: `dist/SRTSlicer.exe`

### 📦 Step 2: Build Installer with Inno Setup

1. Install [Inno Setup](https://jrsoftware.org/isinfo.php).
2. Open `srt_slicer.iss` in the Inno Setup Compiler.
3. Press **F9** to compile the installer.

> ✅ Output: `output/SRT_Slicer_Installer.exe`

---

## ⚙️ Advanced Filename Customization

* `Prefix`: Add text before the filename.
* `Suffix`: Add text after the filename.
* `Auto-generate`: Create names dynamically from input + prefix/suffix.

---

## 🖥️ Platform Support

* ✅ Windows (Packaged and Tested)
* ⚠️ macOS/Linux (Run via Python source only)

---

## 🧯 Troubleshooting

| Issue                     | Solution                                            |
| ------------------------- | --------------------------------------------------- |
| GUI not launching         | Use the `.exe` from the `dist/` or installer output |
| File not processed        | Make sure it's a valid `.srt` or `.txt` file        |
| Icon missing in .exe      | Check `.ico` path in `.spec` file and rebuild       |
| Output not saved properly | Ensure you have write permission and correct path   |

---

## 🤝 Contributing

All contributions are welcome!

* 💡 Suggest features
* 🐞 Report bugs
* 🔧 Submit improvements

Fork the repo, push changes, and open a pull request.

---

## 👨‍💻 Author

**Vikramaditya Khupse**
*Third Year IT Student | Python & Kotlin Dev | AI/ML Learner*
📫 [Contact Me](mailto:vikramadityakhupse.com)

---



This version is:

- Clean and developer-friendly
- User-focused with proper install steps
- Compatible with your new `.spec` and `.iss` setup
- Ready for GitHub or any documentation system

Let me know if you want to:

- Add screenshots/gifs
- Generate badges (e.g., "Built with PyInstaller")
- Link to releases
- Add versioning or changelog section
