import unittest
from unittest.mock import patch
from datetime import datetime, timezone
from backend.weatherpasa_api import obtener_clima_pasajeros

class TestObtenerClimaPasajeros(unittest.TestCase):

    @patch('backend.weatherpasa_api.requests.get')
    def test_obtener_clima_pasajeros_success(self, mock_get):
        # Simular una respuesta exitosa de la API
        mock_response = {
            "cod": 200,
            "main": {
                "temp": 300.15,  # En Kelvin
                "feels_like": 298.15,
                "temp_min": 295.15,
                "temp_max": 305.15,
                "pressure": 1013,
                "humidity": 75
            },
            "weather": [{
                "description": "cielo claro",
                "icon": "01d"
            }],
            "wind": {
                "speed": 5.14,
                "deg": 200
            },
            "visibility": 10000,
            "clouds": {
                "all": 0
            },
            "sys": {
                "country": "MX",
                "sunrise": 1624356789,
                "sunset": 1624401234
            },
            "coord": {
                "lon": -99.1332,
                "lat": 19.4326
            },
            "rain": {
                "3h": 0.0
            }
        }
        
        mock_get.return_value.json.return_value = mock_response

        expected_data = {
            "temperature": "27.00°C",
            "feels_like": "25.00°C",
            "temp_min": "22.00°C",
            "temp_max": "32.00°C",
            "pressure": "1013 hPa",
            "humidity": "75%",
            "description": "Cielo claro",
            "icon_url": "http://openweathermap.org/img/wn/01d@4x.png",
            "wind_speed": "5.14 m/s",
            "wind_deg": "200°",
            "visibility": "10000 m",
            "cloudiness": "0%",
            "sunrise": datetime.fromtimestamp(1624356789, timezone.utc).strftime('%H:%M:%S'),
            "sunset": datetime.fromtimestamp(1624401234, timezone.utc).strftime('%H:%M:%S'),
            "country": "MX",
            "longitude": -99.1332,
            "latitude": 19.4326,
            "rain_3h": "No hay lluvia"
        }

        result = obtener_clima_pasajeros("Mexico City")
        self.assertEqual(result, expected_data)

    @patch('backend.weatherpasa_api.requests.get')
    def test_obtener_clima_pasajeros_not_found(self, mock_get):
        # Simular una respuesta de ciudad no encontrada
        mock_response = {
            "cod": "404",
            "message": "city not found"
        }
        
        mock_get.return_value.json.return_value = mock_response

        result = obtener_clima_pasajeros("XYZ")
        self.assertEqual(result, "Ciudad no encontrada")

    @patch('backend.weatherpasa_api.requests.get')
    def test_obtener_clima_pasajeros_incomplete_data(self, mock_get):
        # Simular una respuesta con datos incompletos
        mock_response = {
            "cod": 200,
            "main": {
                "temp": 300.15,
                "pressure": 1013
            },
            "sys": {
                "country": "MX",
                "sunrise": 1624356789,
                "sunset": 1624401234
            }
        }
        
        mock_get.return_value.json.return_value = mock_response

        expected_data = {
            "temperature": "27.00°C",
            "feels_like": "N/A°C",  # Faltan datos
            "temp_min": "N/A°C",
            "temp_max": "N/A°C",
            "pressure": "1013 hPa",
            "humidity": "N/A%",
            "description": "N/A",
            "icon_url": "N/A",
            "wind_speed": "N/A m/s",
            "wind_deg": "N/A°",
            "visibility": "N/A",
            "cloudiness": "N/A%",
            "sunrise": datetime.fromtimestamp(1624356789, timezone.utc).strftime('%H:%M:%S'),
            "sunset": datetime.fromtimestamp(1624401234, timezone.utc).strftime('%H:%M:%S'),
            "country": "MX",
            "longitude": "N/A",
            "latitude": "N/A",
            "rain_3h": "No hay lluvia"
        }

        result = obtener_clima_pasajeros("Mexico City")
        self.assertEqual(result, expected_data)

if __name__ == '__main__':
    unittest.main()
