import unittest
from city_function_0 import location_info 

class CityCountryTestCase(unittest.TestCase):
    """ Test for 'city_function_0.py' """
    
    def test_city_country(self):
        """Does the names like 'Daly City America' work?"""
        formatted_name = location_info("daly city", "america")
        self.assertEqual(formatted_name, "Daly City, America")
        
if __name__ == "__main__":
    unittest.main()