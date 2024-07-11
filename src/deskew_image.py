import cv2
import numpy as np

def deskew_image(image_path, output_path):
    # Ler a imagem
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detectar bordas
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    # Detectar linhas usando Transformada de Hough
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=100, maxLineGap=10)
    
    # Calcular o ângulo de inclinação médio
    angles = []
    for line in lines:
        x1, y1, x2, y2 = line[0]
        angle = np.degrees(np.arctan2(y2 - y1, x2 - x1))
        angles.append(angle)
    
    median_angle = np.median(angles)
    
    # Rotacionar a imagem para corrigir a inclinação
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, median_angle, 1.0)
    rotated = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

    # Salvar a imagem corrigida
    cv2.imwrite(output_path, rotated)

# Exemplo de uso
image_path = r'C:\Users\rcorreia\Documents\code-reader\temp\LT_001.jpeg'
output_path = r'C:\Users\rcorreia\Documents\cartas\pagina_corrigida.jpg'
deskew_image(image_path, output_path)

# Mostrar a imagem corrigida
corrected_img = cv2.imread(output_path)
cv2.imshow('Imagem Corrigida', corrected_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
