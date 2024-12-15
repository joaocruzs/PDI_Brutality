import numpy as np
from PIL import Image

#4.a. Erosão
def erosao(img, es):
    linhas, colunas = img.shape
    resultado = np.copy(img)

    es = es // 2
    
    for i in range(linhas):
        for j in range(colunas):
            menor_valor = img[i][j]
            for k in range(-es, es + 1):
                for l in range(-es, es + 1):
                    if 0 <= i + k < linhas and 0 <= j + l < colunas:
                        menor_valor = min(menor_valor, img[i + k][j + l])
                    else:
                        menor_valor = min(menor_valor, 0)
            resultado[i][j] = menor_valor

    return resultado

#4.b. Dilatação
def dilatacao(img, es):
    linhas, colunas = img.shape
    resultado = np.copy(img)

    es = es // 2
    
    for i in range(linhas):
        for j in range(colunas):
            menor_valor = img[i][j]
            for k in range(-es, es + 1):
                for l in range(-es, es + 1):
                    if 0 <= i + k < linhas and 0 <= j + l < colunas:
                        menor_valor = max(menor_valor, img[i + k][j + l])
                    else:
                        menor_valor = max(menor_valor, 0)
            resultado[i][j] = menor_valor

    return resultado

#4.c. Abertura
def abertura(img, es):
    return dilatacao(erosao(img, es), es)

#4.d. Fechamento
def fechamento (img, es):
    return erosao(dilatacao(img, es), es)

def i2m(imagem_path):
  imagem = Image.open(imagem_path)
  imagem_gray = imagem.convert('L')
  imagem_array = np.array(imagem_gray)

  return imagem_array
  
def m2i_png(imagem_array, imagem_path):
  imagem = Image.fromarray(np.uint8(imagem_array))
  imagem.save(imagem_path, format='PNG')
  
e1 = ("imagens/ex1.png")
m4 = i2m(e1)
m2i_png(erosao(m4, 3), "imagens_filtradas/erosao.png")
m2i_png(dilatacao(m4, 3), "imagens_filtradas/dilatacao.png")
m2i_png(abertura(m4, 3), "imagens_filtradas/abertura.png")
m2i_png(fechamento(m4, 3), "imagens_filtradas/fechamento.png")