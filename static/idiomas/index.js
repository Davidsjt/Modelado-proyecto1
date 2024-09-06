const idiomaActual = document.getElementById('idioma');
const listaIdiomas = document.getElementById('idiomas');
const idiomas = document.getElementsByClassName('opcion');

// Info
const bienvenida = document.getElementById('bienvenida-info');
const escoja = document.getElementById('escoja-info');
const pasajeros = document.getElementById('pax-info');
const tripulacion = document.getElementById('tp-info');

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
})

function establecerIdioma(idioma) {
    
    switch (idioma) {

        case 'ingles':
            bienvenida.textContent = 'Welcome!';
            escoja.textContent = 'Please select a profile';
            pasajeros.textContent = 'Passengers';
            tripulacion.textContent = 'Cabin Crew';
            document.documentElement.lang = 'en-US';
            break;
        case 'español':
            bienvenida.textContent = '¡Bienvenido!';
            escoja.textContent = 'Por favor escoja un perfil para iniciar'
            pasajeros.textContent = 'Pasajeros';
            tripulacion.textContent = 'Tripulación';
            break;
        case 'coreano':
            bienvenida.textContent = '환영합니다!';
            escoja.textContent = '시작하려면 프로필을 선택하세요.';
            tripulacion.textContent = '승무원';
            pasajeros.textContent = '승객';
            document.documentElement.lang = 'coreano';
            break;
        case 'portugues':
            bienvenida.textContent = 'Bem-vindo!';
            escoja.textContent = 'Escolha um perfil para começar';
            tripulacion.textContent = 'Tripulação';
            pasajeros.textContent = 'Passageiros';
            document.documentElement.lang = 'portugues';
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