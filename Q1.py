import numpy as np
from Q2 import mask2
from PIL import Image

#Questão 1.a. Laplaciano
def laplaciano(img):
    linhas, colunas = img.shape
    resultado = np.copy(img)

    kernel = np.array([[ -1,  -1,  -1],
                       [ -1, 8,  -1],
                       [ -1,  -1,  -1]])
   #kernel = np.array([[ 0,  1,  0],
   #                   [ 1, -4,  1],
   #                   [ 0,  1,  0]])

    for i in range(1, linhas - 1):
        for j in range(1, colunas - 1):
            janela = img[i-1:i+2, j-1:j+2]
            resultado[i, j] = np.sum(janela * kernel)

    return np.clip(resultado, 0, 255)

#Questão 1.b. Unsharp Masking
def unsharp_masking(img, alpha):
    imagem_suavizada = mask2(img)
    realce = img - imagem_suavizada
    imagem_unsharp = img + alpha * realce

    return np.clip(imagem_unsharp, 0, 255)

#Questão 1.c. Highboost
def highboost(img, k):
    imagem_suavizada = mask2(img)
    realce = img - imagem_suavizada
    imagem_highboost = img + k * realce
    
    return np.clip(imagem_highboost, 0, 255)

#Questão 1.d.i Prewitt
def prewitt(img):
    linhas, colunas = img.shape
    kernel_Gx = np.array([[ 1,  0, -1],
                         [ 1,  0, -1],
                         [ 1,  0, -1]])
    
    kernel_Gy = np.array([[ 1,  1,  1],
                         [ 0,  0,  0],
                         [-1, -1, -1]])

    grad_Gx = np.zeros_like(img)
    grad_Gy = np.zeros_like(img)
    
    for i in range(1, linhas - 1):
        for j in range(1, colunas - 1):
            janela = img[i - 1:i + 2, j - 1:j + 2]
            grad_Gx[i, j] = np.sum(janela * kernel_Gx)
            grad_Gy[i, j] = np.sum(janela * kernel_Gy)
            
    gradiente_total = np.sqrt(grad_Gx**2 + grad_Gy**2)
    
    return np.clip(gradiente_total, 0, 255)

#Questão 1.d.ii Sobel
def sobel(img):
    linhas, colunas = img.shape
    kernel_Gx = np.array([[ 1,  0, -1],
                         [ 2,  0, -2],
                         [ 1,  0, -1]])
    kernel_Gy = np.array([[ 1,  2,  1],
                         [ 0,  0,  0],
                         [-1, -2, -1]])
    grad_Gx = np.zeros_like(img)
    grad_Gy = np.zeros_like(img)

    for i in range(1, linhas - 1):
        for j in range(1, colunas - 1):
            janela = img[i - 1:i + 2, j - 1:j + 2]
            grad_Gx[i, j] = np.sum(janela * kernel_Gx)
            grad_Gy[i, j] = np.sum(janela * kernel_Gy)
    
    gradiente_total = np.sqrt(grad_Gx**2 + grad_Gy**2)

    return np.clip(gradiente_total, 0, 255)

def i2m(imagem_path):
  imagem = Image.open(imagem_path)
  imagem_gray = imagem.convert('L')
  imagem_array = np.array(imagem_gray)

  return imagem_array
  
def m2i_bmp(imagem_array, imagem_path):
  imagem = Image.fromarray(np.uint8(imagem_array))
  imagem.save(imagem_path, format='BMP')
  
e1 = ("imagens/lena_gray.bmp")
m1 = i2m(e1)
#m2i_bmp(laplaciano(m1), "imagens_filtradas/lena_laplaciano2.bmp")
m2i_bmp(unsharp_masking(m1, 0.75), "imagens_filtradas/lena_unsharp2.bmp")
m2i_bmp(highboost(m1, 1), "imagens_filtradas/lena_highboost2.bmp")
m2i_bmp(highboost(m1, 2), "imagens_filtradas/lena_highboost3.bmp")
#m2i_bmp(prewitt(m1), "imagens_filtradas/lena_prewitt.bmp")
#m2i_bmp(sobel(m1), "imagens_filtradas/lena_sobel.bmp")