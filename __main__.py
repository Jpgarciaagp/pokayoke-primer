from src.interfaz.gui import AppPrimer
from src.logica.logica import Logica

foto = './src/media/foto.png'
paso = './paso.txt'
validacion = './validacion.txt'
logica = Logica(paso, foto, validacion)
def main():
    app = AppPrimer(
        logo='./src/media/logo_sglass blanco.png',
        title='POKAYOKE - APLICACIÓN DE PRIMER PU',
        width=1280,
        height=720,
        logica = logica,
        start = './src/media/start.png',
        stop = './src/media/stop.png',
        lights_off = './src/media/light_off.png',
        lights_on = './src/media/light_on.png',
        lights_error = './src/media/light_error.png',
        status_ok = './src/media/status_ok.png',
        status_nook = './src/media/status_nook.png',
        p_naranja = './src/media/naranja.png',
        p_rosado = './src/media/rosado.png',
        p_verde = './src/media/verde.png',
        )
    window = app.window
    app.ejecutar(window)

if __name__ == '__main__':
    main()