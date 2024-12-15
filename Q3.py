import numpy as np
from PIL import Image

#3.a. interseção
def intersecao(img1, img2):
    resultado = []
    
    for i in range(len(img1)):
        linha_i = []
        for j in range(len(img1[0])):
            linha_i.append(min(img1[i][j], img2[i][j]))
        resultado.append(linha_i)

    return resultado

#3.b. união
def uniao(img1, img2):
    resultado = []
    
    for i in range(len(img1)):
        linha_i = []
        for j in range(len(img1[0])):
            linha_i.append(max(img1[i][j], img2[i][j]))
        resultado.append(linha_i)

    return resultado

#3.c. diferença
def diferenca(img1, img2):
    resultado = []
    
    for i in range(len(img1)):
        linha_i = []
        for j in range(len(img1[0])):
            if img1[i][j] >= img2[i][j]:
                value = img1[i][j] - img2[i][j]
            else:
                value = 0
            linha_i.append(value)
        resultado.append(linha_i)

    return resultado

def i2m(imagem_path):
  imagem = Image.open(imagem_path)
  imagem_gray = imagem.convert('L')
  imagem_array = np.array(imagem_gray)

  return imagem_array
  
def m2i_png(imagem_array, imagem_path):
  imagem = Image.fromarray(np.uint8(imagem_array))
  imagem.save(imagem_path, format='PNG')

e3a = ("imagens/ex3.png")
e3b = ("imagens/ex2.png")
m3a = i2m(e3a)
m3b = i2m(e3b)

if len(m3a) != len(m3b) or len(m3a[0]) != len(m3b[0]):
    raise ValueError("Imagens de dimensões diferentes.")
else:
    m2i_png(intersecao(m3a, m3b), "imagens_filtradas/intersecao.png")
    m2i_png(uniao(m3a, m3b), "imagens_filtradas/uniao.png")
    m2i_png(diferenca(m3a, m3b), "imagens_filtradas/diferenca.png")