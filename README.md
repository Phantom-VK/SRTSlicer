# SRT Word-Level Timestamp Slicer

## Overview
A powerful tool to generate word-level timestamps from SRT subtitle files with advanced customization options.

## New Features
- Enhanced file selection with file type support
- Custom filename generation
- Flexible input and output file handling
- Prefix and suffix options for output files
- Auto-generate filename toggle

## Features
- Word-level timestamp generation
- Two distribution methods:
  1. Equal Time Distribution
  2. Word Length-based Distribution
- Preserve original subtitle structure
- User-friendly Tkinter GUI
- Customizable input and output

## UI Components

### Input File Section
- File path entry
- Browse button
- File type selection (SRT, TXT, All Files)

### Output File Section
- File path entry
- Browse button
- File type selection (SRT, TXT, All Files)

### Custom Filename
- Prefix input
- Suffix input
- Auto-generate toggle
  - Automatically creates output filename based on input file
  - Customizable prefix and suffix

### Distribution Methods
- Equal Time: Distributes time equally across words
- Word Length: Allocates time proportional to word length

## Installation

### Prerequisites
- Python 3.7+
- tkinter (usually comes with Python)
- cx_Freeze (for creating executable)

### Creating Executable
1. Install dependencies:
```bash
pip install cx_Freeze
```

2. Run setup script:
```bash
python setup.py build
```

## Usage
1. Select Input File
   - Use Browse button or enter file path manually
   - Choose file type (SRT, TXT, All Files)

2. Output File Options
   - Automatically generate filename
   - Customize with prefix/suffix
   - Manual file path selection

3. Choose Distribution Method
   - Equal Time
   - Word Length

4. Optional Settings
   - Preserve original subtitle structure
   - Select file types

5. Click "Process SRT"

## Advanced Filename Generation
- Prefix: Add custom prefix to output filename
- Suffix: Add custom suffix to output filename
- Auto-generate: Toggles automatic filename creation

## Supported Platforms
- Windows
- macOS
- Linux

## Troubleshooting
- Ensure input is a valid subtitle file
- Check file permissions
- Verify Python installation

## Contributing
Contributions are welcome! 
- Implement new features
- Improve existing functionality
- Report bugs


## Author
Vikramaditya Khupse