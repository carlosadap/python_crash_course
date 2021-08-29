import unittest
from city_functions import get_formatted_city

class CitiesTestCase(unittest.TestCase):
    """Test for city_functions.py"""

    def test_city_country(self):
        """Do cities like 'Santigo, Chile' work?"""
        formatted_city = get_formatted_city('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')

    def test_city_country_population(self):
        """Do cities with populations work like: 'Madrid, Spain - population 3.400000'?"""
        formatted_city = get_formatted_city('madrid', 'spain', 3400000)
        self.assertEqual(formatted_city, 'Madrid, Spain - population 3400000')

if __name__ == '__main__':
    unittest.main()
