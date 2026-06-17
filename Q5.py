class onibus:
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
            if isinstance(valor, boo1):
                return self.assentos[indice]
            else:
                raise IndexError(f"Escolha um valor entre 0 e {len(self.assentos)}")
            
         else:
            raise TypeError(f"Valor deve ser booleano (True/False)")
    
    def __str__(self):
        print(f"Onibus: "{self.placa})
        print(f"Assentos totais: len{self.assentos}")
        print(f"Assentos ocupados: {self.assentos.acont{True}}")
        print(f"Assentos ocupados: {self.assentos.acont{False}}")


