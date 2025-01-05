import os
import numpy as np
from Q1 import laplaciano, unsharp, highboost, prewitt, sobel
from Q2 import matriz1, matriz2, matriz3, matriz4, mediana
from Q3 import intersecao, uniao, diferenca
from Q4 import dilatacao, erosao, abertura, fechamento
from Q5 import Q5a, Q5b, Q5c, Q5d, Q5e, Q5f

#==================== C R I A Ç Ã O   D E   P A S T A ================
if not os.path.exists("imagens_geradas"):
    os.makedirs("imagens_geradas")
 
#==================== Q U E S T Õ E S ================================
#==================== Questão 1
laplaciano("imagens/lena_gray.bmp", "imagens_geradas/Q1a_laplaciano.png")
unsharp("imagens/lena_gray.bmp", "imagens_geradas/Q1b_unsharp2.png")
highboost("imagens/lena_gray.bmp", "imagens_geradas/Q1c_highboost.png")
prewitt("imagens/lena_gray.bmp", "imagens_geradas/Q1d_prewitt.png")
sobel("imagens/lena_gray.bmp", "imagens_geradas/Q1e_sobel.png")
 
#==================== Questão 2
matriz1("imagens/lena_ruido.bmp", "imagens_geradas/Q2_mask1.png")
matriz2("imagens/lena_ruido.bmp", "imagens_geradas/Q2_mask2.png")
matriz3("imagens/lena_ruido.bmp", "imagens_geradas/Q2_mask3.png")
matriz4("imagens/lena_ruido.bmp", "imagens_geradas/Q2_mask4.png")
mediana("imagens/lena_ruido.bmp", "imagens_geradas/Q2_mediana.png")

#==================== Questão 3
uniao("imagens/img1.png", "imagens/img2.png", "imagens_geradas/Q3_uniao.png")
intersecao("imagens/img1.png", "imagens/img2.png", "imagens_geradas/Q3_intersecao.png")
diferenca("imagens/img1.png", "imagens/img2.png", "imagens_geradas/Q3_diferenca.png")

#==================== Questão 4 #Adicionar elemento central do kernel
# Elemento estruturante (exemplo)
struct = np.array([
    [0, 1, 0],
    [1, 1, 1],
    [0, 1, 0]
])

# Centro do elemento estruturante
center = (1, 1)
    
dilatacao("imagens/img3.png", struct, center, "imagens_geradas/Q4_dilatacao.png")
erosao("imagens/img3.png", struct, center, "imagens_geradas/Q4_erosao.png")
abertura("imagens/img3.png", struct, center, "imagens_geradas/Q4_abertura.png")
fechamento("imagens/img3.png", struct, center, "imagens_geradas/Q4_fechamento.png")

#==================== Questão 5
Q5a("imagens/quadro.png", "imagens_geradas/Q5a.png")
Q5b("imagens/quadro.png", "imagens_geradas/Q5b.png")
Q5c("imagens/quadro.png", "imagens_geradas/Q5c.png")
Q5d("imagens_geradas/Q5c.png", "imagens_geradas/Q5d.png")
Q5e("imagens_geradas/Q5c.png", "imagens_geradas/Q5e.png")
Q5f("imagens_geradas/Q5c.png", "imagens_geradas/Q5f.png")
