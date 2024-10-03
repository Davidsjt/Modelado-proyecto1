// Info
const climaen = document.getElementById('climaen-info');
const temp = document.getElementById('temp-info');
const tempmin = document.getElementById('tempmin-info');
const tempmax = document.getElementById('tempmax-info');
const presion = document.getElementById('presion-info');
const humedad = document.getElementById('humedad-info');
const desc = document.getElementById('desc-info');
const viento = document.getElementById('viento-info');
const vis = document.getElementById('vis-info');
const amanecer = document.getElementById('amanecer-info');
const nubes = document.getElementById('nubes-info');
const anochecer = document.getElementById('anochecer-info');
const sensater = document.getElementById('sensater-info');

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

function establecerIdioma(idioma) {
    
    switch (idioma) {
        case 'ingles':
            climaen.textContent = 'Weather in';
            temp.textContent = 'Temperature:';
            tempmin.textContent = 'Minimum temperature:';
            tempmax.textContent = 'Maximum temperature:';
            presion.textContent = 'Pressure:';
            humedad.textContent = 'Humidity:';
            desc.textContent = 'Description:';
            viento.textContent = 'Wind:';
            vis.textContent = 'Visibility:';
            amanecer.textContent = 'Sunrise:';
            nubes.textContent = 'Clouds:';
            anochecer.textContent = 'Sunset:';
            sensater.textContent = 'Feels like:';
            break;
        case 'español':
            climaen.textContent = 'Clima en';
            temp.textContent = 'Temperatura';
            tempmin.textContent = 'Temperatura mínima';
            tempmax.textContent = 'Temperatura máxima';
            presion.textContent = 'Presión';
            humedad.textContent = 'Humedad';
            desc.textContent = 'Descripción';
            viento.textContent = 'Viento:';
            vis.textContent = 'Visibilidad:';
            amanecer.textContent = 'Amanecer:';
            nubes.textContent = 'Nubosidad:';
            anochecer.textContent = 'Anochecer:';
            sensater.textContent = 'Sensación Termica:';
            break;
        case 'coreano':
            climaen.textContent = '기후';
            temp.textContent = '온도';
            tempmin.textContent = '최소 온도';
            tempmax.textContent = '최대 온도';
            presion.textContent = '압력';
            humedad.textContent = '습도';
            desc.textContent = '설명';
            viento.textContent = '바람';
            vis.textContent = '가시성';
            amanecer.textContent = '일출';
            nubes.textContent = '클라우드';
            anochecer.textContent = '일몰';
            sensater.textContent = '열 감각';
            
            break;
        case 'portugues':
            climaen.textContent = 'Clima em';
            temp.textContent = 'Temperatura';
            tempmin.textContent = 'Temperatura mínima';
            tempmax.textContent = 'Temperatura máxima';
            presion.textContent = 'Pressão';
            humedad.textContent = 'Humidade';
            desc.textContent = 'Descrição';
            viento.textContent = 'Vento';
            vis.textContent = 'Visibilidade';
            amanecer.textContent = 'Nascer do sol';
            nubes.textContent = 'Nuvens';
            anochecer.textContent = 'Anoitecer';
            sensater.textContent = 'Sensação térmica';

            break;
    
        default:
            break;
    }
}


