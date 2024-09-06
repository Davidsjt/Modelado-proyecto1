from flask import Flask, request, render_template
from backend.city_data_utils import load_iata_data, map_iata_to_city, get_closest_city_name, hex_to_iata
from backend.weather_api import obtener_clima
from backend.data_api import query_wikidata
from backend.weatherpasa_api import obtener_clima_pasajeros
from backend.datapasa_api import query_wikidata_pasajeros

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

    print(f"Received city_name: {city_name}")

    if not city_name:
        return render_template('clima.html', weather_data=None, city_name=None, wikidata_results=None)

    hex_city_iata = hex_to_iata(city_name, iata_to_city)
    if hex_city_iata:
        city_name = map_iata_to_city(hex_city_iata, iata_to_city)

    else:
        mapped_city = map_iata_to_city(city_name, iata_to_city)
        if mapped_city:
            city_name = mapped_city
        else:
            city_name = get_closest_city_name(city_name, valid_cities)            

    # Obtener el clima usando el nombre de la ciudad
    weather_data = obtener_clima(city_name)
    
    # Obtener los datos de Wikidata utilizando el nombre de la ciudad
    wikidata_results = query_wikidata(city_name)

    print(f"Wikidata Results: {wikidata_results}")
    print(f"Weather Data: {weather_data}")

    # Renderizar la plantilla con los datos obtenidos
    return render_template('clima.html', weather_data=weather_data, city_name=city_name, wikidata_results=wikidata_results)



    # Renderizar la plantilla con los datos obtenidos
    return render_template('clima.html', weather_data=weather_data, city_name=city_name, curiosities=curiosities)



    
@app.route('/pasajeros/climapa', methods=['GET'])
def climap():
    city_name = request.args.get('city_name')

    print(f"Received city_name: {city_name}")

    if not city_name:
        return render_template('climapa.html', weather_data_pasajeros=None, city_name=None, wikidata_results_pasajeros=None)

    # Obtener el clima usando el nombre de la ciudad
    weather_data_pasajeros = obtener_clima_pasajeros(city_name)
    
    # Obtener los datos de Wikidata utilizando el nombre de la ciudad
    wikidata_results_pasajeros = query_wikidata_pasajeros(city_name)

    print(f"Wikidata Results: {wikidata_results_pasajeros}")
    print(f"Weather Data: {weather_data_pasajeros}")

    # Renderizar la plantilla con los datos obtenidos
    return render_template('climapa.html', weather_data_pasajeros=weather_data_pasajeros, city_name=city_name, wikidata_results_pasajeros=wikidata_results_pasajeros)



    # Renderizar la plantilla con los datos obtenidos
    return render_template('climapa.html', weather_data_pasajeros=weather_data_pasajeros, city_name=city_name, curiosities_pasajeros=curiosities_pasajeros)

if __name__ == '__main__':
    app.run(debug=True)
