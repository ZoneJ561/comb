import requests

# Playlist URLs to combine
playlists = [
    "https://tvpass.org/playlist/m3u",
    "https://raw.githubusercontent.com/mikekaprielian/rtnaodhor93n398/refs/heads/main/en/videoall.m3u",
    "https://raw.githubusercontent.com/PyC7aM/IPTV/refs/heads/main/USTV.m3u8",
]

# EPG URL
epg_url = "https://github.com/BuddyChewChew/combine-remote-epg/raw/refs/heads/main/combined_epg.xml"

output_file = "combined_playlist.m3u"

with open(output_file, "w", encoding="utf-8") as outfile:
    # Write the EXT header with EPG link
    outfile.write(f'#EXTM3U x-tvg-url="{epg_url}"\n\n')

    for url in playlists:
        try:
            response = requests.get(url, timeout=15)
            response.raise_for_status()
            lines = response.text.splitlines()

            # Add 📺 emoji and source URL as a comment before each playlist block
            outfile.write(f'# 📺 Source: {url}\n')

            # Skip the first line if it's an #EXTM3U (we already added our own above)
            for line in lines:
                if not line.startswith("#EXTM3U"):
                    outfile.write(line + "\n")

            outfile.write("\n")  # Add a blank line between playlist sections

            print(f"✅ Added channels from {url}")

        except Exception as e:
            print(f"❌ Failed to fetch {url}: {e}")

print(f"\n✅ Combined playlist saved as '{output_file}' with EPG: {epg_url}")
