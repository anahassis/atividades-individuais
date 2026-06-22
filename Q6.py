import random 
class Personagem:
    def __init__(self,nome,vida):
        self.nome = nome 
        self.vida = vida 
    def tomar__dano(self,valor):
        self.vida -= valor

class Mago(Personagem):
    def __init__(self,nome,vida,mana: int):
        super().__init__(nome,vida)
        self.mana = mana

    def __str__(self):
        return f"Nome: {self.nome}, vida: {self.vida},mana: {self.mana}"
    
    def __add__(self,valor):
        self.mana += valor
        return self.mana
    
    def __sub__(self,valor):
        self.mana -= valor
        return self.mana

    def __mul__(self,fator):
        self.mana * fator
        return self.mana

    def __truediv__(self,valor):
        self.mana/valor
        return self.mana

class barbaro(Personagem):
    def __init__(self,nome,vida,stramina):
        super().__init__(nome,vida)
        self.stramina = stramina
        self.furia = False
    
    def __str__(self):
        return f"Nome: {self.nome}, vida: {self.vida},stamina:{self.stramina}"
    

    def __add__(self,valor):
        self.stramina += 1
        if self.furia:
            self.valor *1.5
        

        return self.stramina

    def __sub__(self,valor):
        self.stramina -= 1
        if self.stramina < 0 and self.furia:
            self.valor = 5
        return self.stramina

    def __mul__(self,fator):
        self.stramina * fator
        if self.furia:
            self.stramina += 5 
        return self.stramina
    
    def __truediv__(self,valor):
        self.stramina / valor
        return self.valor

match input("Qual o tipo desejado: "):
    case "Mago":
        personagem = Mago(input("Nome: "),int(input("Vida: ")),int(input("Mana: ")))
    
    case "Barbaro":
        personagem = barbaro(input("Nome: "),int(input("Vida: ")),int(input("stamina: ")))
    
while True:
    print(personagem)
    print("1- Tomar porção simples")
    print("2- Tomar porção especial")
    print("3- Ataque básico")
    print("4- Ataque especial")
    print("5- Sair")

    match int(input()):
        case 5:
            print(personagem)
            break
        case 1:
            (personagem +5)
            personagem.tomar__dano(random.randint(1, 10))
        
        case 2:
            (personagem*1.5)
            personagem.tomar__dano(random.randint(1, 10))

        case 3:
            (personagem -2)
            personagem.tomar__dano(random.randint(1, 10))

        case 4:
            (personagem /2)
            personagem.tomar__dano(random.randint(1, 10))
        




        


    





    

        

