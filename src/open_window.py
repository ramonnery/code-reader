from open_dialog import open_dialog
from customtkinter import *

def open_window():
    set_appearance_mode("dark")
    window = CTk()
    window.title('Nomeador de Cartas')
    window.geometry("400x250")

    bold_font_button_settings = CTkFont(family='Segoe UI', size=10, weight='bold')
    button_settings = CTkButton(
        window, 
        text='CONFIGURAÇÕES',
        fg_color='#2964F6',
        corner_radius=0,
        font=bold_font_button_settings,
        text_color='#e0e0e0',
        width=100,
        command=lambda: open_dialog(window)
        )
    button_settings.grid(row=0, column=0)

    bold_font_button_process = CTkFont(family='Segoe UI', size=20, weight='bold')
    button_process = CTkButton(
        window,
        text='PROCESSAR',
        corner_radius=0,
        fg_color='#2964F6',
        font=bold_font_button_process,
        text_color='#e0e0e0'
        )
    button_process.grid(row=1, column=2, sticky='n')
    window.mainloop()