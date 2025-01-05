import cv2
import numpy as np
from PIL import Image
from scipy.ndimage import label

#==================== FUNÇÕES CHAMADAS DIRETAMENTE PELAS QUESTÕES ================= 
#==================== Aplicação de Máscara Genérica para questão 2
def mascara(imagem, kernel, peso):
    linhas, colunas = imagem.shape
    resultado = np.copy(imagem)

    for i in range(1, linhas - 1):
        for j in range(1, colunas - 1):
            janela = imagem[i - 1:i + 2, j - 1:j + 2]
            resultado_pixel = np.sum(janela * kernel)
            resultado[i, j] = resultado_pixel//peso

    return resultado

#==================== Função de dilatação para Questão 4
def dilatar (img, kernel, center):
    img_h, img_w = img.shape
    se_h, se_w = kernel.shape
    resultado = np.zeros_like(img)

    for i in range(img_h):
        for j in range(img_w):
            
            if img[i, j] == 255:
                for m in range(se_h):
                    for n in range(se_w):
                        y = i + (m - center[0])
                        x = j + (n - center[1])

                        if 0 <= y < img_h and 0 <= x < img_w:
                            if kernel[m, n] == 1:
                                resultado[y, x] = 255 
                                
    resultado = np.clip(resultado, 0, 255)
    return resultado

#==================== Função de erosão para Questão 4
def erodir (img, kernel, center):
    img_h, img_w = img.shape
    se_h, se_w = kernel.shape
    resultado = np.zeros_like(img)

    for i in range(img_h):
        for j in range(img_w):
            is_eroded = True
            for m in range(se_h):
                for n in range(se_w):
                    y = i + (m - center[0])
                    x = j + (n - center[1])

                    if 0 <= y < img_h and 0 <= x < img_w:
                        if kernel[m, n] == 1 and img[y, x] != 255:
                            is_eroded = False
                    else:
                        if kernel[m, n] == 1:
                            is_eroded = False

            if is_eroded:
                resultado[i, j] = 255
    return resultado

#==================== Preenchimento de Buracos na Imagem colorida para questão 5.A e 5.C
def preencher(R, G, B, r, g, b):
    N = receba(R, G, B, r, g, b)
    Complemento = 1 - N
    h, w = N.shape
    F = np.zeros((h, w), dtype=np.uint8)

    F[0, :] = 1 - N[0, :]
    F[-1, :] = 1 - N[-1, :]
    F[:, 0] = 1 - N[:, 0]
    F[:, -1] = 1 - N[:, -1]

    bb = np.ones((3, 3), dtype=np.uint8)
    F_dilatado = F.copy()

    while True:
        F_prev = F_dilatado.copy()
        F_dilatado = cv2.dilate(F_dilatado, bb)
        F_dilatado = np.minimum(F_dilatado, Complemento)
        if np.array_equal(F_dilatado, F_prev):
            break

    F_final = 1 - F_dilatado
    preenchido = np.minimum(F_final, Complemento)
    resultado = np.maximum(N, preenchido)

    N = (resultado * 255).astype(np.uint8)
    R, G, B = devolva(R, G, B, N, r, g, b)
    
    return R, G, B

#==================== Função para eliminar uma cor indesejada para questão 5.B
def eliminar(R, G, B, r, g, b):
    h, w = len(R), len(R[0])
    
    def is_valid(x, y):
        return 0 <= x < h and 0 <= y < w
    
    def buscar_diferente(x, y, r, g, b):
        step = 1
        while step < max(h, w):
            for dx in range(-step, step + 1):
                for dy in range(-step, step + 1):
                    nx, ny = x + dx, y + dy
                    if is_valid(nx, ny):
                        if R[nx][ny] != r or G[nx][ny] != g or B[nx][ny] != b:
                            return R[nx][ny], G[nx][ny], B[nx][ny]
            step += 1
        return None
    
    for i in range(h):
        for j in range(w):
            if R[i][j] == r and G[i][j] == g and B[i][j] == b:
                diferente = buscar_diferente(i, j, r, g, b)
                if diferente:
                    R[i][j], G[i][j], B[i][j] = diferente
    
    return R, G, B

