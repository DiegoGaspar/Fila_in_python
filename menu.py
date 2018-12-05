from fila_arq import Fila
import time

fila = Fila()
resposta = open("resposta.txt","w")

inicio = time.time()
arquivo = open("nome_do_arquivo.txt")
for linha in arquivo:
    linha = linha.rstrip()
    fila.push(linha)
fim = time.time()

resposta.write("O tempo de execução foi ")
resposta.write(str(fim - inicio))
resposta.close()
