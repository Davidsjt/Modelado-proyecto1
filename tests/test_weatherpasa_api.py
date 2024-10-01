import unittest
from unittest.mock import patch
from backend.weatherpasa_api import obtener_clima_pasajeros

class TestWeatherAPI(unittest.TestCase):

    @patch('backend.weatherpasa_api.requests.get')
    def test_obtener_clima_pasajeros_exitoso(self, mock_get):
        # Simular una respuesta exitosa de la API de OpenWeather
        mock_response = {
            "cod": 200,
            "main": {
                "temp": 293.15,
                "feels_like": 290.15,
                "temp_min": 290.15,
                "temp_max": 295.15,
                "pressure": 1013,
                "humidity": 78
            },
            "weather": [
                {
                    "description": "cielo claro",
                    "icon": "01d"
                }
            ],
            "wind": {
                "speed": 3.09,
                "deg": 150
            },
            "visibility": 10000,
            "clouds": {
                "all": 0
            },
            "sys": {
                "country": "MX",
                "sunrise": 1633072800,
                "sunset": 1633116000
            },
            "coord": {
                "lon": -99.13,
                "lat": 19.43
            },
            "rain": {
                "3h": 0
            }
        }

        # Configurar el mock para devolver la respuesta simulada
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        # Llamar a la función y verificar los datos
        resultado = obtener_clima_pasajeros("Ciudad de México")
        self.assertEqual(resultado["temperature"], "20.00°C")
        self.assertEqual(resultado["feels_like"], "17.00°C")
        self.assertEqual(resultado["temp_min"], "17.00°C")
        self.assertEqual(resultado["temp_max"], "22.00°C")
        self.assertEqual(resultado["pressure"], "1013 hPa")
        self.assertEqual(resultado["humidity"], "78%")
        self.assertEqual(resultado["description"], "Cielo claro")
        self.assertEqual(resultado["icon_url"], "http://openweathermap.org/img/wn/01d@4x.png")
        self.assertEqual(resultado["wind_speed"], "3.09 m/s")
        self.assertEqual(resultado["wind_deg"], "150°")
        self.assertEqual(resultado["visibility"], "10000 m")
        self.assertEqual(resultado["cloudiness"], "0%")
        self.assertEqual(resultado["sunrise"], "12:00:00")
        self.assertEqual(resultado["sunset"], "00:00:00")
        self.assertEqual(resultado["country"], "MX")
        self.assertEqual(resultado["longitude"], -99.13)
        self.assertEqual(resultado["latitude"], 19.43)
        self.assertEqual(resultado["rain_3h"], "No hay lluvia")

    @patch('backend.weatherpasa_api.requests.get')
    def test_obtener_clima_pasajeros_ciudad_no_encontrada(self, mock_get):
        # Simular una respuesta de error (ciudad no encontrada)
        mock_response = {
            "cod": "404",
            "message": "city not found"
        }

        # Configurar el mock para devolver la respuesta simulada
        mock_get.return_value.status_code = 404
        mock_get.return_value.json.return_value = mock_response

        # Llamar a la función y verificar el resultado de error
        resultado = obtener_clima_pasajeros("CiudadDesconocida")
        self.assertEqual(resultado, "Ciudad no encontrada")

if __name__ == '__main__':
    unittest.main()

