def make_album(artist_name,album_title):
    album = {'artist': artist_name.title(), 'title':album_title.title()}
    return album

while True:
    print("\nInput the name and his/her album")
    print("(press 'q' if you want to quit)")
    
    artist = input("Input the Artist name: ")
    if artist == 'q':
        break
    title = input("Input the Album name: ")
    if title == 'q':
        break
    
    album_description = make_album(artist,title)
    print(album_description)

