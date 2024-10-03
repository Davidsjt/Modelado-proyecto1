# Modelado-proyecto1
Equipo Maravilla haciendo maravillas
# Aplicación de Clima

## Integrantes del Equipo
* Flores Arriola Rafael Edson -
* Ortega Medina David -
* Rivera Soto Aline Daniela -320333035

## Descripción
Esta es una aplicación web desarrollada con Flask que permite a los usuarios buscar información el clima en las ciudadesde origen y destino. La aplicación se conecta a una base de datos y utiliza la API de OpenWeatherMap para obtener datos meteorológicos en tiempo real.

## Estructura de Carpetas
El proyecto se organiza en las siguientes carpetas:

### static
Esta carpeta contiene los archivos estáticos utilizados para la interfaz de usuario de la página web, como hojas de estilo CSS e imágenes, además de contener todos los CSV.

### templates
En esta carpeta se encuentran los archivos HTML que conforman la página web de la aplicación. Hay dos plantillas principales:

1.`pasajeros.html` y `tripulación.html`:Estas plantillas se utilizan para recopilar información de los usuarios a travésde un formulario.
2. `clima.html` y `climapa.html` : Aquí se muestran los resultados de las búsquedas y datos meteorológicos, además de permitir hacer una nueva busqueda.

### backend
Aquí se encuentra todo el código responsable de que la aplicación funcione como se espera.

### test
Podemos encontrar pruebas unitarias del código que se encuentra en la carpeta de `backend`.

## Requisitos

Asegúrate de tener los siguientes requisitos en tu sistema:

- Python 3
- pip (administrador de paquetes de Python)
- Cuenta de OpenWeatherMap API y su clave de API
- Flask

## Uso
Para ejecutar la aplicación, se debe tener  Python y Flask instalados. Luego, sigue estos pasos:

1. Clona el repositorio desde la terminal:

```bash
   $ git clone https://github.com/Davidsjt/Modelado-proyecto1.git
```

2. Agregar la clave de la API de OpenWeatherMap en el archivo `weather_api.py`:

``` python
     api_key = '-----' (Línea de codigo: 5)
```


## Pasos para ejecutar la página:
- Ejecutar la aplicación Flask:
Linux:
```bash
    $ cd Modelado-proyecto1
    $ flask --app index run
```
Esto ejecutara un 'http://localhost:5000', esto lo tendras que abir desde tu navegador


## Funcionalidades Principales
La aplicación ofrece las siguientes funcionalidades:

- Búsqueda de clima por ciudad de origen y destino.
- Búsqueda de clima por IATA.
- Búsqueda de clima por número de ticket(temporalmente solo con samples).
- Visualización de datos meteorológicos en tiempo real de las ciudades de origen y destino.


## API de OpenWeatherMap
Para obtener datos meteorológicos, la aplicación se conecta a la API de OpenWeatherMap. Debes proporcionar tu propia clave de API en el archivo `weather_api.py` para que funcione correctamente.

## Documentación: 

- Python: https://docs.python.org/
- Flask: https://flask.palletsprojects.com/ 



# Roles de trabajo

* Daniela. Frontend 
* David y Edson. Backend


# Recursos Online
* https://www.pexels.com/es-es/  Imagenes sin copyright.
* https://www.flaticon.es/ Iconos PNG para la pagina. 
* https://fonts.google.com/   Fuentes de texto gratuitas para pagina web.
