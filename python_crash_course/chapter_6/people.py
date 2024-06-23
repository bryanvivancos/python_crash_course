people = []

person = {
    'first name' : 'sebastian',
    'last name' : 'vivanco',
    'age' : 19,
    'city' : 'piura',
}
people.append(person)

person = {
    'first name' : 'caty',
    'last name' : 'quiroz',
    'age' : 26,
    'city' : 'lima',
}
people.append(person)

person = {
    'first name' : 'bryan',
    'last name' : 'vivanco',
    'age' : 26,
    'city' : 'piura',
}
people.append(person)

for person in people:
    name = f"{person['first name'].title()} {person['last name'].title()}"
    age = f"{person['age']}"
    location = f"{person['city'].title()}"
    
    print(f"\n{name}, {age} years old, from {location}")