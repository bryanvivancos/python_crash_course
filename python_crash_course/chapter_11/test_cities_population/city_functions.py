#function that accepts two parameters (city name and a country name)
def get_formatted_city_country(city,country,population = 0):
    if population:
        format = f'{city.title()}, {country.title()} - population {population}.'
    else:
        format = f'{city.title()}, {country.title()}.'
    return format     