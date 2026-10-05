# File Organizer

A simple Python project that automatically organizes files in a folder by file type.

## Overview

This script scans the current working directory and moves files into category folders based on their extensions. It creates the folders automatically when you run it.

## Features

- Sorts files into categories such as Images, Documents, Audio, Videos, Archives, and Scripts
- Creates destination folders automatically if they do not exist
- Moves unsupported files into an `Others` folder
- Ignores subdirectories and only processes files

## Categories

The script currently organizes files into:

- `Images`: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`
- `Documents`: `.pdf`, `.docx`, `.txt`, `.xlsx`, `.pptx`
- `Audio`: `.mp3`, `.wav`, `.aac`
- `Videos`: `.mp4`, `.avi`, `.mov`, `.mkv`
- `Archives`: `.zip`, `.rar`, `.tar`, `.gz`
- `Scripts`: `.js`, `.html`, `.css`
- `Others`: any file that does not match a recognized category

## How to Run

1. Open a terminal in the `File_Organizer` folder.
2. Run:

```bash
python main.py
```

The script will organize the files in the current directory where it is executed.

## Important Note

The script uses:

```python
FOLDER_PATHS = os.getcwd()
```

This means it organizes the files in the directory you run the script from. If you want to organize a different folder, update the `FOLDER_PATHS` value in `main.py`.

## Example

Before:

```text
project/
├── notes.txt
├── photo.jpg
├── song.mp3
├── script.js
└── archive.zip
```

After running the script:

```text
project/
├── Documents/
│   └── notes.txt
├── Images/
│   └── photo.jpg
├── Audio/
│   └── song.mp3
├── Scripts/
│   └── script.js
├── Archives/
│   └── archive.zip
```

## Requirements

- Python 3.x
- No external libraries required
