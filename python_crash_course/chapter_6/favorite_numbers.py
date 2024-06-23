fav_numbers = {
    'sebas' : [20,123,23],
    'caty' : [8,2,43],
    'bryan' : [12,42,65,86],
    'cony' : [22,443,9,76,0,5],
    'angelica' : [13,43,7],
}

for person, numbers in fav_numbers.items():
    print(f"\n{person.title()}'s favorite numbers are:")
    for number in numbers:
        print(f" - {number}")