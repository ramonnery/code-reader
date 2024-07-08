from PIL import Image
import os
def generate_letter(images_path, code, output_path):
    images = []

    for image_path in images_path:
        image = Image.open(image_path)
        image. image.covert('RGB')
        images.append(image)

    if images: 
        images[0].save(output_path, salve_all=True, append_images=images[1:])