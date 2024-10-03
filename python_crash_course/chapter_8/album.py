def make_album(artist_name,album_title):
    album = {'artist': artist_name.title(), 'title':album_title.title()}
    return album

n1 = make_album('michael Jackson', 'history')
print(n1)
n1 = make_album('ariana Grande', 'the way')
print(n1)
n1 = make_album('beyonce', 'gold')
print(n1)

def make_album(artist_name,album_title,number_songs=None):
    album = {'artist': artist_name.title(), 'title':album_title.title()}
    if number_songs:
        album['number of songs'] = number_songs
    return album

n4 = make_album('ariana Grande', 'the way',9)
print(n4)