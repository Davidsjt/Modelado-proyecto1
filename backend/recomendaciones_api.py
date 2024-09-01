import requests

def obtener_clima(ciudad, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"
    
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Esto lanza una excepción si la respuesta contiene un error HTTP
        datos = respuesta.json()
        
        # Extrae la información relevante del JSON de la respuesta
        clima = {
            "temperatura": datos["main"]["temp"],
            "descripcion": datos["weather"][0]["description"],
            "humedad": datos["main"]["humidity"],
            "viento": datos["wind"]["speed"],
            "ciudad": datos["name"],
            "pais": datos["sys"]["country"]
        }
        
        return clima
    
    except requests.exceptions.HTTPError as err:
        return {"error": f"Error al obtener el clima: {err}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Error de conexión: {e}"}

if __name__ == "__main__":
    ciudad = input("Introduce el nombre de la ciudad: ")
    api_key = 'a12e604bb78a1a62b9fcdfa09b0b84b7'  # Reemplaza con tu API Key de OpenWeather
    clima = obtener_clima(ciudad, api_key)
    
    if "error" in clima:
        print(clima["error"])
    else:
        print(f"Clima en {clima['ciudad']}, {clima['pais']}:")
        print(f"Temperatura: {clima['temperatura']}°C")
        print(f"Descripción: {clima['descripcion']}")
        print(f"Humedad: {clima['humedad']}%")
        print(f"Viento: {clima['viento']} m/s")

