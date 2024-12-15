import numpy as np
from PIL import Image

#2. Máscara tipo 1
def mask1(img):
    linhas, colunas = img.shape
    resultado = np.copy(img)
    
    kernel = np.array([[0, 1, 0],
                       [1, 1, 1],
                       [0, 1, 0]])

    for i in range(1, linhas - 1):
        for j in range(1, colunas - 1):
            janela = img[i - 1:i + 2, j - 1:j + 2]
            resultado_pixel = np.sum(janela * kernel)
            resultado[i, j] = resultado_pixel//5

    return resultado

#2. Máscara tipo 2
def mask2(img):
    linhas, colunas = img.shape
    resultado = np.copy(img)
    
    kernel = np.array([[1, 1, 1],
                       [1, 1, 1],
                       [1, 1, 1]])

    for i in range(1, linhas - 1):
        for j in range(1, colunas - 1):
            janela = img[i - 1:i + 2, j - 1:j + 2]
            resultado_pixel = np.sum(janela * kernel)
            resultado[i, j] = resultado_pixel//9

    return resultado

#2. Máscara tipo 3
def mask3(img):
    linhas, colunas = img.shape
    resultado = np.copy(img)
    
    kernel = np.array([[1, 3, 1],
                       [3, 16, 3],
                       [1, 3, 1]])

    for i in range(1, linhas - 1):
        for j in range(1, colunas - 1):
            janela = img[i - 1:i + 2, j - 1:j + 2]
            resultado_pixel = np.sum(janela * kernel)
            resultado[i, j] = resultado_pixel//32

    return resultado

#2. Máscara tipo 4
def mask4(img):
    linhas, colunas = img.shape
    resultado = np.copy(img)
    
    kernel = np.array([[0, 1, 0],
                       [1, 4, 1],
                       [0, 1, 0]])

    for i in range(1, linhas - 1):
        for j in range(1, colunas - 1):
            janela = img[i - 1:i + 2, j - 1:j + 2]
            resultado_pixel = np.sum(janela * kernel)
            resultado[i, j] = resultado_pixel//8

    return resultado

#2. Mediana
def mask5(img):
    linhas, colunas = img.shape
    resultado = np.copy(img)

    for i in range(1, linhas - 1):
        for j in range(1, colunas - 1):
            janela = img[i - 1:i + 2, j - 1:j + 2]
            mediana = np.median(janela)
            resultado[i, j] = mediana
    
    return resultado

def i2m(imagem_path):
  imagem = Image.open(imagem_path)
  imagem_gray = imagem.convert('L')
  imagem_array = np.array(imagem_gray)

  return imagem_array
  
def m2i_bmp(imagem_array, imagem_path):
  imagem = Image.fromarray(np.uint8(imagem_array))
  imagem.save(imagem_path, format='BMP')
  
e2 = ("imagens/lena_ruido.bmp")
m2 = i2m(e2)
m2i_bmp(mask1(m2), "imagens_filtradas/m1.bmp")
m2i_bmp(mask2(m2), "imagens_filtradas/m2.bmp")
m2i_bmp(mask3(m2), "imagens_filtradas/m3.bmp")
m2i_bmp(mask4(m2), "imagens_filtradas/m4.bmp")
m2i_bmp(mask5(m2), "imagens_filtradas/mediana.bmp")