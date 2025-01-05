import cv2
import numpy as np
from Auxiliares import m2i

#==================== Q U E S T Õ E S =========================== 
#==================== Questão 1.a. Laplaciano
def laplaciano(img, imagem_path):
    imagem = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    laplaciano = cv2.Laplacian(imagem, cv2.CV_64F, ksize=3)
    laplaciano = cv2.convertScaleAbs(laplaciano)
    matriz = np.array(laplaciano)
    m2i(matriz, imagem_path)

#==================== Questão 1.b. Unsharp Masking   
def unsharp(img, imagem_path, alpha = 1.5):
    imagem = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    imagem_suavizada = cv2.GaussianBlur(imagem, (9, 9), sigmaX=2, sigmaY=2)
    
    mascara = cv2.subtract(imagem, imagem_suavizada)
    
    imagem_unsharp = cv2.addWeighted(imagem, alpha, mascara, -0.5, 0)
    matriz = np.array(imagem_unsharp)
    m2i(matriz, imagem_path)

#==================== Questão 1.c. Highboost
def highboost(img, imagem_path, A = 1.5):
    imagem = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    imagem_suavizada = cv2.GaussianBlur(imagem, (9, 9), sigmaX=2, sigmaY=2)

    mascara = cv2.subtract(imagem, imagem_suavizada)

    imagem_highboost = cv2.addWeighted(imagem, A, mascara, (1 - A), 0)
    matriz = np.array(imagem_highboost)
    m2i(matriz, imagem_path)

#=================== Questão 1.d.i Detecção de Bordas Usando Prewitt
def prewitt(img, imagem_path):
    imagem = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    kernel_prewitt_x = np.array([[-1, 0, 1],
                                 [-1, 0, 1],
                                 [-1, 0, 1]])

    kernel_prewitt_y = np.array([[-1, -1, -1],
                                 [ 0,  0,  0],
                                 [ 1,  1,  1]])

    gradiente_x = cv2.filter2D(imagem, -1, kernel_prewitt_x)
    gradiente_y = cv2.filter2D(imagem, -1, kernel_prewitt_y)

    bordas = cv2.magnitude(gradiente_x.astype(float), gradiente_y.astype(float))
    bordas = np.uint8(bordas)
    matriz = np.array(bordas)
    m2i(matriz, imagem_path)

#==================== Questão 1.d.ii Detecção de Bordas usando Sobel
def sobel(img, imagem_path):
    imagem = cv2.imread(img, cv2.IMREAD_GRAYSCALE)

    gradiente_x = cv2.Sobel(imagem, cv2.CV_64F, dx=1, dy=0, ksize=3)
    gradiente_y = cv2.Sobel(imagem, cv2.CV_64F, dx=0, dy=1, ksize=3)

    gradiente_x = cv2.convertScaleAbs(gradiente_x)
    gradiente_y = cv2.convertScaleAbs(gradiente_y)

    bordas = cv2.addWeighted(gradiente_x, 0.5, gradiente_y, 0.5, 0)
    matriz = np.array(bordas)
    m2i(matriz, imagem_path)