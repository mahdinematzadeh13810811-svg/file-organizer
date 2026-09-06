# File Organizer

A simple and practical Python tool that automatically organizes files into folders based on their file type.

## Features

- Organizes images into `Images`
- Organizes documents into `Documents`
- Organizes videos into `Videos`
- Organizes music into `Music`
- Places unknown file types into `Others`
- Shows files before moving them
- Asks for confirmation before organizing
- Reports the number of moved files
- Handles invalid folder paths

## Supported File Types

| Category | Extensions |
|----------|------------|
| Images | `.jpg`, `.jpeg`, `.png`, `.gif` |
| Documents | `.txt`, `.pdf`, `.docx` |
| Videos | `.mp4`, `.mkv`, `.avi` |
| Music | `.mp3`, `.wav` |

## How to Run

```bash
python file_organizer.pyphoto.jpg -> Images
song.mp3 -> Music
document.txt -> Documents
video.mp4 -> Videos
unknown.xyz -> Others

