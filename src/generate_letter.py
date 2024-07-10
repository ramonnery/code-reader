from PIL import Image
import os

def generate_letter(images_path, code, output_path):
    images = []
    final_name = os.path.join(output_path, f'{code}.pdf')
    for image_path in images_path:
        image = Image.open(image_path)
        image = image.convert('RGB')
        images.append(image)

    if images: 
        images[0].save(final_name, save_all=True, append_images=images[1:])
    
    delete_files(images_path)
    

def delete_files(images_path):
    for file in images_path:
        try:
            os.remove(file)
        except OSError as e:
            print(f"Erro ao deletar o arquivo {file}: {e}")