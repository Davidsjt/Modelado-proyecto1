import unittest
import pandas as pd
from backend.city_data_utils import load_iata_data, map_iata_to_city, get_closest_city_name, hex_to_iata

class TestCityDataUtils(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Cargar datos
        cls.iata_to_city, cls.valid_cities = load_iata_data('static/iata_cities.csv')
        cls.sample_data = pd.read_csv('static/Sample.csv')

    def test_map_iata_to_city(self):
        # Mapeo IATA
        self.assertEqual(map_iata_to_city('MEX', self.iata_to_city), 'Ciudad de Mexico')
        self.assertEqual(map_iata_to_city('OAX', self.iata_to_city), 'Oaxaca')
        self.assertIsNone(map_iata_to_city('XYZ', self.iata_to_city))  # Test for non-existent IATA code

    def test_get_closest_city_name(self):
        # Correccion ortográfica
        self.assertEqual(get_closest_city_name('Ne York', self.valid_cities), 'New York')
        self.assertEqual(get_closest_city_name('Montery', self.valid_cities), 'Monterrey')
        self.assertEqual(get_closest_city_name('UnknownCity', self.valid_cities), 'UnknownCity')  # Should return input if no close match

    def test_hex_to_iata(self):
        for index, row in self.sample_data.iterrows():
            expected_city = row['destination']
            print(f"Expected city is: {expected_city}")
            hex_ticket = row['ticket'].replace(" ", "")  # Remove any spaces if present
            actual_city = hex_to_iata(hex_ticket, self.iata_to_city)
            print(f"Actual city is: {actual_city}")
            self.assertEqual(actual_city, expected_city, f"Failed for ticket: {hex_ticket}")
        self.assertIsNone(hex_to_iata('4a464', self.iata_to_city))  # Incomplete hex code should return None

if __name__ == '__main__':
    unittest.main()
