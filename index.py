from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# Tu clave de API de OpenWeather
api_key = "cc8f7bbf129d916c4b40ad83b402512d"

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/tripulacion')
def tripulacion():
    return render_template('tripulacion.html')

@app.route('/pasajeros')
def pasajeros():
    return render_template('pasajero.html')

@app.route('/tripulacion/clima', methods=['GET'])
def climat():
    iata_code = request.args.get('iata_code')
    weather_data = None
    if iata_code:
        # Aquí se realiza la solicitud a la API de OpenWeather con el código IATA como nombre de ciudad
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

    return render_template('clima.html', weather_data=weather_data, iata_code=iata_code)

@app.route('/pasajeros/clima', methods=['GET'])
def climap():
    iata_code = request.args.get('iata_code')
    weather_data = None
    if iata_code:
        # Similar lógica para la ruta de pasajeros
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

    return render_template('climapa.html', weather_data=weather_data, iata_code=iata_code)

if __name__ == '__main__':
    app.run(debug=True)


