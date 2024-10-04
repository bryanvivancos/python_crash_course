def make_album(artist_name,album_title):
    #create a dict with the album data
    album = {'artist': artist_name.title(), 'title':album_title.title()}
    return album

#input the album data with a loop
while True:
    print("\nInput the name and his/her album")
    print("(press 'q' if you want to quit)")
    
    #making a way to quit
    artist = input("Input the Artist name: ")
    if artist == 'q':
        break
    title = input("Input the Album name: ")
    if title == 'q':
        break
    
    #running the function and print the album data
    album_description = make_album(artist,title)
    print(album_description)

