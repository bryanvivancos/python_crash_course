cities = {
    'madrid' : {
        'country':'españa',
        'population':503_004,
        'season':'summer',
        },
    'barcelona' : {
        'country':'españa',
        'population':600_322,
        'season':'summer',
        },
    'santiago' : {
        'country':'chile',
        'population':6_310_000,
        'season':'winter',
        },
}

for city, city_info in cities.items():
    country = f"{city_info['country']}"
    population = f"{city_info['population']}"
    season = f"{city_info['season']}"
    
    print(f"\n{city.title()} is in {country}.")
    print(f"  It has a population of about {population}.")
    print(f"  The actual season is: {season.title()}")