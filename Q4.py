class pessoa:
    def __init__(self,nome = str, altura = float):
        self.nome = nome
        self.altura = altura

    def __str__(self):
        return (f"Nome{self.nome} e altura {self.altura}")

    def __gt__(self,other):
        return self.altura > other.altura
    
    def __lt__(self,other):
        return self.altura < other.altura

quantidade = int(input("Quantas pessoas:"))

lst = []

for i in range(quantidade):
    lst.append(pessoa(input("NOME: "),float(input("ALTURA: "))))

print(max(lst)) 
print(min(lst))   

for pessoa in sorted(lst):
    print(pessoa)