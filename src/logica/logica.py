import os
import datetime as dt
import math
from PIL import Image, ImageTk

class Logica:
    def __init__(self, path_paso, path_foto, path_validacion, path_arranque, path_status):
        self.ruta_paso = path_paso
        self.ruta_foto = path_foto
        self.ruta_arranque = path_arranque
        self.ruta_status = path_status
        self.ruta_validacion = path_validacion

    def leer_paso(self):
        with open(self.ruta_paso) as f:
            paso_actual = f.read()
            paso_actual = paso_actual.replace(' ', '').replace('\n', '')
        return paso_actual
    
    def leer_status(self):
        with open(self.ruta_status) as f:
            status = f.read()
            status = status.replace(' ','').replace('\n', '')
        return status

    def leer_hora_arranque(self):
        with open(self.ruta_arranque) as f:
            arranque = f.read()
            arranque = arranque.replace(' ','').replace('\n', '')
        arranque = dt.datetime.strptime(arranque, '%d/%m/%Y,%H:%M:%S')
        return arranque
    
    def validar_estado(self):
        with open(self.ruta_validacion) as f:
            validacion = f.read()
            validacion = validacion.replace(' ', '').replace('\n', '')
        return validacion
    
    def fecha_actualizacion(self):
        fecha = os.path.getctime(self.ruta_foto)
        fecha = dt.datetime.fromtimestamp(fecha).strftime('%Y-%m-%d %H:%M')
        return fecha
    
    def procesar_foto(self):
        try:
            foto = Image.open(self.ruta_foto)
        except:
            foto = Image.new('RGB', (80, 60))
            foto.save('./src/media/foto.png', 'PNG')
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
    
    def iluminar_validacion(self, window, paso, luz_apagada, luz_encendida, luz_error):
        key_list = ['-LUZOK-', '-LUZNOOK-']
        for key in key_list:
            window[key].update(luz_apagada)
        if paso == '5':
            validacion = self.validar_estado()
            if validacion == 'OK':
                window[key_list[0]].update(luz_encendida)
            elif validacion == 'NOOK':
                window[key_list[1]].update(luz_error)
        return window
    
    def actualizar_foto(self, window, paso):
        if paso == '5':
            foto = self.procesar_foto()
            window['-FOTO-'].update(data = ImageTk.PhotoImage(image=foto))
            return window
    
    def actualizar_horainicio(self, window):
        hora_inicio = self.leer_hora_arranque()
        hora_actual = dt.datetime.now()
        diferencia_segundos = (hora_actual - hora_inicio).total_seconds()
        minutos = divmod(diferencia_segundos, 60)
        tiempo = f'Tiempo de ejecución:\n{math.floor(minutos[0])}:{math.floor(minutos[1])}'
        window['-TIEMPOINICIO-'].update(tiempo)
        return tiempo
    
    def status_sistema(self, window, status_ok, status_nook):
        status = self.leer_status()
        if status == '1':
            window['-LUZSTATUS-'].update(status_ok)
        else:
            window['-LUZSTATUS-'].update(status_nook)
        return window
    
    def start_button(self):
        with open("./src/data/start.txt", 'w') as f:
            f.write("1")
    
    def reset_button(self):
        with open("./src/data/start.txt", 'w') as f:
            f.write("0")


