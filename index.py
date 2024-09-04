from flask import Flask, request, render_template
from backend.weather_api import obtener_clima
from backend.data_api import query_wikidata

app = Flask(__name__)

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

    # Obtener el clima usando el nombre de la ciudad
    weather_data = obtener_clima(city_name)
    
    # Obtener los datos de Wikidata utilizando el nombre de la ciudad
    wikidata_results = query_wikidata(city_name)

    # Procesar los resultados de Wikidata
    curiosities = []
    if wikidata_results and 'results' in wikidata_results and wikidata_results['results']['bindings']:
        for result in wikidata_results['results']['bindings']:
            curiosity = result.get('curiosityLabel', {}).get('value', None)
            curiosity_desc = result.get('curiosityDescription', {}).get('value', 'No hay descripción disponible.')
            if curiosity:
                curiosities.append(f"{curiosity}: {curiosity_desc}")

    print(f"Weather Data: {weather_data}")
    print(f"Curiosities: {curiosities}")

    return render_template('clima.html', weather_data=weather_data, city_name=city_name, wikidata_results=curiosities)

@app.route('/pasajeros/clima', methods=['GET'])
def climap():
    city_name = request.args.get('city_name')

    print(f"Received city_name: {city_name}")

    if not city_name:
        return render_template('climapa.html', weather_data=None, city_name=None)

    # Obtener el clima usando el nombre de la ciudad
    weather_data = obtener_clima(city_name)
    
    print(f"Weather Data: {weather_data}")

    return render_template('climapa.html', weather_data=weather_data, city_name=city_name)

if __name__ == '__main__':
    app.run(debug=True)

