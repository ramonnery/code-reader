from customtkinter import *
from tkinter.filedialog import askdirectory
import json

paths = {
    'path_input': '',
    'path_output': ''
}

def get_path_folder_input(dialog):
    dialog.attributes('-topmost', False)  # Desativa o atributo 'topmost' da janela de diálogo
    path_folder_input = askdirectory(title='Escolha uma pasta')
    paths['path_input'] = path_folder_input
    print(paths['path_input'])
    dialog.attributes('-topmost', True)   # Reativa o atributo 'topmost' da janela de diálogo

def get_path_folder_output(dialog):
    dialog.attributes('-topmost', False)  # Desativa o atributo 'topmost' da janela de diálogo
    path_folder_input = askdirectory(title='Escolha uma pasta')
    paths['path_output'] = path_folder_input
    print(paths['path_output'])
    dialog.attributes('-topmost', True)   # Reativa o atributo 'topmost' da janela de diálogo

def save_json(window):
    with open('./paths.json', 'w') as json_file:
        json.dump(paths, json_file, indent=4)
    print('dicionário salvo!')
    
    window.attributes('-disabled', False)  # Reabilita a janela principal

def open_dialog(window):
    window.attributes('-disabled', True)  # Desabilita a janela principal
    dialog = CTk()
    dialog.title('CONFIGURAÇÕES')
    dialog.geometry('280x140')

    button_input = CTkButton(
        dialog,
        text='ENTRADA',
        command=lambda: get_path_folder_input(dialog)
    )
    button_input.pack()

    button_output = CTkButton(
        dialog,
        text='SAÍDA',
        command=lambda: get_path_folder_output(dialog)
    )
    button_output.pack()

    button_save = CTkButton(
        dialog,
        text='SALVAR',
        command=lambda: save_json(dialog, window)
    )
    button_save.pack()
    dialog.mainloop()
