from Auxiliares import i2m, m2i

#==================== Q U E S T Õ E S ===========================
#==================== 3.q. união
def uniao(img1, img2, imagem_path):
    imagem1 = i2m(img1)
    imagem2 = i2m(img2)
    
    if len(imagem1) != len(imagem2) or len(imagem1[0]) != len(imagem2[0]):
        raise ValueError("Imagens de dimensões diferentes.")

    resultado = []
    
    for i in range(len(imagem1)):
        linha_i = []
        for j in range(len(imagem1[0])):
            linha_i.append(max(imagem1[i][j], imagem2[i][j]))
        resultado.append(linha_i)

    m2i(resultado, imagem_path)
    
#==================== 3.b. interseção
def intersecao(img1, img2, imagem_path):
    imagem1 = i2m(img1)
    imagem2 = i2m(img2)
    
    if len(imagem1) != len(imagem2) or len(imagem1[0]) != len(imagem2[0]):
        raise ValueError("Imagens de dimensões diferentes.")

    resultado = []
    
    for i in range(len(imagem1)):
        linha_i = []
        for j in range(len(imagem1[0])):
            linha_i.append(min(imagem1[i][j], imagem2[i][j]))
        resultado.append(linha_i)

    m2i(resultado, imagem_path)

#==================== 3.c. diferença
def diferenca(img1, img2, imagem_path):
    imagem1 = i2m(img1)
    imagem2 = i2m(img2)
    
    if len(imagem1) != len(imagem2) or len(imagem1[0]) != len(imagem2[0]):
        raise ValueError("Imagens de dimensões diferentes.")

    resultado = []
    
    for i in range(len(imagem1)):
        linha_i = []
        for j in range(len(imagem1[0])):
            if imagem1[i][j] >= imagem2[i][j]:
                value = imagem1[i][j] - imagem2[i][j]
            else:
                value = 0
            linha_i.append(value)
        resultado.append(linha_i)

    m2i(resultado, imagem_path)