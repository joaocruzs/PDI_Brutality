import cv2
import numpy as np
from Auxiliares import preencher, eliminar, fechar, esqueletar, hitar, m2i_rgb, i2m_rgb

#==================== Q U E S T Õ E S ===========================
#==================== 5.a. Preencher todos os buracos dos objetos pretos
def Q5a(img, imagem_path):
    R, G, B = i2m_rgb(img)
    R, G, B = preencher(R, G, B, 0, 0, 0)
    m2i_rgb(R, G, B, imagem_path)

#==================== 5.b. Eliminar todos e somente os objetos pretos
def Q5b(img, imagem_path):
    R, G, B = i2m_rgb(img)
    R, G, B = eliminar(R, G, B, 0, 0, 0)
    m2i_rgb(R, G, B, imagem_path)

#==================== 5.c. Preencher os buracos dos objetos de cor azul, amarelo e verde
def Q5c(img, imagem_path):
    R, G, B = i2m_rgb(img)
    R, G, B = preencher(R, G, B, 0, 0, 255)
    R, G, B = preencher(R, G, B, 255, 255, 0)
    R, G, B = preencher(R, G, B, 0, 255, 0)
    m2i_rgb(R, G, B, imagem_path)

#==================== 5.d. Encontrar o fecho convexo dos objetos de cor azul, amarelo e verde
def Q5d(img, imagem_path):
    R, G, B = i2m_rgb(img)
    R, G, B = fechar(R, G, B, 0, 0, 255)
    R, G, B = fechar(R, G, B, 255, 255, 0)
    R, G, B = fechar(R, G, B, 0, 255, 0)
    m2i_rgb(R, G, B, imagem_path)

#==================== 5.e. Encontrar o esqueleto dos objetos de cor azul, amarelo e verde
def Q5e(img, imagem_path):
    R, G, B = i2m_rgb(img)
    R, G, B = esqueletar(R, G, B, 0, 0, 255)
    R, G, B = esqueletar(R, G, B, 255, 255, 0)
    R, G, B = esqueletar(R, G, B, 0, 255, 0)
    m2i_rgb(R, G, B, imagem_path)