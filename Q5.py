class Onibus:
    def __init__(self,placa:str,nome_motorista:str,assentos):
        self.placa = placa
        self.nome_motorista = nome_motorista

        lst = []
        for i in range(assentos):
            lst.append(False)
        self.assentos = lst
    
    def __len__(self):
        return  len(self.assentos)
    
    def __getitem__(self,indice):
        if  -1 < self.indice > len(self.assentos):
            return self.assentos[indice] 
        
        else:
            raise IndexError(f"Escolha um valor entre 0 e {len(self.assentos)}")
    
    def __setitem__(self,indice,valor):
        if -1 < indice < len(self.assentos):
            if isinstance(valor, bool):
                return self.assentos[indice]
            else:
                raise IndexError(f"Escolha um valor entre 0 e {len(self.assentos)}")
            
        else:
            raise TypeError(f"Valor deve ser booleano (True/False)")
    
    def __str__(self):
       return  f"Onibus: {self.placa} \n Assentos totais: {len(self.assentos)}\n Assentos totais: {len(self.assentos)}\n Assentos ocupados: {self.assentos.count(True)}\n Assentos ocupados: {self.assentos.count(False)}"
    

onibus = Onibus("ABC-1234", "João Silva", 10) # Ônibus com 10 assentos
print(len(onibus)) # Verificando total de assentos 
onibus[0] = True # Ocupando o primeiro assento (índice 0) 
print(onibus) # Exibindo informações do ônibus 
# Saída esperada: 
# Ônibus (Placa: ABC-1234) - Motorista: João Silva 
# Assentos totais: 10 
# Assentos ocupados: 1 
# Assentos livres: 9
