import random
import string

qtd = input("Informe a quantidade de caracteres: ")
qtd = int(qtd)

caracteres = string.ascii_letters + string.digits + string.punctuation

senha = ""

for i in range(qtd):
    nm = random.choice(caracteres) 
    senha += nm                   

print(senha)

