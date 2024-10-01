import unittest
from unittest.mock import patch
from backend.weather_api import obtener_clima  

class TestObtenerClima(unittest.TestCase):
    @patch('requests.get')
    def test_obtener_clima_exito(self, mock_get):
        # Simular la respuesta de la API para una ciudad válida
        mock_response = {
            "cod": 200,
            "main": {
                "temp": 293.15,
                "feels_like": 295.15,
                "temp_min": 292.15,
                "temp_max": 294.15,
                "pressure": 1012,
                "humidity": 80
            },
            "weather": [{
                "description": "cielo claro",
                "icon": "01d"
            }],
            "wind": {
                "speed": 5,
                "deg": 180
            },
            "visibility": 10000,
            "clouds": {
                "all": 0
            },
            "rain": {},
            "sys": {
                "country": "ES",
                "sunrise": 1635300000,
                "sunset": 1635343200
            },
            "coord": {
                "lon": -3.7038,
                "lat": 40.4168
            }
        }
        mock_get.return_value.json.return_value = mock_response

        # Llamar a la función con un nombre de ciudad
        resultado = obtener_clima("Madrid")

        # Verificar el formato de los datos devueltos
        self.assertIn("temperature", resultado)
        self.assertEqual(resultado["temperature"], "20.00°C")  # 293.15K -> 20°C
        self.assertEqual(resultado["country"], "ES")
        self.assertEqual(resultado["description"], "Cielo claro")

    @patch('requests.get')
    def test_obtener_clima_ciudad_no_encontrada(self, mock_get):
        # Simular una respuesta de ciudad no encontrada
        mock_response = {
            "cod": "404",
            "message": "city not found"
        }
        mock_get.return_value.json.return_value = mock_response

        # Llamar a la función con un nombre de ciudad inválido
        resultado = obtener_clima("CiudadInexistente")

        # Verificar que el resultado sea el esperado
        self.assertEqual(resultado, "Ciudad no encontrada")

    def test_obtener_clima_nulo(self):
        # Llamar a la función con un valor nulo
        resultado = obtener_clima(None)

        # Verificar que el resultado sea el esperado
        self.assertEqual(resultado, "Ciudad no encontrada")

if __name__ == '__main__':
    unittest.main()
