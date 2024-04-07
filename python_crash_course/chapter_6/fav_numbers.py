fav_numbers = {
    'sebas' : 20,
    'caty' : 8,
    'bryan' : 12,
    'cony' : 22,
    'angelica' : 13,
}

person = 'sebas'
print(f"{person.title()}'s fav number is {fav_numbers[person]}")
person = 'caty'
print(f'{person.title()} fav number is {fav_numbers[person]}')
person = 'bryan'
print(f'{person.title()} fav number is {fav_numbers[person]}')
person = 'cony'
print(f'{person.title()} fav number is {fav_numbers[person]}')
person = 'angelica'
print(f'{person.title()} fav number is {fav_numbers[person]}')


print(f'\nCaty fav number is {fav_numbers["caty"]}')
print(f'Bryan fav number is {fav_numbers["bryan"]}')
print(f'Cony fav number is {fav_numbers["cony"]}')
print(f'Angélica fav number is {fav_numbers["angelica"]}')
