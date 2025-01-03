#========================= I M P O R T A Ç Õ E S =====================
import os
import numpy as np
from Q1 import laplaciano, unsharp_masking, highboost, prewitt, sobel
from Q2 import matriz1, matriz2, matriz3, matriz4, mediana
from Q3 import intersecao, uniao, diferenca
from Q4 import dilatacao, erosao, abertura, fechamento
from Q5 import Q5a, Q5b, Q5c, Q5d, Q5e

#==================== C R I A Ç Ã O   D E   P A S T A ================
if not os.path.exists("imagens_filtradas"):
    os.makedirs("imagens_filtradas")

#==================== Q U E S T Õ E S ================================
#==================== Questão 1
laplaciano("lena_gray.bmp", "imagens_filtradas/Q1a_laplaciano.png")
unsharp_masking("lena_gray.bmp", "imagens_filtradas/Q1b_unsharp.png")
highboost("lena_gray.bmp", "imagens_filtradas/Q1c_highboost.png")
prewitt("lena_gray.bmp", "imagens_filtradas/Q1d_prewitt.png")
sobel("lena_gray.bmp", "imagens_filtradas/Q1e_sobel.png")
 
#==================== Questão 2
matriz1("lena_ruido.bmp", "imagens_filtradas/Q2_mask1.png")
matriz2("lena_ruido.bmp", "imagens_filtradas/Q2_mask2.png")
matriz3("lena_ruido.bmp", "imagens_filtradas/Q2_mask3.png")
matriz4("lena_ruido.bmp", "imagens_filtradas/Q2_mask4.png")
mediana("lena_ruido.bmp", "imagens_filtradas/Q2_mediana.png")

#==================== Questão 3
uniao("img1.png", "img2.png", "imagens_filtradas/Q3_uniao.png")
intersecao("img1.png", "img2.png", "imagens_filtradas/Q3_intersecao.png")
diferenca("img1.png", "img2.png", "imagens_filtradas/Q3_diferenca.png")

#==================== Questão 4 #Adicionar elemento central do kernel
# Elemento estruturante (exemplo)
struct = np.array([
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
])

# Centro do elemento estruturante
center = (1, 1)
    
dilatacao("img3.png", struct, center, "imagens_filtradas/Q4_dilatacao.png")
erosao("img3.png", struct, center, "imagens_filtradas/Q4_erosao.png")
abertura("img3.png", struct, center, "imagens_filtradas/Q4_abertura.png")
fechamento("img3.png", struct, center, "imagens_filtradas/Q4_fechamento.png")

#==================== Questão 5
Q5a("quadro.png", "imagens_filtradas/Q5a.png")
Q5b("quadro.png", "imagens_filtradas/Q5b.png")
Q5c("quadro.png", "imagens_filtradas/Q5c.png")
Q5d("quadro.png", "imagens_filtradas/Q5d.png")
Q5e("quadro.png", "imagens_filtradas/Q5e.png")


