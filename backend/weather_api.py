# weather.py
import requests
from datetime import datetime

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
        feels_like_celsius = y["feels_like"] - 273.15
        temp_min_celsius = y["temp_min"] - 273.15
        temp_max_celsius = y["temp_max"] - 273.15
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]
        
        z = x["weather"]
        weather_description = z[0]["description"]

        # Obtener datos del viento
        wind = x.get("wind", {})
        wind_speed = wind.get("speed", "N/A")
        wind_deg = wind.get("deg", "N/A")

        # Obtener visibilidad
        visibility = x.get("visibility", "N/A")

        # Obtener nubosidad
        clouds = x.get("clouds", {})
        cloudiness = clouds.get("all", "N/A")

        # Obtener hora de amanecer y anochecer
        sys = x.get("sys", {})
        country = sys.get("country", "N/A")
        sunrise_unix = sys.get("sunrise")
        sunset_unix = sys.get("sunset")
        if sunrise_unix:
            sunrise_time = datetime.utcfromtimestamp(sunrise_unix).strftime('%H:%M:%S')
        else:
            sunrise_time = "N/A"
        if sunset_unix:
            sunset_time = datetime.utcfromtimestamp(sunset_unix).strftime('%H:%M:%S')
        else:
            sunset_time = "N/A"

        # Opcional: Obtener coordenadas
        coord = x.get("coord", {})
        lon = coord.get("lon", "N/A")
        lat = coord.get("lat", "N/A")

        weather_data = {
            "temperature": f"{current_temperature_celsius:.2f}°C",
            "feels_like": f"{feels_like_celsius:.2f}°C",
            "temp_min": f"{temp_min_celsius:.2f}°C",
            "temp_max": f"{temp_max_celsius:.2f}°C",
            "pressure": f"{current_pressure} hPa",
            "humidity": f"{current_humidity}%",
            "description": weather_description.capitalize(),
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
        weather_data = "Ciudad no encontrada"
    
    return weather_data


