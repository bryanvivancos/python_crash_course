pets = []

pet = {
    "animal type" : "fish",
    "name" : "nemo",
    "owner" : "lucas"
}
pets.append(pet)

pet = {
    "animal type" : "reptile",
    "name" : "croco",
    "owner" : "angelica"
}
pets.append(pet)

pet = {
    "animal type" : "bird",
    "name" : "lucas",
    "owner" : "caty"
}
pets.append(pet)

pet = {
    "animal type" : "dog",
    "name" : "boby",
    "owner" : "sebastian"
}
pets.append(pet)

for pet in pets: 
    print(f"\nHere is what i know about pet {pet['name'].title()}:")
    for key,values in pet.items():
        print(f"\t{key.title()}: {values.title()}")