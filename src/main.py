from read_images import get_image_paths_from_folder
from resize_and_save_image import resize_and_save_image
from open_window import open_window
import os
from get_code import get_code

# open_window()

# def get_update_json():
#     with open('paths.json', 'r') as json_file:
#         paths = json.load(json_file)
#     return paths


# paths = get_update_json()

paths = {
    'path_input': r"C:\Users\rcorreia\Documents\cartas",
    'path_output': "C:/Users/hercu/Videos/Captures"
}

images_path_list = []

images_path = get_image_paths_from_folder(paths['path_input'])
temp_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'temp').replace(r'\src', '')
counter = 1

for path in images_path:
    output_path = temp_path + r'\LT_00' + f'{counter}.jpeg'  
    images_path_list.append(output_path)
    resize_and_save_image(path, output_path)

    counter += 1

codes_list = get_code(images_path_list)

print(codes_list)
print(len(codes_list))
