rivers = {
    'Hai' : 'Pekín',
    'Han' : 'Seúl',
    'Tigris' : 'Bagdad'
}

for river, country in rivers.items():
    print(f"\n The {river} runs through {country}")
    
for river in rivers.keys():
    print(f"\n {river}")
    
for country in rivers.values():
    print(f"\n {country}")