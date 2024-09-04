# weather.py
import requests

# Tu clave de API de OpenWeather
api_key = "cc8f7bbf129d916c4b40ad83b402512d"

def obtener_clima(iata_code):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + iata_code + "&lang=es"

    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]
        current_temperature_celsius = y["temp"] - 273.15
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]

        weather_data = {
            "temperature": f"{current_temperature_celsius:.2f}°C",
            "pressure": f"{current_pressure} hPa",
            "humidity": f"{current_humidity}%",
            "description": weather_description.capitalize()
        }
    else:
        weather_data = "Ciudad no encontrada"
    
    return weather_data

