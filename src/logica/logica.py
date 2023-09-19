import os
from PIL import Image

class Logica:
    def __init__(self, path_paso, path_foto):
        self.ruta_paso = path_paso
        self.ruta_foto = path_foto

    def leer_paso(self):
        with open(self.ruta_paso) as f:
            paso_actual = f.read()
        return paso_actual
    
    def fecha_actualizacion(self):
        fecha = os.path.getctime(self.ruta_foto)
        return fecha
    
    def procesar_foto(self):
        foto = Image.open(self.ruta_foto)
        w, h = foto.size
        foto_final = foto.resize(w*5, h*5)
        return foto_final