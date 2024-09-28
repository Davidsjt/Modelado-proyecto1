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
        self.assertEqual(map_iata_to_city('MEX', self.iata_to_city), 'Ciudad de México')
        self.assertEqual(map_iata_to_city('OAX', self.iata_to_city), 'Oaxaca')
        self.assertEqual(map_iata_to_city('CUN', self.iata_to_city), 'Cancún')
        self.assertEqual(map_iata_to_city('GDL', self.iata_to_city), 'Guadalajara')
        self.assertEqual(map_iata_to_city('MTY', self.iata_to_city), 'Monterrey')
        self.assertEqual(map_iata_to_city('PVR', self.iata_to_city), 'Puerto Vallarta')
        self.assertEqual(map_iata_to_city('SJD', self.iata_to_city), 'San José del Cabo')
        self.assertEqual(map_iata_to_city('VER', self.iata_to_city), 'Veracruz')
        self.assertEqual(map_iata_to_city('HUX', self.iata_to_city), 'Huatulco')
        self.assertEqual(map_iata_to_city('PBC', self.iata_to_city), 'Puebla')
        self.assertEqual(map_iata_to_city('MTY', self.iata_to_city), 'Monterrey')
    
    # Prueba de fallo
        self.assertIsNone(map_iata_to_city('XYZ', self.iata_to_city))

    def test_get_closest_city_name(self):
    # Corrección ortográfica
        self.assertEqual(get_closest_city_name('Ne York', self.valid_cities), 'New York')
        self.assertEqual(get_closest_city_name('Montery', self.valid_cities), 'Monterrey')
        self.assertEqual(get_closest_city_name('Monterye', self.valid_cities), 'Monterrey')
        self.assertEqual(get_closest_city_name('Monterey', self.valid_cities), 'Monterrey')
        self.assertEqual(get_closest_city_name('Londres', self.valid_cities), 'London')
        self.assertEqual(get_closest_city_name('Berlín', self.valid_cities), 'Berlin')
        self.assertEqual(get_closest_city_name('París', self.valid_cities), 'Paris')
        self.assertEqual(get_closest_city_name('Barcelna', self.valid_cities), 'Barcelona')
        self.assertEqual(get_closest_city_name('Tokio', self.valid_cities), 'Tokyo')
        self.assertEqual(get_closest_city_name('Los Ángles', self.valid_cities), 'Los Angeles')
        self.assertEqual(get_closest_city_name('Madris', self.valid_cities), 'Madrid')
        self.assertEqual(get_closest_city_name('Cancún', self.valid_cities), 'Cancun')  # Sin tilde
        self.assertEqual(get_closest_city_name('Guadalajra', self.valid_cities), 'Guadalajara')
        self.assertEqual(get_closest_city_name('Cdmx', self.valid_cities), 'Ciudad de México')
        
    # Caso donde no hay coincidencias
        self.assertEqual(get_closest_city_name('UnknownCity', self.valid_cities), 'UnknownCity')  # Debe regresar el valor original si no hay coincidencias

    def test_hex_to_iata(self):
        for index, row in self.sample_data.iterrows():
            expected_city = row['destination']
            print(f"Expected city is: {expected_city}")
            hex_ticket = row['ticket'].replace(" ", "")
            actual_city = hex_to_iata(hex_ticket, self.iata_to_city)
            print(f"Actual city is: {actual_city}")
            self.assertEqual(actual_city, expected_city, f"Failed for ticket: {hex_ticket}")
        self.assertIsNone(hex_to_iata('4a464', self.iata_to_city))  # Si el ticket no esta completo, debe ser None

if __name__ == '__main__':
    unittest.main()
