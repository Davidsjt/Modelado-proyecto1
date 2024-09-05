import requests

# Función para realizar la consulta a Wikidata
def query_wikidata_pasajeros(city_or_iata):
    url = 'https://query.wikidata.org/sparql'
    headers = {'Accept': 'application/sparql-results+json'}
    
    query = f"""
    SELECT ?cityLabel ?countryLabel ?population ?description ?curiosityLabel ?curiosityDescription 
           ?airportLabel ?airportDistance ?altitude ?incidentLabel ?historicalSiteLabel 
           ?touristAttractionLabel ?eventLabel WHERE {{
      {{
        # Si el input es un nombre de ciudad (en inglés o español)
        ?city wdt:P31/wdt:P279* wd:Q515;   # Instancia de "ciudad" o subtipo
              rdfs:label ?cityName;        # Coincide con la etiqueta
              wdt:P17 ?country;            # Relación con el país
              wdt:P1082 ?population.       # Población
        FILTER(LANG(?cityName) = "en" || LANG(?cityName) = "es") # Filtrar por idioma
        FILTER(?cityName = "{city_or_iata}"@en || ?cityName = "{city_or_iata}"@es) # Coincide con el input en inglés o español
      }} UNION {{
        # Si el input es un código IATA
        ?airport wdt:P238 "{city_or_iata}";   # Coincide con el código IATA
                 wdt:P131 ?city.              # Relacionado con una ciudad
        ?city wdt:P31/wdt:P279* wd:Q515;      # Instancia de "ciudad" o subtipo
              wdt:P17 ?country;               # Relación con el país
              wdt:P1082 ?population.          # Población
      }}
      
      OPTIONAL {{ ?city schema:description ?description FILTER(LANG(?description) = "es") }} # Descripción en español
      
      # Aeropuertos importantes en la ciudad
      OPTIONAL {{ 
          ?city wdt:P527 ?airport. 
          ?airport wdt:P31 wd:Q1248784;   # Instancia de aeropuerto
                   rdfs:label ?airportLabel FILTER(LANG(?airportLabel) = "es").
          ?airport wdt:P2582 ?airportDistance. # Distancia del aeropuerto al centro de la ciudad
      }}
      
      # Altitud de la ciudad
      OPTIONAL {{ ?city wdt:P2044 ?altitude. }}
      
      # Accidentes aéreos importantes en las cercanías de la ciudad
      OPTIONAL {{ 
          ?incident wdt:P31 wd:Q744913;  # Instancia de accidente aéreo
                    wdt:P131 ?city;       # Relacionado con la ciudad
                    rdfs:label ?incidentLabel FILTER(LANG(?incidentLabel) = "es").
      }}
      
      # Eventos importantes relacionados con la ciudad
      OPTIONAL {{
          ?city wdt:P793 ?event.
          ?event rdfs:label ?eventLabel FILTER(LANG(?eventLabel) = "es").
      }}

      SERVICE wikibase:label {{ bd:serviceParam wikibase:language "es". }}
    }}
    ORDER BY DESC(?population) # Ordenar por población (mayor a menor)
    """
    
    params = {'query': query, 'format': 'json'}
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        return format_city_data(data)
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la consulta: {e}")
        return "Error al consultar los datos."

# Función para formatear los datos de la ciudad
def format_city_data(data):
    if data and 'results' in data and 'bindings' in data['results']:
        results = data['results']['bindings']
        if results:
            city_info = results[0]
            city_label = city_info.get('cityLabel', {}).get('value', 'N/A')
            country_label = city_info.get('countryLabel', {}).get('value', 'N/A')
            population = city_info.get('population', {}).get('value', 'N/A')
            description = city_info.get('description', {}).get('value', 'N/A')
            
            # Información de aeropuertos, accidentes aéreos, curiosidades, sitios históricos, etc.
            airports = []
            incidents = []
            curiosities_pasajeros = []
            historical_sites = []
            tourist_attractions = []
            events = []

            for result in results:
                airport_label = result.get('airportLabel', {}).get('value')
                airport_distance = result.get('airportDistance', {}).get('value', 'N/A')
                if airport_label:
                    airports.append(f"Aeropuerto: {airport_label}, Distancia al centro: {airport_distance} km")
                
                incident_label = result.get('incidentLabel', {}).get('value')
                if incident_label:
                    incidents.append(f"Incidente: {incident_label}")
            
                event_label = result.get('eventLabel', {}).get('value')
                if event_label:
                    events.append(f"Evento: {event_label}")

            # Limitar a un máximo de 5 eventos
            events = events[:1]

            if not curiosities_pasajeros:
                curiosities_pasajeros = ["Sin datos curiosos disponibles"]
            if not airports:
                airports = ["No se encontraron aeropuertos relevantes."]
            if not incidents:
                incidents = ["No se encontraron accidentes aéreos relevantes."]
            if not events:
                events = ["No se encontraron eventos relevantes."]

            altitude = city_info.get('altitude', {}).get('value', 'N/A')

            output = (
                f"País: {country_label}\n"
                f"Población: {population}\n"
                f"Descripción: {description}\n"
                f"Altitud: {altitude} metros\n\n"
                f"Aeropuertos:\n" + "\n".join(airports) + "\n\n"
                f"Accidentes Aéreos:\n" + "\n".join(incidents) + "\n\n"
                f"Eventos Relevantes:\n" + "\n".join(events)
            )
            return output
    return "No se encontraron datos para la ciudad especificada."