#==================== Função para fechar um objeto de uma cor específica para questão 5.D
def fechar(R, G, B, r, g, b):
    def vizinhos_iguais(vizinhanca, bb):
        for i in range(bb.shape[0]):
            for j in range(bb.shape[1]):
                if bb[i, j] is not None:
                    if vizinhanca[i, j] != bb[i, j]:
                        return False
        return True
    N = receba(R, G, B, r, g, b)
    N = (N * 255).astype(np.uint8)
    rows, cols = N.shape
    
    b1 = np.array([[255, 255, 255], [None, 0, None], [None, None, None]])
    b2 = np.array([[255, None, None], [255, 0, None], [255, None, None]])
    b3 = np.array([[None, None, None], [None, 0, None], [255, 255, 255]])
    b4 = np.array([[None, None, 255], [None, 0, 255], [None, None, 255]])
    bbs = [b1, b2, b3, b4]
    
    obj_rows, obj_cols = np.where(N == 255)
    if len(obj_rows) == 0 or len(obj_cols) == 0:
        return R, G, B
    min_row, max_row = obj_rows.min(), obj_rows.max()
    min_col, max_col = obj_cols.min(), obj_cols.max()

    min_row = max(0, min_row - 1)
    max_row = min(rows - 1, max_row + 1)
    min_col = max(0, min_col - 1)
    max_col = min(cols - 1, max_col + 1)
    
    change = True
    
    while change == True:
        change = False
        padded_image = np.pad(N, 1, mode='constant', constant_values=0)
        for bb in bbs:
            for i in range(min_row, max_row + 1):
                for j in range(min_col, max_col + 1):
                    neighborhood = padded_image[i:i+3, j:j+3]
                    if vizinhos_iguais(neighborhood, bb):
                        if N[i, j] == 0:
                            N[i, j] = 255
                            change = True
    
    R, G, B = devolva(R, G, B, N, r, g, b)
                
    return R, G, B

#==================== Função para esqueletar um objeto de uma cor específica para questão 5.E
def esqueletar(R, G, B, r, g, b): 
    bb = np.array([[1, 1, 1],
                  [1, 1, 1],
                  [1, 1, 1]], dtype=np.uint8)
    center = (1, 1)
    
    N = receba(R, G, B, r, g, b)
    N = (N * 255).astype(np.uint8)
    rows, cols = N.shape
    esqueleto = np.zeros_like(N, dtype=np.uint8)
    
    obj_rows, obj_cols = np.where(N == 255)
    if len(obj_rows) == 0 or len(obj_cols) == 0:
        return R, G, B
    min_row, max_row = obj_rows.min(), obj_rows.max()
    min_col, max_col = obj_cols.min(), obj_cols.max()

    min_row = max(0, min_row - 1)
    max_row = min(rows - 1, max_row + 1)
    min_col = max(0, min_col - 1)
    max_col = min(cols - 1, max_col + 1)
    
    imagem_erodida = N.copy()
    
    while True:
        imagem_aberta = dilatar(erodir(imagem_erodida, bb, center), bb, center)
        for i in range(min_row, max_row + 1):
            for j in range(min_col, max_col + 1):
                if (imagem_erodida[i][j] - imagem_aberta[i][j]) == 255:
                    esqueleto[i][j] += imagem_erodida[i][j] - imagem_aberta[i][j]
        
        aux = imagem_erodida.copy()
        imagem_erodida = erodir(imagem_erodida, bb, center)

        if (np.array_equal(imagem_erodida, aux)):
            esqueleto += imagem_erodida
            break
    
    N = esqueleto
    for i in range(len(N)):
        for j in range(len(N[0])):
            if N[i][j] == 0 and R[i][j] == r and G[i][j] == g and B[i][j] == b:
                R[i][j] = 255
                G[i][j] = 255
                B[i][j] = 255
                
    return R, G, B

