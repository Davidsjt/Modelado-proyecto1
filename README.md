# Aplicación de Clima

## Integrantes del Equipo
* Flores Arriola Rafael Edson - 423118018
* Ortega Medina David - 319111866
* Rivera Soto Aline Daniela -320333035

## Descripción
Esta es una aplicación web desarrollada con Flask que permite a los usuarios buscar información el clima en las ciudades en tiempo real. La aplicación utiliza la API de OpenWeatherMap para obtener datos meteorológicos en tiempo real.

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

2. Agregar la clave de la API de OpenWeatherMap en el archivo `.env`:

```
 OPENWEATHER_API_KEY=tu_clave_api_aqui
```
   - En algunos sistemas de carpetas como en Fedora el archivo `.env` no aparece después de clonarlo, sin embargo al abrirlo en una IDE el archivo se encuentra ahí.
   - Si no llegara a estar, crear un archivo en la altura de index.py, llamarlo `.env`  y colocar estaa linea `OPENWEATHER_API_KEY=tu_clave_api_aqui` (con tu clave api)

## Pasos para ejecutar la página:
- Ejecutar la aplicación Flask:
Linux:
```bash
    $ cd Modelado-proyecto1
    $ export FLASK_APP=index
    $ flask --app index run
```
Microsoft:
Entrar a Visual Studio Code y abrir el archivo 'index.py', una vez parado ahí darle click al play que se muestra en la esquina superior derecha.

Esto ejecutara un 'http://localhost:5000', dicho link lo tendras que abir desde tu navegador


## Funcionalidades Principales
La aplicación ofrece las siguientes funcionalidades:

- Búsqueda de clima por ciudad de origen y destino.
- Búsqueda de clima por IATA.
- Búsqueda de clima por número de ticket(temporalmente solo con samples).
- Visualización de datos meteorológicos en tiempo real de las ciudades.


## API de OpenWeatherMap
Para obtener datos meteorológicos, la aplicación se conecta a la API de OpenWeatherMap. Debes proporcionar tu propia clave de API en el archivo `.env` para que funcione correctamente.

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
