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

    print(f"Wikidata Results: {wikidata_results}")
    print(f"Weather Data: {weather_data}")

    # Renderizar la plantilla con los datos obtenidos
    return render_template('clima.html', weather_data=weather_data, city_name=city_name, wikidata_results=wikidata_results)



    # Renderizar la plantilla con los datos obtenidos
    return render_template('clima.html', weather_data=weather_data, city_name=city_name, curiosities=curiosities)



    
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

