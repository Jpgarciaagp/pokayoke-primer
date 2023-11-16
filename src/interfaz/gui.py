import PySimpleGUI as psg
import datetime as dt
from PIL import ImageTk

class AppPrimer:    
    def __init__(self, logo, title, width, height, logica, lights_off, lights_on, lights_error, start, stop, status_ok, status_nook, p_naranja, p_rosado, p_verde):
        self.logica = logica
        self.banner_font = ("Segoe UI", 28, "bold")
        self.default_font = ("Segoe UI", 16)
        self.titles_font = ("Segoe UI", 17, "bold")
        self.subtitles_font = ("Segoe UI", 10)
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
        self.width = width
        self.height = height
        
        self.window = self.construct_window()        
    
    def update_banner(self, banner):
        banner.erase()
        banner.DrawText(self.title,(self.width/4,50),color='white', font=self.banner_font)
        banner.DrawImage(filename=self.logo, location=(20,0))
        banner.DrawText(self.logica.fecha_actualizacion(), (self.width/2.15, 35), color='white', font=self.update_font)
        banner.DrawText('Actualización', (self.width/2.15, 60),color='white',font=self.update_font)
    

    def construct_window(self):
        new_theme = {"BACKGROUND": self.bg_color, "TEXT": psg.COLOR_SYSTEM_DEFAULT, "INPUT": psg.COLOR_SYSTEM_DEFAULT,
             "TEXT_INPUT": psg.COLOR_SYSTEM_DEFAULT, "SCROLL": psg.COLOR_SYSTEM_DEFAULT,
             "BUTTON": psg.OFFICIAL_PYSIMPLEGUI_BUTTON_COLOR, "PROGRESS": psg.COLOR_SYSTEM_DEFAULT, "BORDER": 1,
             "SLIDER_DEPTH": 1, "PROGRESS_DEPTH": 0
             }
        psg.theme_add_new('AGP', new_theme)
        psg.theme('AGP')
        
        banner = [psg.Graph(canvas_size=(self.width,100), graph_bottom_left=(0,100), graph_top_right=(self.width/2,0), 
                            expand_x=True, background_color=self.banner_color, key='-BANNER-')] # Banner should always have 100px height
        
        footer = [psg.Graph(canvas_size=(self.width,50), graph_bottom_left=(0,self.height), 
        graph_top_right=(self.width/2,(self.height-50)), 
                            expand_x=True, background_color=self.banner_color)] # Footer should always have 50px height

        foto = psg.Image(background_color=self.bg_color, key='-FOTO-', pad=((50,0), (70,0)))
        luz_1 = psg.Image(self.lights_off, key='-LUZ1-')
        luz_2 = psg.Image(self.lights_off, key='-LUZ2-')
        luz_3 = psg.Image(self.lights_off, key='-LUZ3-')
        luz_4 = psg.Image(self.lights_off, key='-LUZ4-')
        luz_5 = psg.Image(self.lights_off, key='-LUZ5-')

        luz_ok = psg.Image(self.lights_off, key='-LUZOK-', pad=((156, 0), (0,0)))
        luz_nook = psg.Image(self.lights_off, key='-LUZNOOK-', pad=((135, 0), (0,0)))

        luz_statusok = psg.Image(self.status_ok, key='-LUZSTATUS-', pad=((55, 0), (0,0)))
        boton_start = psg.Button(image_filename=self.start, key='START', pad=((5, 0), (0,0)), button_color=self.bg_color, border_width=0, mouseover_colors=self.bg_color)
        boton_stop = psg.Button(image_filename=self.stop, key='RESET', pad=((5, 0), (0,0)), button_color=self.bg_color, border_width=0, mouseover_colors=self.bg_color)

        p_verde1 = psg.Image(self.p_verde, key='-PVerde1-', pad=((50,0), (0,40)))
        p_verde2 = psg.Image(self.p_verde, key='-PVerde2-', pad=((100,0), (0,40)))
        p_rosado1 = psg.Image(self.p_rosado, key='-PRosado1-', pad=((100,0), (0,40)))
        p_rosado2 = psg.Image(self.p_rosado, key='-PRosado2-', pad=((100,0), (0,40)))

        luz1_title = psg.Text(text='PASO 1', font=self.titles_font, text_color=self.titles_color, 
                              justification='center', pad=((25,0), (0,0)))
        luz2_title = psg.Text(text='PASO 2', font=self.titles_font, text_color=self.titles_color, 
                              justification='center', pad=((40,0), (0,0)))
        luz3_title = psg.Text(text='PASO 3', font=self.titles_font, text_color=self.titles_color, 
                              justification='center', pad=((40,0), (0,0)))
        luz4_title = psg.Text(text='PASO 4', font=self.titles_font, text_color=self.titles_color, 
                              justification='center', pad=((40,0), (0,0)))
        luz5_title = psg.Text(text='PASO 5', font=self.titles_font, text_color=self.titles_color, 
                              justification='center', pad=((40,0), (0,0)))
        
        luzok_title = psg.Text(text='OK', font=self.titles_font, text_color=self.titles_color, 
                              justification='center', pad=((200, 0), (0,0)))
        luznook_title = psg.Text(text='NO OK', font=self.titles_font, text_color=self.titles_color, 
                              justification='center', pad=((200, 0), (0,0)))
        
        luz1_description = psg.Text(text='Limpieza\n cara interna', font=self.subtitles_font, text_color=self.titles_color, 
                              justification='center', pad=((30,0), (0,10)))
        luz2_description = psg.Text(text='Limpieza\n cara externa', font=self.subtitles_font, text_color=self.titles_color, 
                              justification='center', pad=((45,0), (0,10)))
        luz3_description = psg.Text(text='Aplicación\n primer horizontal', font=self.subtitles_font, text_color=self.titles_color, 
                              justification='center', pad=((30,0), (0,10)))
        luz4_description =psg.Text(text='Aplicación\n primer vertical', font=self.subtitles_font, text_color=self.titles_color, 
                              justification='center', pad=((25,0), (0,10)))
        luz5_description =psg.Text(text='Fotografía', font=self.subtitles_font, text_color=self.titles_color, 
                              justification='center', pad=((45,0), (0,10)))
        
        status_description = psg.Text(text='Sistema', font=self.titles_font, text_color=self.titles_color, 
                              justification='center', pad=((75,0),(0,0)))
        inicio_description = psg.Text(text='LOREM', font=self.subtitles_font, text_color=self.titles_color, 
                              justification='center', pad=((75,0),(0,0)), key='-TIEMPOINICIO-')

        body_col_izquierda = psg.Column([[foto], 
                                         [luz_statusok, boton_start, boton_stop], 
                                         [status_description, inicio_description]],
                                        element_justification = 'left',
                                        size=(500,570)
        )
        body_col_derecha = psg.Column([[luz1_title, luz2_title, luz3_title, luz4_title, luz5_title],
                                       [luz_1, luz_2, luz_3, luz_4, luz_5],
                                       [luz1_description, luz2_description, luz3_description, luz4_description, luz5_description],
                                       [p_verde1, p_verde2, p_rosado1, p_rosado2],
                                       [luzok_title, luznook_title],
                                       [luz_ok, luz_nook]],
                                       element_justification = 'left',
                                       expand_x = True)
       

        layout = [banner,
                  [body_col_izquierda, body_col_derecha],
                  [footer]]

        window = psg.Window(self.title, layout, 
                    resizable=False, finalize=True,
                    no_titlebar=False, keep_on_top=False, margins=(0,0))
        
        window['-FOTO-'].update(data = ImageTk.PhotoImage(image=self.foto))
        #window.maximize()
        self.update_banner(banner[0])
        return window
    
    def ejecutar(self, window):
        while True:
            event, values = window.read(timeout=50)
            if event == psg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                break
            if event == 'START':
                self.logica.start_button()
            if event == 'RESET':
                self.logica.reset_button()
            paso = self.logica.leer_paso()
            self.logica.iluminar_paso(window, str(paso), self.lights_off, self.lights_on)
            self.logica.iluminar_validacion(window, str(paso), self.lights_off, self.lights_on, self.lights_error)
            self.logica.actualizar_horainicio(window)
            self.logica.status_sistema(window, self.status_ok, self.status_nook)
            if paso == '5':
                self.logica.actualizar_foto(window, paso)
                self.update_banner(window['-BANNER-'])
                