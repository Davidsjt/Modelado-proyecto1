import pandas as pd
from rapidfuzz import process

def load_iata_data(file_path):
    """
    Loads IATA code and city data from a CSV file.
    
    Args:
        file_path (str): The path to the CSV file containing IATA codes and city names.

    Returns:
        dict: A dictionary mapping IATA codes to city names.
        list: A list of unique city names for fuzzy matching.
    """
    # Load the CSV into a DataFrame
    df = pd.read_csv(file_path)
    # Create a dictionary with IATA Code as keys and City names as values
    iata_to_city = pd.Series(df.City.values, index=df.Code).to_dict()
    # Create a list of unique city names for fuzzy matching
    valid_cities = df['City'].unique().tolist()
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
    Converts a hexadecimal string to an IATA code and maps it to a city name.

    Args:
        hex_string (str): The hexadecimal representation of an IATA code.
        iata_to_city (dict): The dictionary mapping IATA codes to city names.

    Returns:
        str or None: The city name if the conversion and mapping are successful, otherwise None.
    """
    try:
        # Convert hex to IATA code
        iata_code = bytes.fromhex(hex_string).decode('utf-8')
        return map_iata_to_city(iata_code, iata_to_city)
    except ValueError:
        return None
