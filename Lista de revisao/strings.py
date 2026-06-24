# Questao 1 
x = input("Digite seu primeiro nome: ")
y = input("Digite seu sobrenome nome: ")
print(f"Bem-vinda(o), {x} {y}!")


# Questao 2 
x = input(" Digite uma frase: ")
y = x.count (" ")
print (f"Contagem de espaços vazios: {y}")

# Questao 3 
nome = input("Digite seu nome: ")
texto = ""
for letra in nome:
    texto += letra
    print(texto)

# Questao 4 
<<<<<<< HEAD
=======
cel = input("Digite o número de celular: ")

if len(cel) == 8:
    cel = "9" + cel

if len(cel) == 9:
    if cel[0] == "9":
        print(cel[:5] + "-" + cel[5:])
    else:
        print("Número inválido.")
else:
    print("Número inválido.")
>>>>>>> 14ca2425bac80f8155ffd9ec43abafe5f2bc8674

# Questao 5
letra = input("Digite uma frase: ")
indices = []
qnt = 0 
for i, letra in enumerate (letra):
    if letra in "AEIOUaeiou":
        indices.append(i)
        qnt = 1
z = letra.count("a") + letra.count("e") + letra.count("i") + letra.count("o") + letra.count("u")
print(f"Indice das vogais: {qnt}")
print(f"Número de vogais: {z}")
