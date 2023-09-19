from src.interfaz.gui import AppPrimer
from src.logica.logica import Logica

logica = Logica()
def main():
    app = AppPrimer(
        logo='./src/media/logo_sglass blanco.png',
        title='POKAYOKE - APLICACIÓN DE PRIMER PU',
        width=1280,
        height=720,
        logica = logica
    )
    window = app.window,
    app.ejecutar(window)

if __name__ == '__main__':
    main()