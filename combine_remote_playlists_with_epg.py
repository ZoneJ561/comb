import requests

# Playlist URLs to combine
playlists = [
    "https://tvpass.org/playlist/m3u",
    "https://raw.githubusercontent.com/mikekaprielian/rtnaodhor93n398/refs/heads/main/en/videoall.m3u",
    "https://raw.githubusercontent.com/iptv-org/iptv/refs/heads/master/streams/us_moveonjoy.m3u"
    
    
]

# Combined EPG URL
epg_url = "https://github.com/BuddyChewChew/combine-remote-epg/raw/refs/heads/main/combined_epg.xml"

# Output file
output_file = "combined_playlist.m3u"

def fetch_and_combine_playlists():
    with open(output_file, "w", encoding="utf-8") as outfile:
        # Write header with EPG URL
        outfile.write(f'#EXTM3U x-tvg-url="{epg_url}"\n\n')

        for url in playlists:
            try:
                response = requests.get(url, timeout=15)
                response.raise_for_status()
                lines = response.text.splitlines()

                # Add 📺 source comment before the channels
                outfile.write(f'# 📺 Source: {url}\n')

                for line in lines:
                    if not line.startswith("#EXTM3U"):  # Skip the initial header
                        outfile.write(line + "\n")

                outfile.write("\n")  # Space between sources
                print(f"✅ Added channels from {url}")

            except Exception as e:
                print(f"❌ Failed to fetch {url}: {e}")

    print(f"\n✅ Combined playlist saved as '{output_file}' with EPG: {epg_url}")

if __name__ == "__main__":
    fetch_and_combine_playlists()
