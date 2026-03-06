import unittest
from city_functions_2 import location_info

class CityCountryTestCase(unittest.TestCase):
    """ Test for 'city_function_2.py' """
    
    def test_city_country(self):
        """Does the names like 'Daly City America' work?"""
        formatted_name = location_info("daly city", "america")
        self.assertEqual(formatted_name, "Daly City, America")
        
    def test_city_country_population(self):
        """Does the information like 'Daly City Ameriica - Population 3000 work' ?"""
        formatted_information = location_info("paris", "france", 450123)
        self.assertEqual(formatted_information, "Paris, France - Population 450123")
        
if __name__ == "__main__":
    unittest.main()