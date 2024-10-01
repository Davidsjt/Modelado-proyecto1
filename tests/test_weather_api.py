import unittest
from unittest.mock import patch
import requests
from backend.weather_api import obtener_clima  # Asegúrate de que esta sea la ruta correcta a la función

class TestWeatherAPI(unittest.TestCase):

    @patch('backend.weather_api.requests.get')
    def test_obtener_clima_valid_city(self, mock_get):
        # Simulación de una respuesta válida de OpenWeather para la ciudad de "London"
        mock_response = {
            "cod": 200,
            "main": {
                "temp": 293.15,
                "feels_like": 290.15,
                "temp_min": 291.15,
                "temp_max": 295.15,
                "pressure": 1012,
                "humidity": 75
            },
            "weather": [
                {
                    "description": "cielo despejado",
                    "icon": "01d"
                }
            ],
            "wind": {
                "speed": 4.12,
                "deg": 240
            },
            "visibility": 10000,
            "clouds": {"all": 0},
            "sys": {
                "country": "GB",
                "sunrise": 1600413600,
                "sunset": 1600459200
            },
            "coord": {
                "lon": -0.1257,
                "lat": 51.5085
            },
            "rain": {}
        }

        mock_get.return_value.json.return_value = mock_response

        # Llamar a la función con la ciudad "London"
        result = obtener_clima("London")

        # Verificar que los datos retornados sean los esperados
        self.assertEqual(result['temperature'], "20.00°C")
        self.assertEqual(result['feels_like'], "17.00°C")
        self.assertEqual(result['temp_min'], "18.00°C")
        self.assertEqual(result['temp_max'], "22.00°C")
        self.assertEqual(result['pressure'], "1012 hPa")
        self.assertEqual(result['humidity'], "75%")
        self.assertEqual(result['description'], "Cielo despejado")
        self.assertEqual(result['country'], "GB")
        self.assertEqual(result['longitude'], "-0.1257")
        self.assertEqual(result['latitude'], "51.5085")
        self.assertEqual(result['wind_speed'], "4.12 m/s")
        self.assertEqual(result['wind_deg'], "240°")
        self.assertEqual(result['cloudiness'], "0%")
        self.assertEqual(result['rain_3h'], "No hay lluvia")

    @patch('backend.weather_api.requests.get')
    def test_obtener_clima_invalid_city(self, mock_get):
        # Simulación de una respuesta de error de OpenWeather para una ciudad no válida
        mock_response = {"cod": "404", "message": "city not found"}
        mock_get.return_value.json.return_value = mock_response

        # Llamar a la función con una ciudad no válida
        result = obtener_clima("InvalidCity")

        # Verificar que la función retorne el mensaje adecuado
        self.assertEqual(result, "Ciudad no encontrada")

    @patch('backend.weather_api.requests.get')
    def test_obtener_clima_api_key_error(self, mock_get):
        # Simulación de una respuesta de error por falta de API Key
        mock_response = {"cod": "401", "message": "Invalid API key"}
        mock_get.return_value.json.return_value = mock_response

        # Llamar a la función con un nombre de ciudad
        result = obtener_clima("London")

        # Verificar que la función maneje el error adecuadamente
        self.assertEqual(result, "Ciudad no encontrada")

if __name__ == '__main__':
    unittest.main()
