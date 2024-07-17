import os
from natsort import natsorted

class InvalidFormat(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class OnlyOneFileInSourceFolderError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def get_image_paths_from_folder(folder_path):
    # Definir extensões de arquivos de imagem válidos
    valid_extensions = ['.jpg', '.jpeg']

    # Listar todos os arquivos no diretório
    files = os.listdir(folder_path)

    # Filtrar arquivos para manter apenas imagens e obter os caminhos completos
    image_files = [os.path.join(folder_path, f) for f in files if any(f.lower().endswith(ext) for ext in valid_extensions)]

    if len(image_files) == 0:
        raise InvalidFormat('Os arquivos não estão em formato JPEG.')
    
    if len(image_files) == 1:
        raise OnlyOneFileInSourceFolderError('Há apenas um único arquivo na sua pasta de origem')
    
    # Classificar os arquivos numericamente
    image_files = natsorted(image_files)

    return image_files

# Exemplo de uso
# folder_path = r"C:\Users\rcorreia\Documents\cartas"
# images = get_image_paths_from_folder(folder_path)

# print(images)