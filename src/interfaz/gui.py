import PySimpleGUI as psg
import datetime as dt

class AppPrimer:
    
    def __init__(self, logo, title, width, height, logica):
        self.logica = logica
        self.banner_font = ("Segoe UI", 28, "bold")
        self.default_font = ("Segoe UI", 16)
        self.titles_font = ("Segoe UI", 20, "bold")
        self.update_font = ("Segoe UI", 12)
        self.bg_color = '#eef5f6'
        self.banner_color = '#8fc5cf'
        self.title = title
        self.logo = logo
        self.window = self.construct_window(width, height)
    
    def update_banner(self, banner, update_time, width):
        banner.erase()
        banner.DrawText(self.title,(width/3.6,50),color='white',font=self.banner_font)
        banner.DrawImage(filename=self.logo, location=(20,0))
        banner.DrawText(dt.datetime.now().strftime('%Y-%m-%d %H:%M'), (width/2.2, 35), color='white', font=self.update_font)
        banner.DrawText(update_time, (width/2.2, 60),color='white',font=self.update_font)
    
    def generate_matrix(self, numrows:int, numcols:int, prefix:str):
        matrix = []
        for i in range(numrows):
            row = []
            for j in range(numcols):
                column = psg.Column([], background_color=self.bg_color, key=f'{prefix}-{i}{j}', element_justification='center', expand_x=True)
                row.append(column)
            matrix.append(row)
        return matrix

    def construct_window(self, width, height):
        banner = [psg.Graph(canvas_size=(width,100), graph_bottom_left=(0,100), graph_top_right=(width/2,0), 
                            expand_x=True, background_color=self.banner_color)] # Banner should always have 100px height
        
        footer = [psg.Graph(canvas_size=(width,50), graph_bottom_left=(0,height), 
        graph_top_right=(width/2,(height-50)), 
                            expand_x=True, background_color=self.banner_color)] # Footer should always have 50px height

        body_photo = self.generate_matrix(1, 1, 'fotos')
        body_steps = self.generate_matrix(1, 5, 'pasos')
        body_valid = self.generate_matrix(1, 2, 'valid')

        layout = [banner,
                  [body_photo, body_steps],
                  [body_valid],
                  [psg.Button('Cancel')],
                  [footer]         
        ]

        window = psg.Window(self.title, layout, 
                    background_color=self.bg_color, resizable=True, finalize=True,
                    no_titlebar=False, keep_on_top=True, margins=(0,0))
        return window
    
    def ejecutar(self, window):
        while True:
            event, values = window.read(timeout=50)
            if event == psg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                break
            paso = self.logica.leer_paso()