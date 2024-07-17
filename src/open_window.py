import customtkinter as ctk
from tkinter import filedialog, messagebox
import json
from main import main
import threading
import os
from time import sleep

# Função para selecionar um diretório
def select_directory(entry):
    directory = filedialog.askdirectory()
    if directory:
        entry.set(directory)

def center_window(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int((screen_width - width) / 2)
    y = int((screen_height - height) / 2)
    root.geometry(f'{width}x{height}+{x}+{y}')

# Função para abrir a janela de configuração
def open_config_window():
    config_window = ctk.CTkToplevel(app)
    config_window.title("Configurações")
    config_window.grab_set()  # Torna a janela de configuração modal

    config_window.grid_rowconfigure(0, weight=1)
    config_window.grid_rowconfigure(1, weight=1)
    config_window.grid_rowconfigure(2, weight=1)
    config_window.grid_rowconfigure(3, weight=1)
    config_window.grid_rowconfigure(4, weight=1)
    config_window.grid_columnconfigure(0, weight=1)
    config_window.grid_columnconfigure(1, weight=1)
    config_window.grid_columnconfigure(2, weight=1)

    # Função para ler os caminhos do arquivo JSON
    def load_paths():
        try:
            with open('paths.json', 'r') as json_file:
                paths = json.load(json_file)
                return paths
        except FileNotFoundError:
            return {"input_path": "", "output_path": ""}

    # Carregar os caminhos do arquivo JSON
    paths = load_paths()

    # Campo para diretório de entrada
    input_path = ctk.StringVar(value=paths.get("input_path", ""))
    ctk.CTkLabel(config_window,
                 text="Diretório de Entrada",
                 font=('Segoe UI', 18),
                 ).grid(pady=5, column=1, row=0)
    input_entry = ctk.CTkEntry(config_window,
                               textvariable=input_path,
                               width=300,
                               height=30,
                               corner_radius=0,
                               )
    input_entry.grid(pady=5, padx=15, column=0, columnspan=2, row=1)
    ctk.CTkButton(config_window,
                  text="Escolher entrada",
                  command=lambda: select_directory(input_path),
                  fg_color='#0066ff',
                  hover_color='#0055cc',
                  corner_radius=0,
                  width=120,
                  height=30,
                  font=('Segoe UI', -14)
                  ).grid(pady=5, padx=15, column=3, row=1)

    # Campo para diretório de saída
    output_path = ctk.StringVar(value=paths.get("output_path", ""))
    ctk.CTkLabel(config_window,
                 text="Diretório de Saída",
                 font=('Segoe UI', 18),
                 ).grid(pady=5, row=2, column=1)
    output_entry = ctk.CTkEntry(config_window, textvariable=output_path, width=300)
    output_entry.grid(pady=5, padx=15, column=0, columnspan=2, row=3)
    ctk.CTkButton(config_window,
                  text="Escolher saída",
                  command=lambda: select_directory(output_path),
                  fg_color='#0066ff',
                  hover_color='#0055cc',
                  corner_radius=0,
                  width=120,
                  height=30,
                  font=('Segoe UI', -14)
                  ).grid(pady=5, padx=15, column=3, row=3)

    # Função para salvar os caminhos no arquivo JSON
    def save_paths():
        paths = {
            "input_path": input_path.get(),
            "output_path": output_path.get()
        }
        with open('paths.json', 'w') as json_file:
            json.dump(paths, json_file)
        messagebox.showinfo("Salvar", "Configurações salvas com sucesso!")
        config_window.destroy()  # Fecha a janela de configuração

    # Botão de salvar
    ctk.CTkButton(config_window,
                  text="Salvar",
                  command=save_paths,
                  fg_color='#0066ff',
                  hover_color='#0055cc',
                  corner_radius=0,
                  width=180,
                  height=40,
                  font=('Segoe UI', -18)
                  ).grid(pady=20, column=0, columnspan=4, row=4)

# Função para iniciar o processamento
def start_processing():
    settings_button.configure(state='disabled')
    process_button.configure(state='disabled')
    threading.Thread(target=main).start()
    threading.Thread(target=start_update_thread).start()

def start_update_thread():

    input_path = paths['input_path']
    temp_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'temp').replace(r'\src', '')



    files_input = len(os.listdir(input_path)) * 2
    files_temp = len(os.listdir(temp_path))

    while files_temp != (files_input/2):
        percentage = files_temp / files_input
        progressbar.set(percentage)
        app.update_idletasks()
        files_temp = len(os.listdir(temp_path))
        sleep(0.2)
    
    files_input = len(os.listdir(input_path))
    while files_temp >= 0:
        try:
            percentage = 0.5 + 0.5 * (1 - (files_temp / files_input))
            progressbar.set(percentage)
            app.update_idletasks()
            if files_temp == 0:
                messagebox.showinfo("Confirmação", f"Cartas geradas com sucesso!")
                progressbar.set(0)
                settings_button.configure(state='normal')
                process_button.configure(state='normal')
                return
            files_temp = len(os.listdir(temp_path))
            sleep(0.2)

        except ZeroDivisionError:
            messagebox.showinfo("ERRO!", f"Não há imagens para processar na pasta de entrada.\nVerifique e tente novamente.")
            settings_button.configure(state='normal')
            process_button.configure(state='normal')
            return

# Configuração da janela principal
app = ctk.CTk()
app.title("Nomeador de Cartas")
center_window(app, 500, 320)

# Configurar a grade da janela
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)
app.grid_rowconfigure(2, weight=1)
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(2, weight=1)

# Botão no canto superior esquerdo
settings_button = ctk.CTkButton(app, text="CONFIGURAÇÕES",
                                command=open_config_window,
                                fg_color='#0066ff',
                                hover_color='#0055cc',
                                corner_radius=0,
                                width=120,
                                height=30,
                                font=('Segoe UI', -12))
settings_button.grid(row=0, column=0, sticky='nw', pady=10, padx=10)

# Botão centralizado
process_button = ctk.CTkButton(app, text="PROCESSAR", 
                              command=start_processing,
                              fg_color='#0066ff',
                              hover_color='#0055cc',
                              corner_radius=0,
                              width=250,
                              height=50,
                              font=('Segoe UI', -22))
process_button.grid(row=1, column=0, columnspan=3, pady=0, padx=0)

progressbar = ctk.CTkProgressBar(app, orientation="horizontal",
                                 height=25,
                                 corner_radius=0,
                                 progress_color='#0066ff',
                                 mode='determinate')

progressbar.set(0)
progressbar.grid(row=2, column=0, columnspan=4, sticky='ews', padx=0, pady=0)

# Carregar os caminhos do arquivo JSON ao iniciar
paths = {}
try:
    with open('paths.json', 'r') as json_file:
        paths = json.load(json_file)
except FileNotFoundError:
    pass

app.mainloop()
