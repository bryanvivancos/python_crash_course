favorite_places = {
    'sebastian' : ['las vegas','university','paris'],
    'caty' : ['lima','washigton','ohio'],
    'ximena' : ['madrid','england','usa']
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f" - {place.title()}")