import os

def is_folder_empty(folder_path):
    # Verifica se a lista de arquivos e subpastas está vazia
    return len(os.listdir(folder_path)) == 0
