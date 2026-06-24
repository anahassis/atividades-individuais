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