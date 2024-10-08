from city_functions import get_formatted_city_country
#test the function city_country
def test_city_country():
    """Do words 'santiago, chile' work?"""
    format = get_formatted_city_country('santiago','chile')
    assert format == 'Santiago, Chile.'