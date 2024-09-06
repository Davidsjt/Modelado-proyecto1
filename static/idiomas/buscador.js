const idiomaActual = document.getElementById('idioma');
const listaIdiomas = document.getElementById('idiomas');
const idiomas = document.getElementsByClassName('opcion');

// Info
const busca = document.getElementById('busca-info');
const porfa = document.getElementById('porfa-info');
const mensaje = document.getElementById('mensaje-info');


// Toggle lista idiomas
idiomaActual.addEventListener('click',()=>{
    listaIdiomas.classList.toggle('toggle');
});

const opcionesArray = Array.from(idiomas);

opcionesArray.forEach((opcion)=>{
    opcion.addEventListener('click',()=>{
        const idioma = opcion.getElementsByTagName('span')[0].textContent.toLowerCase();
        establecerIdioma(idioma);
    });
});


function establecerIdioma(idioma) {
    
    switch (idioma) {
        case 'ingles':
            busca.textContent = 'Let\'s look the weather';
            porfa.textContent = 'Please enter city, ticket or IATA code';
            miPlaceholderId = 'Let\'s search the weather in... '
            break;
        case 'español':
            busca.textContent = 'Busquemos el clima de interes';
            porfa.textContent = 'Por favor ingrese ciudad, ticket o IATA.';
            break;
        case 'coreano':
            busca.textContent = '관심 있는 분위기를 찾아보세요';
            porfa.textContent = '도시, 항공권 또는 IATA를 입력하세요.';
            break;
        case 'portugues':
            busca.textContent = 'Vamos ver o clima';
            porfa.textContent = 'Introduzir cidade, bilhete ou IATA.';
            break;
    
        default:
            break;
    }
}

document.addEventListener('DOMContentLoaded',()=>{
    
    const lang = document.documentElement.getAttribute('lang');

    switch (lang) {
        case 'es-MX':
            establecerIdioma('español')
            break;
        case 'en-US':
            establecerIdioma('ingles')
            break;
        case 'coreano':
            establecerIdioma('coreano')
            break;
        case 'portugues':
            establecerIdioma('portugues')
            break;
        
        default:
            break;
    }
});