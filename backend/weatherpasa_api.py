import requests
from datetime import datetime

# Tu clave de API de OpenWeather
api_key = "cc8f7bbf129d916c4b40ad83b402512d"

# Función para obtener el clima dado un nombre de ciudad o un código IATA
def obtener_clima_pasajeros(city_or_iata_code):
    # Verificar que el valor de city_or_iata_code no sea None
    if city_or_iata_code is None:
        return "Ciudad no encontrada"

    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_or_iata_code + "&lang=es"

    response = requests.get(complete_url)
    weather_response = response.json()  # Renombrado de 'x' a 'weather_response'

    # Verificar si el código de respuesta es válido y contiene las claves necesarias
    if weather_response.get("cod") != "404" and "main" in weather_response:
        main_weather_data = weather_response["main"]  # Renombrado de 'y' a 'main_weather_data'
        
        current_temperature_celsius = main_weather_data["temp"] - 273.15
        feels_like_celsius = main_weather_data["feels_like"] - 273.15
        temp_min_celsius = main_weather_data["temp_min"] - 273.15
        temp_max_celsius = main_weather_data["temp_max"] - 273.15
        current_pressure = main_weather_data["pressure"]
        current_humidity = main_weather_data["humidity"]

        # Verificar si "weather" está presente antes de acceder a su contenido
        weather_description = weather_response["weather"][0]["description"] if "weather" in weather_response else "N/A"

        # Obtener el ícono del clima si está disponible
        weather_icon = weather_response["weather"][0]["icon"] if "weather" in weather_response else "N/A"
        icon_url = f"http://openweathermap.org/img/wn/{weather_icon}@4x.png" if weather_icon != "N/A" else "N/A"

        # Obtener datos del viento, visibilidad, y nubosidad
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

        # Obtener coordenadas si están disponibles
        coord = weather_response.get("coord", {})
        lon = coord.get("lon", "N/A")
        lat = coord.get("lat", "N/A")

        weather_data_pasajeros = {
            "temperature": f"{current_temperature_celsius:.2f}°C",
            "feels_like": f"{feels_like_celsius:.2f}°C",
            "temp_min": f"{temp_min_celsius:.2f}°C",
            "temp_max": f"{temp_max_celsius:.2f}°C",
            "pressure": f"{current_pressure} hPa",
            "humidity": f"{current_humidity}%",
            "description": weather_description.capitalize(),
            "icon_url": icon_url,  # Añadimos la URL del ícono
            "wind_speed": f"{wind_speed} m/s",
            "wind_deg": f"{wind_deg}°",
            "visibility": f"{visibility} m" if visibility != "N/A" else "N/A",
            "cloudiness": f"{cloudiness}%",
            "sunrise": sunrise_time,
            "sunset": sunset_time,
            "country": country,
            "longitude": lon,
            "latitude": lat
        }
    else:
        weather_data_pasajeros = "Ciudad no encontrada"

    return weather_data_pasajeros

