#!/usr/bin/env python3
import re
import shutil
import subprocess
from pathlib import Path

# Regex patterns
video_pattern = re.compile(r'[sS](\d{1,2})[eE](\d{1,2})')   # Matches S01E01
sub_x_pattern = re.compile(r'(\d{1,2})x(\d{1,2})', re.IGNORECASE)  # Matches 1x01

BASE = Path(".")

def find_episode_in_name(name: str):
    """Extract (season, episode) tuple from a filename."""
    m = video_pattern.search(name)
    if m:
        return int(m.group(1)), int(m.group(2))
    m = sub_x_pattern.search(name)
    if m:
        return int(m.group(1)), int(m.group(2))
    return None

def replace_episode_token(name: str, season: int, episode: int):
    """Replace 1x01 with S01E01 in subtitle filename. If already in SxxExx format, leave it."""
    new = sub_x_pattern.sub(f"S{season:02d}E{episode:02d}", name, count=1)
    if new != name:
        return new
    return name

def main():
    # Check mkvmerge availability
    if shutil.which("mkvmerge") is None:
        print("❌ mkvmerge not found. Make sure mkvtoolnix-tools is installed and in PATH.")
        return

    videos = list(BASE.glob("*.mkv"))
    subs = [f for f in BASE.glob("*.srt") if ".en." in f.name.lower()]  # Only English subtitles

    # Map (season, episode) -> subtitle file
    sub_map = {}
    for s in subs:
        ep = find_episode_in_name(s.name)
        if ep:
            sub_map[ep] = s

    for video in videos:
        ep = find_episode_in_name(video.name)
        if not ep:
            continue
        season, episode = ep
        if ep not in sub_map:
            print(f"⚠️ No English subtitle found for {video.name}")
            continue

        subtitle = sub_map[ep]
        new_name = replace_episode_token(subtitle.name, season, episode)
        output_path = video.with_name(str(Path(new_name).with_suffix(".mkv")))

        if output_path.exists():
            print(f"⏩ Output already exists, skipped: {output_path.name}")
            continue

        # mkvmerge command
        cmd = [
            "mkvmerge", "-o", str(output_path),
            str(video),
            "--language", "0:en", str(subtitle)
        ]

        print(f"➕ Adding {subtitle.name} -> {output_path.name}")
        subprocess.run(cmd, check=True)
        print(f"✅ Done: {output_path.name}")

if __name__ == "__main__":
    main()
