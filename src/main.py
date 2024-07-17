from read_images import get_image_paths_from_folder, InvalidFormat, OnlyOneFileInSourceFolderError
from resize_and_save_image import resize_and_save_image
import os
from get_code import get_code
from is_folder_empty import is_folder_empty
from delete_files_in_directory import delete_files_in_directory
import json

def get_paths(json_path):
    with open(json_path, 'r') as json_file:
        input_path = json.load(json_file)

    return input_path

def main():
    json_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + r'\paths.json'

    paths = get_paths(json_path)

    images_path_list = []
    temp_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'temp').replace(r'\src', '')

    images_path = get_image_paths_from_folder(paths['input_path'])
    counter = 1

    try:
        for path in images_path:
            output_path = temp_path + r'\LT_00' + f'{counter}.jpeg'  
            images_path_list.append(output_path)
            resize_and_save_image(path, output_path)

            counter += 1

        c = 0
        while not is_folder_empty(temp_path):   
            images = get_code(images_path_list)
            images_path_list = images_path_list[images:]
            c += 1

        delete_files_in_directory(paths['input_path'])
    
    except InvalidFormat as e:
        raise InvalidFormat(str(e))

    except OnlyOneFileInSourceFolderError as e:
        raise OnlyOneFileInSourceFolderError(str(e))
