# Add Subtitles to MKV

## Overview
This Python script automatically embeds external **English subtitle files (.srt)** into **MKV video files** without altering the original video file.  
It adds subtitles as **soft-sub tracks**, meaning subtitles can be turned on/off in the video player.

It is especially useful if:  
- Your MKV files already contain one subtitle track (e.g., Persian) and you want to add another language.  
- You have multiple episodes of a TV show and want to automatically match subtitles to the correct episode based on filenames.

---

## Features
- Scans the current folder for `.mkv` and `.srt` files.  
- Matches each subtitle file to its corresponding episode using season/episode numbers in filenames (e.g., `Friends - 1x01 ...` ↔ `Friends.S01E01 ...`).  
- Converts numbering style from `1x01` to `S01E01` for consistency in output filenames.  
- Keeps the original video file untouched.  
- Generates a new `.mkv` file with the embedded English subtitle track.

---

## Requirements
- **Python 3.7+**  
- **MKVToolNix** (must include `mkvmerge` in your PATH): [https://mkvtoolnix.download/](https://mkvtoolnix.download/)

Check `mkvmerge` installation:
```bash
mkvmerge --version
```


## Usage
Run the script inside the folder containing your .mkv and .srt files:

```bash
# Using Python
python3 add_sub.py
```

The script will:

1- Detect all .mkv files.

2- Detect all .srt files containing .en. in their filename (only English subtitles).

3- Match each subtitle to its corresponding video episode.

4- Create a new MKV file with the English subtitle embedded.

### Example:

Input files:

```
Friends - 1x01 - The One Where Monica Gets a Roommate.BluRay.en.srt
Friends.S01E01.720p.BluRay.SoftSub.Unknown.DonyayeSerial.mkv
```
Output file:

```
Friends - S01E01 - The One Where Monica Gets a Roommate.BluRay.en.mkv
```
The original MKV remains untouched.

Notes
Filenames must contain the season/episode info for proper matching:

- 1x01 
- S01E01

The script only embeds English subtitles (.en. in the filename).

If the output file already exists, the script will skip it to avoid overwriting.

Soft-sub format allows toggling subtitles on/off in media players.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
