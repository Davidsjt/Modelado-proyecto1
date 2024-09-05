# weatherpasa_api.py
import requests
from datetime import datetime

# Tu clave de API de OpenWeather
api_key = "cc8f7bbf129d916c4b40ad83b402512d"

def obtener_clima_pasajero(iata_code):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + iata_code + "&lang=es"

    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]
        temperatura_actual_celsius = y["temp"] - 273.15
        sensacion_termica_celsius = y["feels_like"] - 273.15
        temp_min_celsius = y["temp_min"] - 273.15
        temp_max_celsius = y["temp_max"] - 273.15
        presion_actual = y["pressure"]
        humedad_actual = y["humidity"]
        
        z = x["weather"]
        descripcion_clima = z[0]["description"]

        # Obtener datos del viento
        viento = x.get("wind", {})
        velocidad_viento = viento.get("speed", "N/A")
        direccion_viento = viento.get("deg", "N/A")

        # Obtener visibilidad
        visibilidad = x.get("visibility", "N/A")

        # Obtener nubosidad
        nubes = x.get("clouds", {})
        nubosidad = nubes.get("all", "N/A")

        # Obtener hora de amanecer y anochecer
        sys = x.get("sys", {})
        pais = sys.get("country", "N/A")
        amanecer_unix = sys.get("sunrise")
        atardecer_unix = sys.get("sunset")
        if amanecer_unix:
            hora_amanecer = datetime.utcfromtimestamp(amanecer_unix).strftime('%H:%M:%S')
        else:
            hora_amanecer = "N/A"
        if atardecer_unix:
            hora_atardecer = datetime.utcfromtimestamp(atardecer_unix).strftime('%H:%M:%S')
        else:
            hora_atardecer = "N/A"

        # Opcional: Obtener coordenadas
        coordenadas = x.get("coord", {})
        longitud = coordenadas.get("lon", "N/A")
        latitud = coordenadas.get("lat", "N/A")

        weather_data_pasajero = {
            "temperatura": f"{temperatura_actual_celsius:.2f}°C",
            "sensacion_termica": f"{sensacion_termica_celsius:.2f}°C",
            "temp_min": f"{temp_min_celsius:.2f}°C",
            "temp_max": f"{temp_max_celsius:.2f}°C",
            "presion": f"{presion_actual} hPa",
            "humedad": f"{humedad_actual}%",
            "descripcion": descripcion_clima.capitalize(),
            "velocidad_viento": f"{velocidad_viento} m/s",
            "direccion_viento": f"{direccion_viento}°",
            "visibilidad": f"{visibilidad} m" if visibilidad != "N/A" else "N/A",
            "nubosidad": f"{nubosidad}%",
            "amanecer": hora_amanecer,
            "atardecer": hora_atardecer,
            "pais": pais,
            "longitud": longitud,
            "latitud": latitud
        }
    else:
        weather_data_pasajero = "Ciudad no encontrada"
    
    return weather_data_pasajero



