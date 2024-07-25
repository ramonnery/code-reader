import json
import os

def load_paths():
    file_path = './paths.json'
    
    # Verificar se o arquivo existe antes de tentar abrir
    if not os.path.exists(file_path):
        # Se não existir, cria o arquivo com o conteúdo padrão
        default_paths = {"input_path": "", "output_path": "", "tesseract_path": ""}
        with open(file_path, 'w') as json_file:
            json.dump(default_paths, json_file, indent=4)
        return default_paths
    
    # Se o arquivo existe, faz a leitura
    try:
        with open(file_path, 'r') as json_file:
            paths = json.load(json_file)
            return paths
    except Exception as e:
        # Lidar com outros possíveis erros (ex.: erro de leitura)
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
        return {"input_path": "", "output_path": "", "tesseract_path": ""}
