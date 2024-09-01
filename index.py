from flask import Flask, request, render_template

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
    iata_code = request.args.get('iata_code')  # Obtener el valor del parámetro 'iata_code'
    if iata_code:
        # Aquí puedes procesar el código IATA y realizar la búsqueda del clima
        # Por ejemplo, podrías hacer una solicitud a la API de clima
        # Y luego pasar los datos a una plantilla para mostrarlos
        # Por ahora solo muestra el código recibido
        return render_template('clima.html', iata_code=iata_code)  # Pasar el código IATA a la plantilla
    else:
        return render_template('clima.html', error='No se ha ingresado ningún código IATA')

@app.route('/pasajeros/clima', methods=['GET'])
def climap():
    iata_code = request.args.get('iata_code')  # Obtener el valor del parámetro 'iata_code'
    if iata_code:
        # Aquí puedes procesar el código IATA y realizar la búsqueda del clima
        # Por ejemplo, podrías hacer una solicitud a la API de clima
        # Y luego pasar los datos a una plantilla para mostrarlos
        # Por ahora solo muestra el código recibido
        return render_template('climapa.html', iata_code=iata_code)  # Pasar el código IATA a la plantilla
    else:
        return render_template('climapa.html', error='No se ha ingresado ningún código IATA')

if __name__ == '__main__':
    app.run(debug=True)

