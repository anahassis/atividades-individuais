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

