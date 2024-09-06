import pandas as pd
from rapidfuzz import process

def load_iata_data(file_path):
    """
    Carga los datos de codigos IATA y nombre de ciudades.
    
    Args:
        file_path (str): El directorio donde se encuentra el archivo.

    Returns:
        dict: Diccionario que mapea los IATA con los nombres de las ciudades.
        list: Lista de nombres ocupados para corregir errores ortograficos.
    """
    df = pd.read_csv(file_path, encoding='utf-8')
    iata_to_city = {row['Code']: row['City'] for _, row in df.iterrows()}
    valid_cities = set(df['City'].unique())

    return iata_to_city, valid_cities

def map_iata_to_city(iata_code, iata_to_city):
    """
    Maps an IATA code to a city name using a provided dictionary.

    Args:
        iata_code (str): The IATA code to map.
        iata_to_city (dict): The dictionary mapping IATA codes to city names.

    Returns:
        str or None: The city name if found, otherwise None.
    """
    return iata_to_city.get(iata_code.upper(), None)

def get_closest_city_name(user_input, city_list):
    """
    Finds the closest matching city name from a list of valid city names.

    Args:
        user_input (str): The user input city name to correct.
        city_list (list): The list of valid city names.

    Returns:
        str: The closest matching city name.
    """
    # Find the closest match from the list of valid city names
    closest_match = process.extractOne(user_input, city_list, score_cutoff=80)  # Use a threshold for match confidence
    if closest_match:
        return closest_match[0]
    return user_input  # Return the input if no close match is found

def hex_to_iata(hex_string, iata_to_city):
    """
    Convierte una cadena hexadecimal (correspondiente al ticket) en codigo IATA.

    Args:
        hex_string (str): El ticket como cadena hexadecimal.
        iata_to_city (dict): El diccionario de codigos IATA

    Returns:
        str or None: El codigo IATA en caso de ser un ticket válido, o None si no.
    """
    try:
        # Convert hex to IATA code
        iata_code = bytes.fromhex(hex_string).decode('utf-8')
        return iata_code
    except ValueError:
        return None
