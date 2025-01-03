import numpy as np
from Auxiliares import i2m, m2i, dilatar, erodir

#==================== Q U E S T Õ E S ===========================
#==================== QUestão 4.a. Dilatação
def dilatacao(imagem, kernel, center, imagem_path):
    img = i2m(imagem)
    resultado = dilatar(img, kernel, center)
    m2i(resultado, imagem_path)

#==================== Questão 4.b. Erosão
def erosao(imagem, kernel, center, imagem_path):
    img = i2m(imagem)
    resultado  = erodir(img, kernel, center)
    m2i(resultado, imagem_path)

#==================== Questão 4.c. Abertura
def abertura(img, kernel, center, imagem_path):
    imagem = i2m(img)
    resultado = dilatar(erodir(imagem, kernel, center), kernel, center)
    m2i(resultado, imagem_path)
#==================== Questão 4.d. Fechamento
def fechamento(img, kernel, center, imagem_path):
    imagem = i2m(img)
    resultado = erodir(dilatar(imagem, kernel, center), kernel, center)
    m2i(resultado, imagem_path)