#==================== Função que aplica o Hit or Miss para questão 5.F
def hitar(R, G ,B, r, g, b):
    N = receba(R, G, B, r, g, b)
    hit = np.zeros(N.shape)
    
    labeled_matrix, num_features = label(N)
    bbs = []
    ccs = []

    for i in range(1, num_features + 1):
        rows, cols = np.where(labeled_matrix == i)
        min_row, max_row = rows.min(), rows.max()
        min_col, max_col = cols.min(), cols.max()

        bb = N[min_row:max_row + 1, min_col:max_col + 1]
        bbs.append(bb)
        
    for i in range(len(bbs)):
        aux = np.pad(bbs[i], pad_width=1, mode='constant', constant_values=0)
        ccs.append(1 - aux)
        
    for i in range(len(bbs)):
        eroded_hit = cv2.erode(N, bbs[i])
        dilated_miss = cv2.dilate(1 - N, ccs[i])
        hit += cv2.bitwise_and(eroded_hit, dilated_miss)
        
    for i in range(len(bbs)):
        caminho_completo = f"{'caminho_base'}_{i}.png"
        bbs[i] = (bbs[i] * 127).astype(np.uint8)
        m2i(bbs[i], caminho_completo)
    for i in range(len(bbs)):
        caminho_completo = f"{'novo_caminho_base'}_{i}.png"
        ccs[i] = (ccs[i] * 127).astype(np.uint8)
        m2i(ccs[i], caminho_completo)
    
    hit = 1 - hit
    return (hit * 255).astype(np.uint8)

#==================== Função para gerar uma nova matriz binária delimitando apenas a cor desejada
def receba(R, G, B, r, g, b):
    linhas, colunas = R.shape
    N = np.zeros((linhas, colunas), dtype=np.uint8)
    
    for i in range(len(N)):
        for j in range(len(N[0])):
            if R[i][j] == r and G[i][j] == g and B[i][j] == b:
                N[i][j] = 1
            else:
                N[i][j] = 0
    return N

#==================== Função para "sobrepor" a matriz binária sobre a imagem colorida 
def devolva(R, G, B, N, r, g, b):
    for i in range(len(N)):
        for j in range(len(N[0])):
            if N[i][j] == 255:
                R[i][j] = r
                G[i][j] = g
                B[i][j] = b
    return R, G, B
   
#==================== Função para aplicar a transformada hit-or-miss
def hit_or_miss(img, kernel_hit, kernel_miss):
    eroded_hit = cv2.erode(img, kernel_hit)
    dilated_miss = cv2.dilate(1 - img, kernel_miss)
    result = cv2.bitwise_and(eroded_hit, dilated_miss)
    
    return result


#==================== C O N V E R S Õ E S =========================================
#==================== Converter de imagem para matriz em escala de Cinza
def i2m(imagem_path):
    imagem = Image.open(imagem_path)
    imagem_gray = imagem.convert('L')
    imagem_array = np.array(imagem_gray)

    return imagem_array

#==================== Converter de imagem para matrizes RGB
def i2m_rgb(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    
    if image is None:
        raise FileNotFoundError(f"Imagem não encontrada: {image_path}")
    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    r_channel = image[:, :, 0]
    g_channel = image[:, :, 1]
    b_channel = image[:, :, 2]
    
    return r_channel, g_channel, b_channel
    
#==================== Converter de matriz para imagem png em escala de cinza
def m2i(imagem_array, imagem_path):
    imagem = Image.fromarray(np.uint8(imagem_array))
    imagem.save(imagem_path)

#==================== Converter de matriz RGB para imagem png
def m2i_rgb(R, G, B, imagem_path):
    if not (R.shape == G.shape == B.shape):
        raise ValueError("As matrizes dos canais devem ter as mesmas dimensões.")

    image = np.dstack((R, G, B))
    image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    cv2.imwrite(imagem_path, image_bgr)