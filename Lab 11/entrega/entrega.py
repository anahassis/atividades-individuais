from abc import ABC, abstractmethod


class Entrega(ABC):
    def __init__(self, endereco_destino, status, peso):
        self.endereco_destino = endereco_destino
        self.status = status
        self.peso = peso

    def atualizar_status(self, status):
        self.status = status

    def imprimir_dados(self):
        print(f"Endereço de Destino: {self.endereco_destino}")
        print(f"Status: {self.status}")
        print(f"Peso: {self.peso}")

    @abstractmethod
    def calcular_frete(self):
        pass


class EntregaTerrestre(Entrega):
    def __init__(self, endereco_destino, status, peso, distancia_km):
        super().__init__(endereco_destino, status, peso)
        self.distancia_km = distancia_km

    def calcular_frete(self):
        if self.distancia_km <= 100:
            return 20.0
        elif self.distancia_km <= 500:
            return 40.0 + 1.50 * self.peso
        else:
            return 70.0 + 2.20 * self.peso

    def imprimir_dados(self):
        super().imprimir_dados()
        print(f"Distância (km): {self.distancia_km}")
        print(f"Frete: {self.calcular_frete()}")


class EntregaAerea(Entrega):
    def __init__(self, endereco_destino, status, peso, taxa_despacho):
        super().__init__(endereco_destino, status, peso)
        self.taxa_despacho = taxa_despacho

    def calcular_frete(self):
        return self.taxa_despacho + 12.0 * self.peso

    def imprimir_dados(self):
        super().imprimir_dados()
        print(f"Taxa de Despacho: {self.taxa_despacho}")
        print(f"Frete: {self.calcular_frete()}")