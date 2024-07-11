import os

def is_folder_empty(folder_path):
    # Verifica se a lista de arquivos e subpastas está vazia
    return len(os.listdir(folder_path)) == 0


r = is_folder_empty(r'C:\Users\rcorreia\Documents\nomeadas')
print(r)