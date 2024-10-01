import os
import unittest
from unittest.mock import patch
from backend.weatherpasa_api import obtener_clima_pasajeros

class TestObtenerClimaPasajeros(unittest.TestCase):

    @patch("backend.weather.requests.get")  # Simulamos requests.get
    def test_obtener_clima_con_ciudad_valida(self, mock_get):
        # Simulamos la respuesta de la API para una ciudad válida
        mock_response = {
            "cod": 200,
            "main": {
                "temp": 293.15,
                "feels_like": 295.15,
                "temp_min": 290.15,
                "temp_max": 295.15,
                "pressure": 1013,
                "humidity": 80,
            },
            "weather": [
                {
                    "description": "cielo claro",
                    "icon": "01d"
                }
            ],
            "wind": {
                "speed": 3.1,
                "deg": 200
            },
            "visibility": 10000,
            "clouds": {
                "all": 1
            },
            "sys": {
                "country": "ES",
                "sunrise": 1601000000,
                "sunset": 1601040000
            },
            "coord": {
                "lon": -3.7038,
                "lat": 40.4168
            },
            "rain": {
                "3h": 0
            }
        }

        mock_get.return_value.json.return_value = mock_response

        resultado = obtener_clima_pasajeros("Madrid")  # Llama a la función con un nombre de ciudad

        # Verificamos que el resultado sea correcto
        self.assertEqual(resultado["temperature"], "20.00°C")  # Temperatura en Celsius
        self.assertEqual(resultado["description"], "Cielo claro")  # Descripción del clima
        self.assertEqual(resultado["country"], "ES")  # País

    @patch("backend.weather.requests.get")
    def test_obtener_clima_con_ciudad_no_encontrada(self, mock_get):
        # Simulamos la respuesta de la API para una ciudad no encontrada
        mock_response = {
            "cod": "404",
            "message": "city not found"
        }
        mock_get.return_value.json.return_value = mock_response

        resultado = obtener_clima_pasajeros("CiudadInexistente")  # Llama a la función con un nombre de ciudad no válida

        # Verificamos que el resultado sea el mensaje de error
        self.assertEqual(resultado, "Ciudad no encontrada")

    @patch("backend.weather.requests.get")
    def test_obtener_clima_con_codigo_nulo(self, mock_get):
        resultado = obtener_clima_pasajeros(None)  # Llama a la función con un código nulo

        # Verificamos que el resultado sea el mensaje de error
        self.assertEqual(resultado, "Ciudad no encontrada")

if __name__ == '__main__':
    unittest.main()
