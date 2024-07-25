from cv2 import cvtColor, Canny, HoughLinesP, getRotationMatrix2D, warpAffine, INTER_CUBIC, BORDER_REPLICATE, COLOR_BGR2GRAY

import numpy as np

def deskew_image(img):
    gray = cvtColor(img, COLOR_BGR2GRAY)

    # Detectar bordas
    edges = Canny(gray, 50, 150, apertureSize=3)

    # Detectar linhas usando Transformada de Hough
    lines = HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=100, maxLineGap=10)
    
    # Calcular o ângulo de inclinação médio
    angles = []
    for line in lines:
        x1, y1, x2, y2 = line[0]
        angle = np.degrees(np.arctan2(y2 - y1, x2 - x1))
        angles.append(angle)
    
    if len(angles) > 0:
        median_angle = np.median(angles)
    else:
        median_angle = 0
    
    # Rotacionar a imagem para corrigir a inclinação
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)
    M = getRotationMatrix2D(center, median_angle, 1.0)
    rotated = warpAffine(img, M, (w, h), flags=INTER_CUBIC, borderMode=BORDER_REPLICATE)

    return rotated