from read_images import get_image_paths_from_folder, InvalidFormat, OnlyOneFileInSourceFolderError
from resize_and_save_image import resize_and_save_image
import os
from get_code import get_code
from is_folder_empty import is_folder_empty
from delete_files_in_directory import delete_files_in_directory
from load_paths import load_paths
import ctypes
from pathlib import Path


def main():
    path_json = load_paths()
    temp_folder = Path(path_json['input_path']).parent / 'temp'
    os.makedirs(temp_folder, exist_ok=True)
    FILE_ATTRIBUTE_HIDDEN = 0x02
    temp_folder = str(temp_folder)
    # Converte o caminho para o formato de bytes necessário para SetFileAttributesW
    path_bytes = temp_folder.encode('utf-16le')

    # Define o atributo "oculto" usando ctypes
    ctypes.windll.kernel32.SetFileAttributesW(path_bytes, FILE_ATTRIBUTE_HIDDEN)

    images_path_list = []

    images_path = get_image_paths_from_folder(path_json['input_path'])
    counter = 1

    try:
        for path in images_path:
            output_path = temp_folder + r'\LT_00' + f'{counter}.jpeg'  
            images_path_list.append(output_path)
            resize_and_save_image(path, output_path)

            counter += 1

        c = 0
        while not is_folder_empty(temp_folder):   
            images = get_code(images_path_list)
            images_path_list = images_path_list[images:]
            c += 1

        delete_files_in_directory(path_json['input_path'])
    
    except InvalidFormat as e:
        raise InvalidFormat(str(e))

    except OnlyOneFileInSourceFolderError as e:
        raise OnlyOneFileInSourceFolderError(str(e))

