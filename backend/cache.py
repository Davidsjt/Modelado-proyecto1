from datetime import datetime, timedelta

# Diccionario global de caché compartido
_cache = {}
cache_duration = 1800  # Duración del caché en segundos (30 minutos)

def get_from_cache(key): # Recupera un valor del caché si no ha expirado
    if key in _cache: # key (str): La clave que se busca en el caché
        value, last_updated = _cache[key]
        if datetime.now() - last_updated < timedelta(seconds=cache_duration):
            return value, last_updated
    return None, None #   tuple: (Valor en caché, Última actualización) o (None, None)

def set_to_cache(key, value): #Almacena un valor en el caché con la clave dada
    _cache[key] = (value, datetime.now()) # key (str): La clave a usar en el caché
# value (any): El valor a almacenar en el caché

def clear_cache(): # Limpia todo el caché
    _cache.clear()
