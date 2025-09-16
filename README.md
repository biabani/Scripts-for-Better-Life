# My Python Utility Scripts

This repository contains several small but useful Python scripts.  
Each script is in its own folder with a dedicated README for usage details.

## Available Scripts

### 1. [add_subs_to_mkv/](add_subs_to_mkv)
Embed external `.srt` subtitles into `.mkv` video files using `mkvmerge` from [MKVToolNix](https://mkvtoolnix.download/).  
- Matches subtitles and videos based on season/episode numbers.  
- Converts numbering style from `1x01` → `S01E01`.  
- Keeps the original file intact and creates a new MKV with the embedded subtitle.  

### 2. [zip_folders/](zip_folders)
Automatically compresses each folder in the current directory into a `.zip` archive.  
- Scans all folders in the current directory.  
- Creates a ZIP file for each folder.  
- Preserves the folder structure inside the archive.  
