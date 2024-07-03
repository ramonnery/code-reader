from read_images import get_image_paths_from_folder
from resize_and_save_image import resize_and_save_image

folder_path = r'C:\Users\hercu\OneDrive\Imagens\erros-estranhos'
images_path = get_image_paths_from_folder(folder_path)
temp_path = '../temp'
counter = 1

for image_path in images_path:
    new_lt = '/LT_00' + str(counter)
    output_path = temp_path + new_lt

    resize_and_save_image(image_path, output_path)

    counter += 1