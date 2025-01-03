import numpy as np
from Auxiliares import mascara, i2m, m2i

#==================== Q U E S T Õ E S ===========================
#==================== Questão 2. Máscara tipo 1
def matriz1(img, imagem_path):
    imagem = i2m(img)
    kernel = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])

    resultado = mascara(imagem, kernel, 5)
    m2i(resultado, imagem_path)

#==================== Questão 2. Máscara tipo 2
def matriz2(img, imagem_path):
    imagem = i2m(img)
    kernel = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])

    resultado = mascara(imagem, kernel, 9)
    m2i(resultado, imagem_path)

#==================== Questão 2. Máscara tipo 3
def matriz3(img, imagem_path):
    imagem = i2m(img)
    kernel = np.array([[1, 3, 1], [13, 16, 3], [1, 3, 1]])

    resultado = mascara(imagem, kernel, 32)
    m2i(resultado, imagem_path)

#==================== Questão 2. Máscara tipo 4
def matriz4(img, imagem_path):
    imagem = i2m(img)
    kernel = np.array([[0, 1, 0], [1, 4, 1], [0, 1, 0]])

    resultado = mascara(imagem, kernel, 8)
    m2i(resultado, imagem_path)

#==================== Questão 2. Mediana
def mediana(img, imagem_path):
    imagem = i2m(img)
    linhas, colunas = imagem.shape
    resultado = np.copy(imagem)

    for i in range(1, linhas - 1):
        for j in range(1, colunas - 1):
            janela = imagem[i - 1:i + 2, j - 1:j + 2]
            mediana = np.median(janela)
            resultado[i, j] = mediana
    
    m2i(resultado, imagem_path)