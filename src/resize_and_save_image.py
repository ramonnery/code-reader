import cv2
from deskew_image import deskew_image

def resize_and_save_image(image_path, output_path):
    target_width = 2481
    target_height = 3507

    # Carregar a imagem
    image = cv2.imread(image_path)

    # Verificar se a imagem foi carregada corretamente
    if image is None:
        print(f"Erro ao carregar a imagem em {image_path}")
        return None

    # Redimensionar a imagem
    resized_image = cv2.resize(image, (target_width, target_height), interpolation=cv2.INTER_AREA)

    # Salvar a imagem redimensionada
    success = cv2.imwrite(output_path, resized_image)
    if success:
        print(f"Imagem redimensionada salva em: {output_path}")
    else:
        print("Erro ao salvar a imagem redimensionada.")
    return success
    



# Exemplo de uso
# image_path = r'C:\Users\hercu\OneDrive\Documentos\cartas-juntas\teste.jpg'

# output_path = r'C:\Users\hercu\OneDrive\Documentos\cartas-juntas\nova-img.jpg'

# success = resize_and_save_image(image_path, output_path)

# if success:
#     print("Imagem redimensionada e salva com sucesso!")
# else:
#     print("Erro ao redimensionar e salvar a imagem.")
