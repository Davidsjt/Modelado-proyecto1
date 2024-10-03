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
    # Mapeo IATA para ciudades de México
        self.assertEqual(map_iata_to_city('MEX', self.iata_to_city), 'Ciudad de Mexico')  # Ciudad de México (CDMX)
        self.assertEqual(map_iata_to_city('OAX', self.iata_to_city), 'Oaxaca')  # Oaxaca
        self.assertEqual(map_iata_to_city('GDL', self.iata_to_city), 'Guadalajara')  # Guadalajara
        self.assertEqual(map_iata_to_city('MTY', self.iata_to_city), 'Monterrey')  # Monterrey
        self.assertEqual(map_iata_to_city('CUN', self.iata_to_city), 'Cancun')  # Cancún
        self.assertEqual(map_iata_to_city('PVR', self.iata_to_city), 'Puerto Vallarta')  # Puerto Vallarta

        self.assertEqual(map_iata_to_city('TIJ', self.iata_to_city), 'Tijuana')  # Tijuana
        self.assertEqual(map_iata_to_city('VER', self.iata_to_city), 'Veracruz')  # Veracruz
        self.assertEqual(map_iata_to_city('MID', self.iata_to_city), 'Merida')  # Mérida
        self.assertEqual(map_iata_to_city('ZIH', self.iata_to_city), 'Ixtapa-Zihuatanejo')  # Ixtapa-Zihuatanejo
        self.assertEqual(map_iata_to_city('QRO', self.iata_to_city), 'Querétaro')  # Querétaro
        self.assertEqual(map_iata_to_city('CUU', self.iata_to_city), 'Chihuahua')  # Chihuahua
        self.assertEqual(map_iata_to_city('CUL', self.iata_to_city), 'Culiacán')  # Culiacán
        self.assertEqual(map_iata_to_city('HMO', self.iata_to_city), 'Hermosillo')  # Hermosillo
        self.assertEqual(map_iata_to_city('SLP', self.iata_to_city), 'San Luis Potosí')  # San Luis Potosí
        self.assertEqual(map_iata_to_city('LAP', self.iata_to_city), 'La Paz')  # La Paz
        self.assertEqual(map_iata_to_city('REX', self.iata_to_city), 'Reynosa')  # Reynosa
        self.assertEqual(map_iata_to_city('TLC', self.iata_to_city), 'Toluca')  # Toluca
    # Prueba de fallo para código IATA no válido
        self.assertIsNone(map_iata_to_city('XYZ', self.iata_to_city))  # Código IATA desconocido


    def test_get_closest_city_name(self):
    # Corrección ortográfica para ciudades internacionales
        self.assertEqual(get_closest_city_name('Ne York', self.valid_cities), 'New York')  # Error común: falta de "w"
        self.assertEqual(get_closest_city_name('Lodon', self.valid_cities), 'London')  # Error común: inversión de letras
        self.assertEqual(get_closest_city_name('Tokyo', self.valid_cities), 'Tokyo')  # Error común: uso del nombre en español
        self.assertEqual(get_closest_city_name('Sidny', self.valid_cities), 'Sydney')  # Error común: uso de "i" en lugar de "y"
    
    # Corrección ortográfica para ciudades de México
        self.assertEqual(get_closest_city_name('Guadaljara', self.valid_cities), 'Guadalajara')  # Error común: falta de "a"
        self.assertEqual(get_closest_city_name('Montery', self.valid_cities), 'Monterrey') # Error común: falta de "r"
        self.assertEqual(get_closest_city_name('Monterye', self.valid_cities), 'Monterrey')
        self.assertEqual(get_closest_city_name('Monterey', self.valid_cities), 'Monterrey')       
        self.assertEqual(get_closest_city_name('Puepla', self.valid_cities), 'Puebla')  # Error común: inversión de letras

    # Si la ciudad no se encuentra en la lista válida, debe regresar el valor original
        self.assertEqual(get_closest_city_name('UnknownCity', self.valid_cities), 'UnknownCity')


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
