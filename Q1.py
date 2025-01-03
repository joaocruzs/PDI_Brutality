import numpy as np
from Auxiliares import gaussiano, i2m, m2i

#==================== Q U E S T Õ E S =========================== 
#==================== Questão 1.a. Laplaciano
def laplaciano(img, imagem_path):
    imagem = i2m(img)
    kernel = np.array([[ 0,  1,  0], [ 1, -4,  1], [ 0,  1,  0]])
    
    linhas, colunas = imagem.shape
    laplaciano = np.copy(imagem)

    for i in range(1, linhas - 1):
        for j in range(1, colunas - 1):
            janela = imagem[i-1:i+2, j-1:j+2]
            laplaciano[i, j] = np.sum(janela * kernel)

    resultado = np.clip(laplaciano, 0, 255)
    m2i(resultado, imagem_path)

#==================== Questão 1.b. Unsharp Masking
def unsharp_masking(img,imagem_path, alpha = 1.5):
    imagem = i2m(img)
    imagem_suavizada = gaussiano(imagem)
    realce = imagem - imagem_suavizada
    imagem_unsharp = imagem + alpha * realce

    resultado = np.clip(imagem_unsharp, 0, 255)
    m2i(resultado, imagem_path)

#==================== Questão 1.c. Highboost
def highboost(img, imagem_path, k = 1.5):
    imagem = i2m(img)
    imagem_suavizada = gaussiano(imagem)
    imagem_highboost = k * imagem - imagem_suavizada
    
    resultado = np.clip(imagem_highboost, 0, 255)
    m2i(resultado, imagem_path)

#=================== Questão 1.d.i Detecção de Bordas Usando Prewitt
def prewitt(img, imagem_path):
    imagem = i2m(img)
    kernel_Gx = np.array([[ 1,  0, -1], [ 1,  0, -1], [ 1,  0, -1]])
    kernel_Gy = np.array([[ 1,  1,  1], [ 0,  0,  0], [-1, -1, -1]])

    linhas, colunas = imagem.shape
    grad_Gx = np.zeros_like(imagem)
    grad_Gy = np.zeros_like(imagem)
    
    for i in range(1, linhas - 1):
        for j in range(1, colunas - 1):
            janela = imagem[i - 1:i + 2, j - 1:j + 2]
            grad_Gx[i, j] = np.sum(janela * kernel_Gx)
            grad_Gy[i, j] = np.sum(janela * kernel_Gy)
            
    gradiente_total = np.sqrt(grad_Gx**2 + grad_Gy**2)
    binarizado = (gradiente_total > 10) * 255 
    
    resultado = np.clip(binarizado, 0, 255)
    m2i(resultado, imagem_path)

#==================== Questão 1.d.ii Detecção de Bordas usando Sobel
def sobel(img, imagem_path):
    imagem = i2m(img)
    kernel_Gx = np.array([[ 1,  0, -1], [ 2,  0, -2], [ 1,  0, -1]])
    kernel_Gy = np.array([[ 1,  2,  1], [ 0,  0,  0], [-1, -2, -1]])
    
    linhas, colunas = imagem.shape
    grad_Gx = np.zeros_like(imagem)
    grad_Gy = np.zeros_like(imagem)

    for i in range(1, linhas - 1):
        for j in range(1, colunas - 1):
            janela = imagem[i - 1:i + 2, j - 1:j + 2]
            grad_Gx[i, j] = np.sum(janela * kernel_Gx)
            grad_Gy[i, j] = np.sum(janela * kernel_Gy)
    
    gradiente_total = np.sqrt(grad_Gx**2 + grad_Gy**2)
    binarizado = (gradiente_total > 10) * 255 
    
    resultado = np.clip(binarizado, 0, 255)
    m2i(resultado, imagem_path)