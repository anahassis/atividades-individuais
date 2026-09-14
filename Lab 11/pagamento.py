from abc import ABC, abstractmethod


class MeioDePagamento(ABC):
    def __init__(self, status="pendente"):
        self.status = status

    @abstractmethod
    def processar_pagamento(self):
        pass

    @abstractmethod
    def cancelar_pagamento(self):
        pass

    @abstractmethod
    def gerar_comprovante(self):
        pass


class CartaoCredito(MeioDePagamento):
    def __init__(self, numero_cartao, status="pendente"):
        super().__init__(status)
        self.numero_cartao = str(numero_cartao)

    def processar_pagamento(self):
        self.status = "aprovado"
        print("Pagamento processado via cartão de crédito.")

    def cancelar_pagamento(self):
        self.status = "cancelado"
        print("Pagamento foi cancelado.")

    def gerar_comprovante(self):
        if self.status == "aprovado":
            ultimos_4 = self.numero_cartao[-4:]
            print(f"comprovante gerado para o cartão número: {ultimos_4}")
        elif self.status == "cancelado":
            print("Pagamento cancelado.")
        else:
            print("Pagamento pendente. Nenhum comprovante gerado.")


class Pix(MeioDePagamento):
    def __init__(self, chave_pix, status="pendente"):
        super().__init__(status)
        self.chave_pix = chave_pix

    def processar_pagamento(self):
        self.status = "aprovado"
        print(f"Aguardando pagamento para a seguinte chave Pix: {self.chave_pix}")

    def cancelar_pagamento(self):
        print("Operação Pix não pode ser cancelada.")

    def gerar_comprovante(self):
        print("comprovante gerado")


class Boleto(MeioDePagamento):
    def __init__(self, codigo_de_barras, status="pendente"):
        super().__init__(status)
        self.codigo_de_barras = codigo_de_barras

    def processar_pagamento(self):
        self.status = "aprovado"
        print(f"Aguardando pagamento para o boleto de código: {self.codigo_de_barras}")

    def cancelar_pagamento(self):
        self.status = "cancelado"
        print("Boleto cancelado")

    def gerar_comprovante(self):
        if self.status == "aprovado":
            print("comprovante gerado")
        elif self.status == "cancelado":
            print("Pagamento foi cancelado.")
        else:
            print("Pagamento pendente. Nenhum comprovante gerado.")


# main.py
