import requests

# Playlist URLs and their group titles
playlists = [
    ("https://tvpass.org/playlist/m3u", "TVPass"),
    ("https://raw.githubusercontent.com/mikekaprielian/rtnaodhor93n398/refs/heads/main/en/videoall.m3u", "Mike's Playlist"),
    ("https://raw.githubusercontent.com/PyC7aM/IPTV/refs/heads/main/USTV.m3u8", "USTV"),
]

# EPG URL
epg_url = "https://github.com/BuddyChewChew/combine-remote-epg/raw/refs/heads/main/combined_epg.xml"

output_file = "combined_playlist.m3u"

with open(output_file, "w", encoding="utf-8") as outfile:
    # Write the EXT header with EPG link
    outfile.write(f'#EXTM3U x-tvg-url="{epg_url}"\n\n')

    for url, group_title in playlists:
        try:
            response = requests.get(url, timeout=15)
            response.raise_for_status()
            lines = response.text.splitlines()

            print(f"✅ Processing {group_title} - {url}")

            for line in lines:
                if line.startswith("#EXTINF"):
                    if 'group-title' not in line:
                        parts = line.split(",", 1)
                        if len(parts) == 2:
                            info_part, channel_name = parts
                            line = f'{info_part} group-title="{group_title}",{channel_name}'

                if not line.startswith("#EXTM3U"):
                    outfile.write(line + "\n")

            outfile.write("\n")

        except Exception as e:
            print(f"❌ Failed to fetch {url}: {e}")

print(f"\n✅ Combined playlist saved as '{output_file}' with EPG: {epg_url}")
