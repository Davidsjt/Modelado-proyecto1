import requests

def query_wikidata(city_name):
    url = 'https://query.wikidata.org/sparql'
    headers = {'Accept': 'application/sparql-results+json'}
    
    # Consulta SPARQL mejorada para obtener múltiples datos curiosos con descripciones
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
      }} # Sitio Patrimonio de la Humanidad
      OPTIONAL {{ 
          ?city wdt:P1071 ?battleLocation. 
          ?battleLocation rdfs:label ?curiosityLabel FILTER(LANG(?curiosityLabel) = "es").
          OPTIONAL {{ ?battleLocation schema:description ?curiosityDescription FILTER(LANG(?curiosityDescription) = "es") }}
      }} # Lugar de una batalla
      OPTIONAL {{ 
          ?city wdt:P61 ?revolutionLocation. 
          ?revolutionLocation rdfs:label ?curiosityLabel FILTER(LANG(?curiosityLabel) = "es").
          OPTIONAL {{ ?revolutionLocation schema:description ?curiosityDescription FILTER(LANG(?curiosityDescription) = "es") }}
      }} # Lugar de una revolución
      OPTIONAL {{ 
          ?city wdt:P84 ?earthquakeLocation. 
          ?earthquakeLocation rdfs:label ?curiosityLabel FILTER(LANG(?curiosityLabel) = "es").
          OPTIONAL {{ ?earthquakeLocation schema:description ?curiosityDescription FILTER(LANG(?curiosityDescription) = "es") }}
      }} # Lugar de un terremoto
      OPTIONAL {{ 
          ?city wdt:P964 ?airport. 
          ?airport rdfs:label ?curiosityLabel FILTER(LANG(?curiosityLabel) = "es").
          OPTIONAL {{ ?airport schema:description ?curiosityDescription FILTER(LANG(?curiosityDescription) = "es") }}
      }} # Tiene un aeropuerto
      OPTIONAL {{ 
          ?city wdt:P193 ?museum. 
          ?museum rdfs:label ?curiosityLabel FILTER(LANG(?curiosityLabel) = "es").
          OPTIONAL {{ ?museum schema:description ?curiosityDescription FILTER(LANG(?curiosityDescription) = "es") }}
      }} # Museo importante
      OPTIONAL {{ 
          ?city wdt:P138 ?honoree. 
          ?honoree rdfs:label ?curiosityLabel FILTER(LANG(?curiosityLabel) = "es").
          OPTIONAL {{ ?honoree schema:description ?curiosityDescription FILTER(LANG(?curiosityDescription) = "es") }}
      }} # Nombrado en honor a alguien
      OPTIONAL {{ 
          ?city wdt:P206 ?port. 
          ?port rdfs:label ?curiosityLabel FILTER(LANG(?curiosityLabel) = "es").
          OPTIONAL {{ ?port schema:description ?curiosityDescription FILTER(LANG(?curiosityDescription) = "es") }}
      }} # Puerta o puerto importante
      OPTIONAL {{ 
          ?city wdt:P1191 ?commercialDistrict. 
          ?commercialDistrict rdfs:label ?curiosityLabel FILTER(LANG(?curiosityLabel) = "es").
          OPTIONAL {{ ?commercialDistrict schema:description ?curiosityDescription FILTER(LANG(?curiosityDescription) = "es") }}
      }} # Distrito comercial relevante
      OPTIONAL {{ 
          ?city wdt:P915 ?filmLocation. 
          ?filmLocation rdfs:label ?curiosityLabel FILTER(LANG(?curiosityLabel) = "es").
          OPTIONAL {{ ?filmLocation schema:description ?curiosityDescription FILTER(LANG(?curiosityDescription) = "es") }}
      }} # Grabación de película o serie
      OPTIONAL {{ 
          ?city wdt:P1740 ?twinCity. 
          ?twinCity rdfs:label ?curiosityLabel FILTER(LANG(?curiosityLabel) = "es").
          OPTIONAL {{ ?twinCity schema:description ?curiosityDescription FILTER(LANG(?curiosityDescription) = "es") }}
      }} # Ciudad gemela
      OPTIONAL {{ 
          ?city wdt:P361 ?partOf. 
          ?partOf rdfs:label ?curiosityLabel FILTER(LANG(?curiosityLabel) = "es").
          OPTIONAL {{ ?partOf schema:description ?curiosityDescription FILTER(LANG(?curiosityDescription) = "es") }}
      }} # Parte de (una entidad más grande)
      OPTIONAL {{ 
          ?city wdt:P708 ?event. 
          ?event rdfs:label ?curiosityLabel FILTER(LANG(?curiosityLabel) = "es").
          OPTIONAL {{ ?event schema:description ?curiosityDescription FILTER(LANG(?curiosityDescription) = "es") }}
      }} # Evento importante
      OPTIONAL {{ 
          ?city wdt:P570 ?historicalFigureDeathDate. 
          ?historicalFigureDeathDate rdfs:label ?curiosityLabel FILTER(LANG(?curiosityLabel) = "es").
          OPTIONAL {{ ?historicalFigureDeathDate schema:description ?curiosityDescription FILTER(LANG(?curiosityDescription) = "es") }}
      }} # Fecha de muerte de una figura histórica
      OPTIONAL {{ 
          ?city wdt:P2046 ?area. 
          ?area rdfs:label ?curiosityLabel FILTER(LANG(?curiosityLabel) = "es").
          OPTIONAL {{ ?area schema:description ?curiosityDescription FILTER(LANG(?curiosityDescription) = "es") }}
      }} # Área
      OPTIONAL {{ 
          ?city wdt:P2397 ?mainTopic. 
          ?mainTopic rdfs:label ?curiosityLabel FILTER(LANG(?curiosityLabel) = "es").
          OPTIONAL {{ ?mainTopic schema:description ?curiosityDescription FILTER(LANG(?curiosityDescription) = "es") }}
      }} # Tema principal
      
      SERVICE wikibase:label {{ bd:serviceParam wikibase:language "es". }}
    }}
    ORDER BY DESC(?population) # Ordenar por población (mayor a menor)
    """
    params = {'query': query, 'format': 'json'}
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la consulta: {e}")
        return None
