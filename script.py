from ytmusicapi import YTMusic

ytmusic = YTMusic()

content = ytmusic.get_playlist('PLrBzvA1TJnge63cOxrng8N_Yu4lIbdYiH', limit=200)

artists = {}
for entry in content['tracks']:
    artist = entry['artists'][0]['name']
    if artist in artists.keys():
        artists[artist] = artists[artist] + 1
    else:
        artists[artist] = 1

artists = {k: v for k, v in sorted(artists.items(), key=lambda item: item[1], reverse=True)}
print(artists)