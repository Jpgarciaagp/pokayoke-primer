import PySimpleGUI as psg
import datetime as dt
from PIL import ImageTk

class AppPrimer:    
    def __init__(self, logo, title, width, height, logica, lights_off, lights_on, lights_error, start, stop, status_ok, status_nook, p_naranja, p_rosado, p_verde):
        self.logica = logica
        self.banner_font = ("Segoe UI", 28, "bold")
        self.default_font = ("Segoe UI", 16)
        self.titles_font = ("Segoe UI", 20, "bold")
        self.subtitles_font = ("Segoe UI", 12)
        self.update_font = ("Segoe UI", 12)
        self.bg_color = '#eef5f6'
        self.banner_color = '#8fc5cf'
        self.titles_color = '#5F7A83'
        self.title = title
        self.logo = logo
        self.foto = logica.procesar_foto()
        self.lights_off = lights_off
        self.lights_on = lights_on
        self.lights_error = lights_error
        self.start = start
        self.stop = stop
        self.status_ok = status_ok
        self.status_nook = status_nook
        self.p_naranja = p_naranja
        self.p_rosado = p_rosado
        self.p_verde = p_verde
        
        self.window = self.construct_window(width, height)        
    
    def update_banner(self, banner, width):
        banner.erase()
        banner.DrawText(self.title,(width/4,50),color='white', font=self.banner_font)
        banner.DrawImage(filename=self.logo, location=(20,0))
        banner.DrawText(self.logica.fecha_actualizacion(), (width/2.15, 35), color='white', font=self.update_font)
        banner.DrawText('Actualización', (width/2.15, 60),color='white',font=self.update_font)
    

    def construct_window(self, width, height):
        new_theme = {"BACKGROUND": self.bg_color, "TEXT": psg.COLOR_SYSTEM_DEFAULT, "INPUT": psg.COLOR_SYSTEM_DEFAULT,
             "TEXT_INPUT": psg.COLOR_SYSTEM_DEFAULT, "SCROLL": psg.COLOR_SYSTEM_DEFAULT,
             "BUTTON": psg.OFFICIAL_PYSIMPLEGUI_BUTTON_COLOR, "PROGRESS": psg.COLOR_SYSTEM_DEFAULT, "BORDER": 1,
             "SLIDER_DEPTH": 1, "PROGRESS_DEPTH": 0
             }
        psg.theme_add_new('AGP', new_theme)
        psg.theme('AGP')
        
        banner = [psg.Graph(canvas_size=(width,100), graph_bottom_left=(0,100), graph_top_right=(width/2,0), 
                            expand_x=True, background_color=self.banner_color)] # Banner should always have 100px height
        
        footer = [psg.Graph(canvas_size=(width,50), graph_bottom_left=(0,height), 
        graph_top_right=(width/2,(height-50)), 
                            expand_x=True, background_color=self.banner_color)] # Footer should always have 50px height

        foto_title = psg.Text(text='ÚLTIMA FOTO TOMADA', font=self.titles_font, text_color=self.titles_color,
                              pad=((50,0),(0,0)))
        foto = psg.Image(background_color=self.bg_color, key='-FOTO-', pad=((0,0),(50, 0)))
        luz_1 = psg.Image(self.lights_off, key='-LUZ1-')
        luz_2 = psg.Image(self.lights_off, key='-LUZ2-')
        luz_3 = psg.Image(self.lights_off, key='-LUZ3-')
        luz_4 = psg.Image(self.lights_off, key='-LUZ4-')
        luz_5 = psg.Image(self.lights_off, key='-LUZ5-')

        luz_ok = psg.Image(self.lights_off, key='-LUZOK-', pad=(50, 0))
        luz_nook = psg.Image(self.lights_off, key='-LUZNOOK-', pad=(50, 0))

        luz_statusok = psg.Image(self.status_ok, key='-LUZSTATUSOK-')
        luz_statusnook = psg.Image(self.status_nook, key='-LUZSTATUSNOOK-')
        boton_start = psg.Image(self.start, key='-BOTONSTART-')
        boton_stop = psg.Image(self.stop, key='-BOTONSTOP-')

        p_verde = psg.Image(self.p_verde, key='-PVerde-', pad=(125,0), expand_x=True)
        p_naranja = psg.Image(self.p_naranja, key='-PNaranja-', pad=(0,0), expand_x=True)
        p_rosado1 = psg.Image(self.p_rosado, key='-PRosado1-', pad=(10,0), expand_x=True)
        p_rosado2 = psg.Image(self.p_rosado, key='-PRosado2-', pad=(125,0), expand_x=True)

        luz1_title = psg.Text(text='PASO 1', font=self.titles_font, text_color=self.titles_color, 
                              justification='center', pad=(20, 0))
        luz2_title = psg.Text(text='PASO 2', font=self.titles_font, text_color=self.titles_color, 
                              justification='center', pad=(25, 0))
        luz3_title = psg.Text(text='PASO 3', font=self.titles_font, text_color=self.titles_color, 
                              justification='center', pad=(25, 0))
        luz4_title = psg.Text(text='PASO 4', font=self.titles_font, text_color=self.titles_color, 
                              justification='center', pad=(25, 0))
        luz5_title = psg.Text(text='PASO 5', font=self.titles_font, text_color=self.titles_color, 
                              justification='center', pad=(20, 0))
        luzok_title = psg.Text(text='OK', font=self.titles_font, text_color=self.titles_color, 
                              justification='center', pad=(105, 0))
        luznook_title = psg.Text(text='NO OK', font=self.titles_font, text_color=self.titles_color, 
                              justification='center', pad=(80, 0))
        
        luz1_description = psg.Text(text='Limpieza\n cara interna', font=self.subtitles_font, text_color=self.titles_color, 
                              justification='center', pad=(30, 0))
        luz2_description = psg.Text(text='Limpieza\n cara externa', font=self.subtitles_font, text_color=self.titles_color, 
                              justification='center', pad=(45, 0))
        luz3_description = psg.Text(text='Aplicación\n primer horizontal', font=self.subtitles_font, text_color=self.titles_color, 
                              justification='center', pad=(0, 0))
        luz4_description =psg.Text(text='Aplicación\n primer vertical', font=self.subtitles_font, text_color=self.titles_color, 
                              justification='center', pad=(45, 0))
        luz5_description =psg.Text(text='Fotografía', font=self.subtitles_font, text_color=self.titles_color, 
                              justification='center', pad=(30, 0))

        body_photo = psg.Column([[foto]], expand_x=True, element_justification='left', expand_y=True)
        body_steps_panos = psg.Column([[p_naranja, p_verde, p_rosado1, p_rosado2]])
        body_steps_light = psg.Column([[luz1_title, luz2_title, luz3_title, luz4_title, luz5_title],
                                       [luz_1, luz_2, luz_3, luz_4, luz_5],
                                       [luz1_description, luz2_description, luz3_description, luz4_description, luz5_description],
                                       [body_steps_panos]], 
                                       expand_x=True, element_justification='center')
        body_steps_control = psg.Column([[luz_statusok, boton_start, boton_stop]], 
                                       expand_x=True, element_justification='center')
        body_steps_valid = psg.Column([[luzok_title, luznook_title],
                                       [luz_ok, luz_nook]], 
                                       expand_x=True, element_justification='center')
       

        layout = [banner,
                  [body_photo, body_steps_light],
                  [body_steps_control,body_steps_valid],
                  [footer]]

        window = psg.Window(self.title, layout, 
                    resizable=True, finalize=True,
                    no_titlebar=False, keep_on_top=False, margins=(0,0))
        
        window['-FOTO-'].update(data = ImageTk.PhotoImage(image=self.foto))
        self.update_banner(banner[0], width)
        window.maximize()
        return window
    
    def ejecutar(self, window):
        while True:
            event, values = window.read(timeout=50)
            if event == psg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                break
            paso = self.logica.leer_paso()
            self.logica.iluminar_paso(window, str(paso), self.lights_off, self.lights_on)
            self.logica.iluminar_validacion(window, str(paso), self.lights_off, self.lights_on, self.lights_error)
            if paso == '5':
                foto = self.logica.actualizar_foto(window, paso)
                self.logica.fecha_actualizacion()