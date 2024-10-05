import os
import requests
from dotenv import load_dotenv
from datetime import datetime
from backend.cache import get_from_cache, set_to_cache  # Importar funciones del módulo cache

# Cargar las variables de entorno
load_dotenv()
api_key = os.getenv('OPENWEATHER_API_KEY')  # Clave API de OpenWeather

# Función para obtener el clima dado un nombre de ciudad o un código IATA (para pasajeros)
def obtener_clima_pasajeros(city_or_iata_code):
    if city_or_iata_code is None:
        return "Ciudad no encontrada"
   
 # Verificar si la ciudad ya está en caché
    cached_data, _ = get_from_cache(city_or_iata_code)
    if cached_data:
        print("Usando datos en caché")
        return cached_data

    # Construir la URL para la solicitud a OpenWeather
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_or_iata_code + "&lang=es"

    response = requests.get(complete_url)
    weather_response = response.json()

    # Verificar si la respuesta contiene datos válidos
    if weather_response.get("cod") != "404" and "main" in weather_response:
        main_weather_data = weather_response["main"]

        # Convertir las temperaturas de Kelvin a Celsius
        current_temperature_celsius = main_weather_data["temp"] - 273.15
        feels_like_celsius = main_weather_data["feels_like"] - 273.15
        temp_min_celsius = main_weather_data["temp_min"] - 273.15
        temp_max_celsius = main_weather_data["temp_max"] - 273.15

        current_pressure = main_weather_data["pressure"]
        current_humidity = main_weather_data["humidity"]

        # Obtener descripción del clima y el ícono
        weather_description = weather_response["weather"][0]["description"] if "weather" in weather_response else "N/A"
        weather_icon = weather_response["weather"][0]["icon"] if "weather" in weather_response else "N/A"
        icon_url = f"http://openweathermap.org/img/wn/{weather_icon}@4x.png" if weather_icon != "N/A" else "N/A"

        # Obtener datos adicionales (viento, visibilidad, nubosidad)
        wind = weather_response.get("wind", {})
        wind_speed = wind.get("speed", "N/A")
        wind_deg = wind.get("deg", "N/A")
        visibility = weather_response.get("visibility", "N/A")
        clouds = weather_response.get("clouds", {})
        cloudiness = clouds.get("all", "N/A")

        # Obtener hora de amanecer y anochecer si están disponibles
        sys = weather_response.get("sys", {})
        country = sys.get("country", "N/A")
        sunrise_unix = sys.get("sunrise")
        sunset_unix = sys.get("sunset")
        sunrise_time = datetime.utcfromtimestamp(sunrise_unix).strftime('%H:%M:%S') if sunrise_unix else "N/A"
        sunset_time = datetime.utcfromtimestamp(sunset_unix).strftime('%H:%M:%S') if sunset_unix else "N/A"

        # Obtener coordenadas geográficas si están presentes
        coord = weather_response.get("coord", {})
        lon = coord.get("lon", "N/A")
        lat = coord.get("lat", "N/A")

        # Obtener datos de lluvia si están disponibles
        rain = weather_response.get("rain", {})
        rain_1h = rain.get("1h", 0)  # Lluvia en las últimas 3 horas

        # Estructurar los datos del clima
        weather_data_pasajeros = {
            "temperature": f"{current_temperature_celsius:.2f}°C",
            "feels_like": f"{feels_like_celsius:.2f}°C",
            "temp_min": f"{temp_min_celsius:.2f}°C",
            "temp_max": f"{temp_max_celsius:.2f}°C",
            "pressure": f"{current_pressure} hPa",
            "humidity": f"{current_humidity}%",
            "description": weather_description.capitalize(),
            "icon_url": icon_url,  # URL del ícono del clima
            "wind_speed": f"{wind_speed} m/s",
            "wind_deg": f"{wind_deg}°",
            "visibility": f"{visibility} m" if visibility != "N/A" else "N/A",
            "cloudiness": f"{cloudiness}%",
            "sunrise": sunrise_time,
            "sunset": sunset_time,
            "country": country,
            "longitude": lon,
            "latitude": lat,
            "rain_1h": f"{rain_1h} mm" if rain_1h != 0 else "No hay lluvia"
        }
    else:
        # Retornar mensaje de error si no se encuentran los datos
        weather_data_pasajeros = "Ciudad no encontrada"

     # Almacenar los datos en el caché compartido
    set_to_cache(city_or_iata_code, weather_data_pasajeros)
    return weather_data_pasajeros