from flask import Flask, request, render_template, redirect, url_for
from backend.city_data_utils import load_iata_data, map_iata_to_city, get_closest_city_name, hex_to_iata
from backend.weather_api import obtener_clima
from backend.weatherpasa_api import obtener_clima_pasajeros
import re  # Importamos re para validar el input

app = Flask(__name__)

iata_to_city, valid_cities = load_iata_data('static/iata_cities.csv')

# Función que valida si el input contiene solo letras
def is_valid_city_name(city_name):
    return re.match("^[A-Za-záéíóúÁÉÍÓÚ\s]+$", city_name)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/tripulacion')
def tripulacion():
    return render_template('tripulacion.html')

@app.route('/pasajeros')
def pasajeros():
    return render_template('pasajero.html')

def validar_city_name(city_name):
    # Verificar si la entrada es numérica
    if city_name.isdigit():
        # Redirigir a la página de error si la entrada es solo números
        return redirect(url_for('error', city_name=city_name, context='tripulacion'))
    
    # Verificar si la longitud excede los 15 caracteres
    if len(city_name) > 15:
        # Redirigir a la página de error si la entrada es demasiado larga
        return redirect(url_for('error', city_name=city_name, context='tripulacion'))
    
    return None

@app.route('/tripulacion/clima', methods=['GET'])
def climat():
    city_name = request.args.get('city_name')

    if not city_name:
        return render_template('clima.html', weather_data=None, city_name=None)

    # Validar la entrada
    error = validar_city_name(city_name)
    if error:
        return error  # Si es un error, redirigir a la plantilla de error

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

    # Si no hay datos de clima o la ciudad no es encontrada, redirigir a la página de error
    if not weather_data or weather_data == "Ciudad no encontrada":
        return redirect(url_for('error', city_name=city_name, context='tripulacion'))

    return render_template('clima.html', weather_data=weather_data, city_name=city_name)

@app.route('/pasajeros/climapa', methods=['GET'])
def climap():
    city_name = request.args.get('city_name')

    if not city_name:
        return render_template('climapa.html', weather_data_pasajeros=None, city_name=None)

    # Validar la entrada
    error = validar_city_name(city_name)
    if error:
        return error  # Si es un error, redirigir a la plantilla de error

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

    # Si no hay datos de clima o la ciudad no es encontrada, redirigir a la página de error
    if not weather_data_pasajeros or weather_data_pasajeros == "Ciudad no encontrada":
        return redirect(url_for('error', city_name=city_name, context='pasajeros'))

    return render_template('climapa.html', weather_data_pasajeros=weather_data_pasajeros, city_name=city_name)

# Ruta para la página de error
@app.route('/error')
def error():
    city_name = request.args.get('city_name')
    context = request.args.get('context', 'tripulacion')  # Si no se pasa context, por defecto será 'tripulacion'
    return render_template('error.html', city_name=city_name, context=context)

if __name__ == '__main__':
    app.run(debug=True)



