const idiomaActual = document.getElementById('idioma');
const listaIdiomas = document.getElementById('idiomas');
const idiomas = document.getElementsByClassName('opcion');

// Info
const bienvenida = document.getElementById('bienvenida-info');
const escoja = document.getElementById('escoja-info');
const pasajeros = document.getElementById('pax-info');
const tripulacion = document.getElementById('tp-info');
const duda = document.getElementById('duda');
const busca_aero = document.getElementById('busca_aero');
const pregunta = document.getElementById('pregunta')
const seleccione = document.getElementById('seleccione')

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

// Se encarga de dar las frases al html en el idioma seleccionado por el usuario.
function establecerIdioma(idioma) {
    
    switch (idioma) {

        case 'ingles':
            bienvenida.textContent = 'Welcome!';
            escoja.textContent = 'Please select a profile';
            pasajeros.textContent = 'Passengers';
            tripulacion.textContent = 'Cabin Crew';
            duda.textContent = 'Having troubles finding where to do your check in?';
            busca_aero.textContent = 'Select your airline';
            pregunta.textContent = 'Troubles getting to the airport?'
            seleccione.textContent = 'Select an option.'
            document.documentElement.lang = 'en-US';
            break;
        case 'español':
            bienvenida.textContent = '¡Bienvenido!';
            escoja.textContent = 'Por favor escoja un perfil para iniciar'
            pasajeros.textContent = 'Pasajeros';
            tripulacion.textContent = 'Tripulación';
            duda.textContent = '¿No sabes cómo hacer tú check-in?';
            busca_aero.textContent = 'Selecciona tú aerolínea';
            pregunta.textContent = '¿Problemas para llegar?'
            seleccione.textContent = 'Seleccione una opción.'
            document.documentElement.lang = 'es-MX';
            break;
        case 'coreano':
            bienvenida.textContent = '환영합니다!';
            escoja.textContent = '시작하려면 프로필을 선택하세요.';
            tripulacion.textContent = '승무원';
            pasajeros.textContent = '승객';
            duda.textContent = '체크인 방법을 모르시나요?';
            busca_aero.textContent = '항공사 선택';
            pregunta.textContent = '공항에 가는 데 문제가 있으신가요?'
            seleccione.textContent = '옵션 선택'
            document.documentElement.lang = 'ko';
            break;
        case 'portugues':
            bienvenida.textContent = 'Bem-vindo!';
            escoja.textContent = 'Escolha um perfil para começar';
            tripulacion.textContent = 'Tripulação';
            pasajeros.textContent = 'Passageiros';
            duda.textContent = 'Não sabe como fazer o check-in?';
            busca_aero.textContent = 'Selecione a sua companhia aérea';
            pregunta.textContent = 'Problemas para chegar ao aeroporto?'
            seleccione.textContent = 'Selecionar uma opção'
            document.documentElement.lang = 'pt';
            break;
    
        default:
            break;
    }
}


//Se encarga de ver cuál es el lang del html para saber que idioma regresar.
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