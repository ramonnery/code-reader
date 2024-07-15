import customtkinter as ctk
from tkinter import filedialog, messagebox
import json
from main import main
import threading


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
    ctk.CTkLabel(config_window, text="Diretório de Entrada:").pack(pady=5)
    input_entry = ctk.CTkEntry(config_window, textvariable=input_path, width=300)
    input_entry.pack(pady=5)
    ctk.CTkButton(config_window, text="Input", command=lambda: select_directory(input_path)).pack(pady=5)

    # Campo para diretório de saída
    output_path = ctk.StringVar(value=paths.get("output_path", ""))
    ctk.CTkLabel(config_window, text="Diretório de Saída:").pack(pady=5)
    output_entry = ctk.CTkEntry(config_window, textvariable=output_path, width=300)
    output_entry.pack(pady=5)
    ctk.CTkButton(config_window, text="Output", command=lambda: select_directory(output_path)).pack(pady=5)

    # Função para salvar os caminhos no arquivo JSON
    def save_paths():
        paths = {
            "input_path": input_path.get(),
            "output_path": output_path.get()
        }
        with open('paths.json', 'w') as json_file:
            json.dump(paths, json_file)
        messagebox.showinfo("Salvar", "Configurações salvas!")
        config_window.destroy()  # Fecha a janela de configuração

    # Botão de salvar
    ctk.CTkButton(config_window, text="Salvar", command=save_paths).pack(pady=20)

# Função para iniciar o processamento
def start_processing():
    # Limpar a janela principal e exibir a barra de progresso
    for widget in app.winfo_children():
        widget.destroy()
    
    progress_bar = ctk.CTkProgressBar(app, width=300)
    progress_bar.pack(pady=20)
    progress_bar.set(0)

    # Atualizar a barra de progresso
    def update_progress():
        # Chamar a função main() em um thread separado para não bloquear a GUI
        main_thread = threading.Thread(target=main)
        main_thread.start()

        # Função para atualizar a barra de progresso enquanto a função main() é executada
        def check_progress():
            if main_thread.is_alive():
                # Atualiza o valor da barra de progresso baseado no progresso da função main()
                progress = main.get_progress()  # Supondo que main() tenha um método get_progress()
                progress_bar.set(progress)
                app.after(100, check_progress)
            else:
                # Quando main() terminar, destrói a barra de progresso e retorna à tela inicial
                progress_bar.destroy()
                ctk.CTkButton(app, text="Configurações", command=open_config_window).pack(pady=20)
                ctk.CTkButton(app, text="Processar", command=start_processing).pack(pady=20)

        # Inicia a verificação do progresso
        check_progress()

    # Inicia a atualização da barra de progresso
    update_progress()

# Configuração da janela principal
app = ctk.CTk()
app.title("Nomeador de Cartas")
center_window(app, 500, 400)

# Botões principais
ctk.CTkButton(app, text="Configurações", command=open_config_window).pack(side=ctk.LEFT, pady=20, padx=50)
ctk.CTkButton(app, text="Processar", command=start_processing).pack(side=ctk.LEFT, pady=20, padx=50)

# Carregar os caminhos do arquivo JSON ao iniciar
paths = {}
try:
    with open('paths.json', 'r') as json_file:
        paths = json.load(json_file)
except FileNotFoundError:
    pass

app.mainloop()
