#function that accepts two parameters (city name and a country name)
def get_formatted_city_country(city,country):
    format = f'{city}, {country}.'
    return format.title()     