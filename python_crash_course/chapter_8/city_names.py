def city_country(city,country):
    #formatting a city and his country
    format = f"{city.title()},{country.title()}"
    return format

cCountry1 = city_country('lima','Perú')
print(cCountry1)
cCountry2 = city_country('buenos Aires','argentina')
print(cCountry2)
cCountry3 = city_country('boston','USA')
print(cCountry3)