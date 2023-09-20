import os
import datetime as dt
from PIL import Image, ImageTk

class Logica:
    def __init__(self, path_paso, path_foto, path_validacion):
        self.ruta_paso = path_paso
        self.ruta_foto = path_foto
        self.ruta_validacion = path_validacion

    def leer_paso(self):
        with open(self.ruta_paso) as f:
            paso_actual = f.read()
        return paso_actual
    
    def validar_estado(self):
        with open(self.ruta_validacion) as f:
            validacion = f.read()
        return validacion
    
    def fecha_actualizacion(self):
        fecha = os.path.getctime(self.ruta_foto)
        fecha = dt.datetime.fromtimestamp(fecha).strftime('%Y-%m-%d %H:%M')
        return fecha
    
    def procesar_foto(self):
        foto = Image.open(self.ruta_foto)
        w, h = foto.size
        foto_final = foto.resize((w*5, h*5))
        return foto_final
    
    def iluminar_paso(self, window, paso_actual, luz_apagada, luz_encendida):
        key_list = ['-LUZ1-','-LUZ2-','-LUZ3-','-LUZ4-','-LUZ5-']
        for key in key_list:
            window[key].update(luz_apagada)
        if paso_actual == '1':
            window[key_list[0]].update(luz_encendida)
        if paso_actual == '2':
            window[key_list[1]].update(luz_encendida)
        if paso_actual == '3':
            window[key_list[2]].update(luz_encendida)
        if paso_actual == '4':
            window[key_list[3]].update(luz_encendida)
        if paso_actual == '5':
            window[key_list[4]].update(luz_encendida)
        return window
    
    def iluminar_validacion(self, window, paso, luz_apagada, luz_encendida):
        key_list = ['-LUZOK-', '-LUZNOOK-']
        for key in key_list:
            window[key].update(luz_apagada)
        if paso == '5':
            validacion = self.validar_estado()
            if validacion == 'OK':
                window[key_list[0]].update(luz_encendida)
            elif validacion == 'NO OK':
                window[key_list[1]].update(luz_encendida)
        return window
    
    def actualizar_foto(self, window, paso):
        if paso == 5:
            foto = self.procesar_foto()
            window['-FOTO-'].update(data = ImageTk.PhotoImage(image=foto))
            return window