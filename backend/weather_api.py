@app.route('/obtener_clima', methods=['GET'])
def obtener_clima():
    city_name = request.args.get('city_name')  # Obtener el nombre de la ciudad del formulario

    if city_name:
        complete_url = f"{base_url}appid={api_key}&q={city_name}&lang=es"
        response = requests.get(complete_url)
        x = response.json()

        if x["cod"] != "404":
            y = x["main"]
            current_temperature_kelvin = y["temp"]
            current_temperature_celsius = current_temperature_kelvin - 273.15
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]

            # Pasar los datos a la plantilla
            return render_template('resultado_clima.html',
                                   city_name=city_name,
                                   temperature=current_temperature_celsius,
                                   pressure=current_pressure,
                                   humidity=current_humidity,
                                   description=weather_description.capitalize())
        else:
            return render_template('resultado_clima.html', error="Ciudad no encontrada")
    else:
        return render_template('resultado_clima.html', error="No se proporcionó el nombre de la ciudad")



