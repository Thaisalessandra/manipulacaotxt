##criado um arquivo com números de 1 a 1000
import random
'''
1 - Criar um programa que receba 200 números randômicos
(usar pacote Random do Python) e escreva em um arquivo texto.
2 - Fazer um programa para ler o arquivo do exercício 1 e gravar
em um segundo arquivo todos os números múltiplos de 3
3 - Criar um programa no qual o usuário informe uma quantidade X de nomes
de produtos e valores. Os nome e valores devem se gravados em um arquivo,
o nome com string de tamanho 50 e o valor com 3 casas decimais com string de tamanho 15.
'''

#1
num = open("numeros.txt","w")
numero_aleatorio =random.random()
mult=[]
for i in range(1,11):

    numero_aleatorio = numero_aleatorio+1
    num.write(str(numero_aleatorio)+"\n")
num.close()
#2
with open("numeros.txt","r") as arquivo:
    multiplo= open("multiplo.txt","w")
    for valor in arquivo:
        x = float(valor)
        if x % 3 == 0:
            multiplo.write(str(valor)+"\n")
            mult.append(valor)


#3
valores=[]
nomes=[]
qtd_nomes_cadastro=int(input("Digite a quantidade de produtos que serão digitados:"))
qtd_de_valores=int(input("Digite a quantidade de valores a ser cadastrado:"))
valores_e_nomes=open("valoresenome.txt","w")
for i in range(0,qtd_nomes_cadastro):
    nome = str(input("Digite nome do produto:"))
    nome_composto = "%-50s" % nome
    valores_e_nomes.write(str(nome_composto) + "\n")
    nomes.append(nome)

    if len(nome)> 50:
        while len(nome)> 50:
            print("Numero de caracter acima do limite, digite novamente!")
            nome = str(input("Digite nome do produto:"))
            nome_composto="%-50s"%nome
            print(nome_composto)
            valores_e_nomes.write(str(nome_composto) + "\n")
            nomes.append(nome)

for i in range(qtd_de_valores):
    valores_list=[]
    valores=float(input("Digite os valores dos produtos:"))
    # valores="{:.3f}".format(valores)
    valor3f='%.3f'%valores
    stringcomposta="%-15s"%valor3f
    valores_list.append(valor3f)
    valores_e_nomes.write(str(stringcomposta)+"\n")

valores_e_nomes.close()

