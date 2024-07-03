import cv2

# Função de callback do mouse
def select_roi(event, x, y, flags, param):
    global x1, y1, x2, y2, cropping

    # Se o botão esquerdo do mouse foi clicado, registre o ponto inicial (x1, y1)
    if event == cv2.EVENT_LBUTTONDOWN:
        x1, y1 = x, y
        cropping = True

    # Se o mouse está em movimento e estamos no meio de um corte, registre o ponto final (x2, y2)
    elif event == cv2.EVENT_MOUSEMOVE:
        if cropping:
            x2, y2 = x, y

    # Se o botão esquerdo do mouse foi solto, registre o ponto final (x2, y2) e finalize o corte
    elif event == cv2.EVENT_LBUTTONUP:
        x2, y2 = x, y
        cropping = False
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.imshow("image", image)

# Carregar a imagem
image = cv2.imread(r'C:\Users\hercu\OneDrive\Documentos\cartas-juntas\nova-img.jpg')
clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", select_roi)

print("Selecione a região de interesse (ROI) e pressione 'c' para confirmar ou 'r' para redefinir")

# Inicializar as coordenadas e a variável de corte
x1, y1, x2, y2 = -1, -1, -1, -1
cropping = False

while True:
    cv2.imshow("image", image)
    key = cv2.waitKey(1) & 0xFF

    # Pressione 'r' para redefinir a seleção da ROI
    if key == ord("r"):
        image = clone.copy()

    # Pressione 'c' para confirmar a seleção da ROI
    elif key == ord("c"):
        break

cv2.destroyAllWindows()

# Exibir as coordenadas da ROI
print(f"Coordenadas da ROI: ({x1}, {y1}) até ({x2}, {y2})")

# Cortar a ROI e exibir
if x1 != -1 and y1 != -1 and x2 != -1 and y2 != -1:
    roi = clone[y1:y2, x1:x2]
    cv2.imshow("ROI", roi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
