class carteira:
    def __init__(self,moeda=str,saldo=float):
        self.moeda = moeda
        self.saldo = saldo
        self.conversao = {
            "BRL":0.75,
            "USD":0.15,
            "CNY":1
        }

    
    def  __add__(self,valor_yuan):
        self.saldo += valor_yuan * self.conversao[self.moeda]
        return (self.saldo)

    def __sub__(self,valor_yuan):
       self.saldo -= valor_yuan * self.conversao[self.moeda]
       return (self.saldo)
Carteira = carteira("USD",10)
print (Carteira +10)
print(Carteira -10)
