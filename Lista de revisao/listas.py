#Questao 1
numero = int(input("Quantidade desejada: "))

lst = []

for i in range(numero):
    lst.append(int(input("Digite um número: ")))

print("Lista original:", lst)
print("3 primeiros elementos:", lst[:3])
print("2 últimos elementos:", lst[-2:])
print("Lista invertida:", lst[::-1])
print("Índices pares:", lst[::2])
print("Índices ímpares:", lst[1::2])

#Questao 2
urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

dominios = []

for url in urls:
    dominios.append(url[4:-4])

print("URLs:", urls)
print("Dominios:", dominios)

#Questao 3 

from random import randint

lista = []

for i in range(10):
    lista.append(randint(-100, 100))

print("Lista ordenada:", sorted(lista))
print("Lista original:", lista)

print("Índice do maior valor:", lista.index(max(lista)))
print("Índice do menor valor:", lista.index(min(lista)))

print("Soma dos valores:", sum(lista))
print("Média dos valores:", sum(lista) / len(lista))

#Questao 4

Lista_1 = [int(x) for x in input("Lista1 separada por espaço: ").split()]
Lista_2 = [int(x) for x in input("Lista2 separada por espaço: ").split()]
Lista_3 = []
for i in range(max(len(Lista_1),len(Lista_2))-1):
    try:
        Lista_3.append(Lista_1[i])
    except:
        pass
    try:
        Lista_3.append(Lista_2[i])
    except:
        pass
print(Lista_3)

#Questao 5

import random
lista_1 = [random.randint(0,50) for x in range(10)]
lista_2 = [random.randint(0,50) for x in range(10)]
lista_intersecao = []
for elemento in lista_1:
    if elemento in lista_2 and elemento not in lista_intersecao:
        lista_intersecao.append(elemento)
print(lista_1)
print(lista_2)
print(lista_intersecao)

# QUESTÃO 6
import random
lista = [random.randint(0,100) for x in range(20)]
tamanho = int(input("Tamanho para divisão: "))
lista_principal =[]
for i in range(0,len(lista),tamanho):
    lista_principal.append(lista[i:i+tamanho])
print(lista_principal)

# QUESTÃO 7
matriz = []
for i in range(n :=int(input("Digte n:"))):
    matriz.append([i for _ in range(n)])
print(matriz)



