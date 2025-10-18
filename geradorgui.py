import random
import tkinter as tk
import string

janela = tk.Tk()
janela.title("Gerador de Senhas")  # título da janela
entrada = tk.Entry(janela)
entrada.pack()

resultado = tk.Label(janela, text="")
resultado.pack()


def gerar_senha():
    qtd = int(entrada.get())
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ""
    for i in range(qtd):
        senha += random.choice(caracteres)
    resultado.config(text=senha)
    
botao = tk.Button(janela, text="Gerar Senha", command=gerar_senha)
botao.pack()

janela.mainloop()
    



