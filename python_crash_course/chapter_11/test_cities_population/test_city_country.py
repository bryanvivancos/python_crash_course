from city_functions import get_formatted_city_country
#test the function city_country
def test_city_country():
    """Do words 'santiago, chile' work?"""
    format = get_formatted_city_country('santiago','chile')
    assert format == 'Santiago, Chile.'
    
def test_city_country_population():
    """Do words 'santiago, chile and population' work?"""
    format = get_formatted_city_country('santiago','chile',5000000)
    assert format == 'Santiago, Chile - population 5000000.'