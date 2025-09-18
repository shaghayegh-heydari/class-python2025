my_song = ["song A", "song B", "song C", "song T", "song A", "song B"]

seen_song = set ()
duplicates = set ()

for song in my_song :
    if song in seen_song :
        duplicates.add(song)
    else :
        seen_song.add(song)

print("duplicates song")
for song in duplicates :
    print(f"duplicates{song}")