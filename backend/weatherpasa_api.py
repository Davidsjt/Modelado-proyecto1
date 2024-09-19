import requests
from datetime import datetime

# API key
api_key = "cc8f7bbf129d916c4b40ad83b402512d"

# Función para obtener el clima dado un nombre de ciudad o un código IATA, especialmente para datos de pasajeros
def obtener_clima_pasajeros(city_or_iata_code):
    
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_or_iata_code + "&lang=es"

    # Realizar la solicitud HTTP a la API
    response = requests.get(complete_url)
    weather_response = response.json()  # Convertir la respuesta en un diccionario JSON

    # Verificar si se encontró la ciudad (código diferente a "404")
    if weather_response["cod"] != "404":
        # Extraer la información principal del clima 
        main_info = weather_response["main"]
        current_temperature_celsius = main_info["temp"] - 273.15  # Convertir la temperatura de Kelvin a Celsius
        feels_like_celsius = main_info["feels_like"] - 273.15  # Sensación térmica
        temp_min_celsius = main_info["temp_min"] - 273.15  # Temperatura mínima
        temp_max_celsius = main_info["temp_max"] - 273.15  # Temperatura máxima
        current_pressure = main_info["pressure"]  # Presión atmosférica
        current_humidity = main_info["humidity"]  # Humedad actual
        
        # Extraer la descripción del clima 
        weather_conditions = weather_response["weather"]
        weather_description = weather_conditions[0]["description"]
        
        # Obtener el código del ícono del clima 
        weather_icon = weather_conditions[0]["icon"]
        icon_url = f"http://openweathermap.org/img/wn/{weather_icon}@4x.png"

        # Extraer la información del viento
        wind_info = weather_response.get("wind", {})
        wind_speed = wind_info.get("speed", "N/A")  # Velocidad del viento
        wind_deg = wind_info.get("deg", "N/A")  # Dirección del viento en grados

        # Extraer la visibilidad (si está disponible)
        visibility = weather_response.get("visibility", "N/A")

        # Extraer la nubosidad (porcentaje de cielo cubierto por nubes)
        cloud_info = weather_response.get("clouds", {})
        cloudiness = cloud_info.get("all", "N/A")

        # Extraer la hora de amanecer y anochecer y convertirlo a formato legible
        sys_info = weather_response.get("sys", {})
        country = sys_info.get("country", "N/A")  # País donde se encuentra la ciudad
        sunrise_unix = sys_info.get("sunrise")
        sunset_unix = sys_info.get("sunset")
        
        if sunrise_unix:
            sunrise_time = datetime.utcfromtimestamp(sunrise_unix).strftime('%H:%M:%S')
        else:
            sunrise_time = "N/A"  # Si no está disponible
        
        if sunset_unix:
            sunset_time = datetime.utcfromtimestamp(sunset_unix).strftime('%H:%M:%S')
        else:
            sunset_time = "N/A"  # Si no está disponible

        # Extraer las coordenadas (longitud y latitud) de la ciudad
        coordinates = weather_response.get("coord", {})
        longitude = coordinates.get("lon", "N/A")
        latitude = coordinates.get("lat", "N/A")

        # Construir un diccionario con todos los datos relevantes del clima
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
            "longitude": longitude,
            "latitude": latitude
        }
    else:
        # Si la ciudad no se encuentra, devolver un mensaje de error
        weather_data_pasajeros = "Ciudad no encontrada"
    
    # Devolver los datos del clima o el mensaje de error
    return weather_data_pasajeros