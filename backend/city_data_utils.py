import pandas as pd
from rapidfuzz import process
import unicodedata

# Diccionario de sinónimos de ciudades para normalizar las entradas
city_synonyms = {
    "Ciudad De México": ["CDMX", "Ciudad De México", "Ciudad De Mexico", "Ciudad de Mexico", "Mexico City"],
    "Nueva York": ["NYC", "New York", "New York City"],
    "Sao Paulo": ["Sao Paulo", "São Paulo"],
}

def remove_accents(input_str):
    """
    Elimina los acentos de un string.

    Args:
        input_str (str): Cadena de texto de entrada.

    Returns:
        str: Cadena de texto sin acentos.
    """
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return "".join([c for c in nfkd_form if not unicodedata.combining(c)])

def load_iata_data(file_path):
    """
    Carga los datos de códigos IATA y nombre de ciudades.

    Args:
        file_path (str): El directorio donde se encuentra el archivo.

    Returns:
        dict: Diccionario que mapea los IATA con los nombres de las ciudades.
        list: Lista de nombres ocupados para corregir errores ortográficos.
    """
    df = pd.read_csv(file_path, encoding='utf-8')
    iata_to_city = {row['Code']: row['City'] for _, row in df.iterrows()}
    valid_cities = set(df['City'].unique())

    return iata_to_city, valid_cities

def normalize_city_name(user_input):
    """
    Normaliza el nombre de la ciudad usando el diccionario de sinónimos y eliminando acentos.

    Args:
        user_input (str): El nombre de ciudad proporcionado por el usuario.

    Returns:
        str: El nombre de la ciudad normalizado si se encuentra, de lo contrario devuelve la entrada original.
    """
    # Convertir a minúsculas y eliminar acentos para comparación
    cleaned_input = remove_accents(user_input.lower())

    # Recorre el diccionario para encontrar el nombre normalizado
    for city_name, synonyms in city_synonyms.items():
        # Convertir también las entradas del diccionario a minúsculas y sin acentos
        cleaned_synonyms = [remove_accents(syn.lower()) for syn in synonyms]
        if cleaned_input in cleaned_synonyms:
            return city_name
    return user_input

def get_closest_city_name(user_input, city_list):
    """
    Encuentra el nombre de ciudad más cercano de una lista de nombres de ciudades válidos.

    Args:
        user_input (str): El input del nombre de ciudad proporcionado por el usuario.
        city_list (list): La lista de ciudades válidas.

    Returns:
        str: El nombre de ciudad que tiene el match más cercano.
    """
    # Normaliza el nombre de la ciudad usando el diccionario de sinónimos
    normalized_input = normalize_city_name(user_input)
    # Encuentra el match más cercano de la lista de nombres válidos de ciudades
    closest_match = process.extractOne(normalized_input, city_list, score_cutoff=80)
    if closest_match:
        return closest_match[0]
    return user_input  # Devuelve el input si no se encuentra un match cercano

def map_iata_to_city(iata_code, iata_to_city):
    """
    Asigna un código IATA a un nombre de ciudad utilizando un diccionario proporcionado.

    Args:
        iata_code (str): El código IATA a mapear.
        iata_to_city (dict): El diccionario que relaciona los códigos IATA con los nombres de las ciudades.

    Returns:
        str or None: El nombre de la ciudad si es encontrado, de lo contrario None.
    """
    return iata_to_city.get(iata_code.upper(), None)

def hex_to_iata(hex_string, iata_to_city):
    """
    Convierte una cadena hexadecimal (correspondiente al ticket) en código IATA.

    Args:
        hex_string (str): El ticket como cadena hexadecimal.
        iata_to_city (dict): El diccionario de códigos IATA.

    Returns:
        str or None: El código IATA en caso de ser un ticket válido, o None si no lo es.
    """
    try:
        # Convertir hexadecimal a código IATA
        iata_code = bytes.fromhex(hex_string).decode('utf-8')
        return iata_code
    except ValueError:
        return None

