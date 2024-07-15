from read_images import get_image_paths_from_folder
from resize_and_save_image import resize_and_save_image
import os
from get_code import get_code
from is_folder_empty import is_folder_empty

def main():
    paths = {
        'path_input': r"C:\Users\rcorreia\Documents\cartas",
        'path_output': "C:/Users/hercu/Videos/Captures"
    }

    images_path_list = []
    temp_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'temp').replace(r'\src', '')

    images_path = get_image_paths_from_folder(paths['path_input'])
    counter = 1


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

    # print(f'TOTAL: {c}')
# print(codes_list)
# print(len(codes_list))

main()