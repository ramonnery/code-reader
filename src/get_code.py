import cv2
import pytesseract as pt
from is_valid_code import is_valid_code
from to_name import to_name

# pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' # em casa
pt.pytesseract.tesseract_cmd = r'C:\Users\rcorreia\AppData\Local\Programs\Tesseract-OCR/tesseract.exe'

def get_code(images_path_list):
    x1, y1 = 839, 353  # Coordenadas do canto superior esquerdo
    x2, y2 = 1466, 527  # Coordenadas do canto inferior direito
    codes_list = []
    
    for image_path in images_path_list:
        img = cv2.imread(image_path)

        # Verificar se as coordenadas são válidas
        if x1 < 0 or y1 < 0 or x2 > img.shape[1] or y2 > img.shape[0]:
            print("As coordenadas da ROI estão fora dos limites da imagem.")
        else:
            # Recortar a ROI da imagem
            roi = img[y1:y2, x1:x2]

            # # Mostrar a ROI (opcional)
            # cv2.imshow("ROI", roi)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            
            # Extrair texto da ROI usando Tesseract
            code = pt.image_to_string(roi).replace("\n", "").replace(' ', '')
            print("Texto extraído da ROI:")
            print(code)
            code = is_valid_code(code)

            if code:
                new_code = to_name(code)
                codes_list.append(new_code)

            #     else:
            #         break

            # else:
            #     continue

    return codes_list


