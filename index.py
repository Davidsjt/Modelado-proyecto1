from flask import Flask, request, render_template
from backend.city_data_utils import load_iata_data, map_iata_to_city, get_closest_city_name, hex_to_iata
from backend.weather_api import obtener_clima
from backend.weatherpasa_api import obtener_clima_pasajeros

app = Flask(__name__)

iata_to_city, valid_cities = load_iata_data('static/iata_cities.csv')

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
    city_name = request.args.get('city_name')

    if not city_name:
        return render_template('clima.html', weather_data=None, city_name=None)

    hex_city_iata = hex_to_iata(city_name, iata_to_city)
    if hex_city_iata:
        city_name = map_iata_to_city(hex_city_iata, iata_to_city)
    else:
        mapped_city = map_iata_to_city(city_name, iata_to_city)
        if mapped_city:
            city_name = mapped_city
        else:
            city_name = get_closest_city_name(city_name, valid_cities)

    weather_data = obtener_clima(city_name)

    # Redirigir a la página de error si no se encuentra la ciudad
    if weather_data == "Ciudad no encontrada":
        return render_template('error.html', city_name=city_name)
    
    return render_template('clima.html', weather_data=weather_data, city_name=city_name)

@app.route('/pasajeros/climapa', methods=['GET'])
def climap():
    city_name = request.args.get('city_name')

    if not city_name:
        return render_template('climapa.html', weather_data_pasajeros=None, city_name=None)

    hex_city_iata = hex_to_iata(city_name, iata_to_city)
    if hex_city_iata:
        city_name = map_iata_to_city(hex_city_iata, iata_to_city)
    else:
        mapped_city = map_iata_to_city(city_name, iata_to_city)
        if mapped_city:
            city_name = mapped_city
        else:
            city_name = get_closest_city_name(city_name, valid_cities)

    weather_data_pasajeros = obtener_clima_pasajeros(city_name)

    # Redirigir a la página de error si no se encuentra la ciudad
    if weather_data_pasajeros == "Ciudad no encontrada":
        return render_template('error.html', city_name=city_name)

    return render_template('climapa.html', weather_data_pasajeros=weather_data_pasajeros, city_name=city_name)

if __name__ == '__main__':
    app.run(debug=True)

