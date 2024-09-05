import requests

# Función para realizar la consulta a Wikidata
def query_wikidata(city_name):
    url = 'https://query.wikidata.org/sparql'
    headers = {'Accept': 'application/sparql-results+json'}
    
    query = f"""
    SELECT ?cityLabel ?countryLabel ?population ?description ?curiosityLabel ?curiosityDescription WHERE {{
      ?city wdt:P31/wdt:P279* wd:Q515;   # Instancia de "ciudad" o subtipo
            rdfs:label "{city_name}"@en;  # Coincide con la etiqueta en inglés
            wdt:P17 ?country;             # Relación con el país
            wdt:P1082 ?population.        # Población
      OPTIONAL {{ ?city schema:description ?description FILTER(LANG(?description) = "es") }} # Descripción en español
      
      # Datos curiosos y sus descripciones
      OPTIONAL {{ 
          ?city p:P1435 ?heritageStatement. 
          ?heritageStatement ps:P1435 ?heritageSite. 
          ?heritageSite rdfs:label ?curiosityLabel FILTER(LANG(?curiosityLabel) = "es").
          OPTIONAL {{ ?heritageSite schema:description ?curiosityDescription FILTER(LANG(?curiosityDescription) = "es") }}
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
            
            curiosities = []
            for result in results:
                curiosity_label = result.get('curiosityLabel', {}).get('value')
                curiosity_description = result.get('curiosityDescription', {}).get('value', '')
                if curiosity_label:
                    curiosities.append(f"{curiosity_label}: {curiosity_description}")

            if not curiosities:
                curiosities = ["Sin datos curiosos disponibles"]

            output = (
                f"Ciudad: {city_label}\n"
                f"País: {country_label}\n"
                f"Población: {population}\n"
                f"Descripción: {description}\n"
                f"Datos curiosos:\n" + "\n".join(curiosities)
            )
            return output
    return "No se encontraron datos para la ciudad especificada."

