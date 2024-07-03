import cv2
import pytesseract as pt

pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread(r'C:\Users\hercu\OneDrive\Imagens\erros-estranhos\1.jpg')

x1, y1 = 893, 438  # Coordenadas do canto superior esquerdo
x2, y2 = 1444, 564  # Coordenadas do canto inferior direito

# Verificar se as coordenadas são válidas
if x1 < 0 or y1 < 0 or x2 > img.shape[1] or y2 > img.shape[0]:
    print("As coordenadas da ROI estão fora dos limites da imagem.")
else:
    # Recortar a ROI da imagem
    roi = img[y1:y2, x1:x2]

    # Mostrar a ROI (opcional)
    cv2.imshow("ROI", roi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # Extrair texto da ROI usando Tesseract
    text = pt.image_to_string(roi)
    print("Texto extraído da ROI:")
    print(text)