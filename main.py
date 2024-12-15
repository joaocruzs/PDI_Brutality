import os
import tkinter as tk
from tkinter import filedialog, messagebox, Checkbutton, IntVar
from PIL import Image, ImageTk, ImageOps, ImageFilter
import numpy as np
from Q1 import laplaciano, unsharp_masking, highboost, prewitt, sobel
from Q2 import mask1, mask2, mask3, mask4, mask5
from Q3 import diferenca, uniao, intersecao
from Q4 import erosao, dilatacao, abertura, fechamento

def i2m(imagem_path):
  imagem = Image.open(imagem_path)
  imagem_gray = imagem.convert('L')
  imagem_array = np.array(imagem_gray)

  return imagem_array

def m2i_png(imagem_array, imagem_path):
  imagem = Image.fromarray(np.uint8(imagem_array))
  imagem.save(imagem_path, format='PNG')
  
def m2i_bmp(imagem_array, imagem_path):
  imagem = Image.fromarray(np.uint8(imagem_array))
  imagem.save(imagem_path, format='BMP')
  
def selecionar_imagem():
    root = tk.Tk()
    root.withdraw()
    caminho_imagem = filedialog.askopenfilename(
        title="Selecione a Imagem", 
        filetypes=[("Arquivos de Imagem", "*.bmp;*.png;*.jpg;*.jpeg;*.tiff")]
    )
    
    return caminho_imagem

#========================= P R I N C I P A L =========================
class Principal:

  def __init__(self, root):
    self.root = root
    self.root.title("Atividade Prática 02")
    self.imagem_atual = None
    self.criar_pastas()

    #==========================BOTÕES=========================
    self.Question1 = tk.Button(root,
                          text="Questão 1",
                          command=self.Q1,
                          bg="lightblue",
                          width=25)

    self.Question2 = tk.Button(root,
                             text="Questão 2",
                             command=self.Q2,
                             bg="lightblue",
                             width=25)

    self.Question3 = tk.Button(root,
                            text="Questão 3",
                            command=self.Q3,
                            bg="lightblue",
                            width=25)
    
    self.Question4 = tk.Button(root,
                            text="Questão 4",
                            command=self.Q4,
                            bg="lightblue",
                            width=25)

    self.sair = tk.Button(root,
                          text="4. Sair",
                          command=self.root.destroy,
                          bg="lightblue",
                          width=25)
    #========layout==========
    self.Question1.pack(pady=10)
    self.Question2.pack(pady=10)
    self.Question3.pack(pady=10)
    self.Question4.pack(pady=10)
    self.sair.pack(pady=10)


#=========================FUNÇÕES=========================

  def criar_pastas(self):
    if not os.path.exists("imagens"):
      os.makedirs("imagens")
    if not os.path.exists("imagens_filtradas"):
      os.makedirs("imagens_filtradas")

  def Q1(self):
    e1 = ("imagens/lena_gray.bmp")
    m1 = i2m(e1)
    m2i_bmp(laplaciano(m1), "imagens_filtradas/laplace.bmp")
    m2i_bmp(unsharp_masking(m1), "imagens_filtradas/unsharp.bmp")
    m2i_bmp(highboost(m1), "imagens_filtradas/highb.bmp")
    m2i_bmp(prewitt(m1), "imagens_filtradas/prew.bmp")
    m2i_bmp(sobel(m1), "imagens_filtradas/sob.bmp")
    
  def Q2(self):
    e2 = ("imagens/lena_ruido.bmp")
    m2 = i2m(e2)
    m2i_bmp(mask1(m2), "imagens_filtradas/m1.bmp")
    m2i_bmp(mask2(m2), "imagens_filtradas/m2.bmp")
    m2i_bmp(mask3(m2), "imagens_filtradas/m3.bmp")
    m2i_bmp(mask4(m2), "imagens_filtradas/m4.bmp")
    m2i_bmp(mask5(m2), "imagens_filtradas/mediana.bmp")
    
  def Q3(self):
    e3a = selecionar_imagem()
    e3b = selecionar_imagem()
    m3a = i2m(e3a)
    m3b = i2m(e3b)
    
    if len(m3a) != len(m3b) or len(m3a[0]) != len(m3b[0]):
        raise ValueError("Imagens de dimensões diferentes.")
    else:
        m2i_png(intersecao(m3a, m3b), "imagens_filtradas/intersecao.png")
        m2i_png(uniao(m3a, m3b), "imagens_filtradas/uniao.png")
        m2i_png(diferenca(m3a, m3b), "imagens_filtradas/diferenca.png")
    
  def Q4(self):
    e4 = selecionar_imagem()
    m4 = i2m(e4)
    m2i_png(erosao(m4, 3), "imagens_filtradas/erosao.png")
    m2i_png(dilatacao(m4, 3), "imagens_filtradas/dilatacao.png")
    m2i_png(abertura(m4, 3), "imagens_filtradas/abertura.png")
    m2i_png(fechamento(m4, 3), "imagens_filtradas/fechamento.png")
    
if __name__ == "__main__":
  root = tk.Tk()
  programa = Principal(root)
  root.mainloop()
