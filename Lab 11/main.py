def main():
    print("Escolha o meio de pagamento:")
    print("1 - Cartão de Crédito")
    print("2 - Pix")
    print("3 - Boleto")
    opcao_meio = input("Opção: ")

    pagamento = None

    if opcao_meio == "1":
        numero = input("Informe o número do cartão de crédito: ")
        pagamento = CartaoCredito(numero)
    elif opcao_meio == "2":
        chave = input("Informe a chave Pix: ")
        pagamento = Pix(chave)
    elif opcao_meio == "3":
        codigo = input("Informe o código de barras do boleto: ")
        pagamento = Boleto(codigo)
    else:
        print("Opção inválida.")
        return

    while True:
        print("\n--- MENU ---")
        print("1 - Processar Pagamento")
        print("2 - Cancelar Pagamento")
        print("3 - Gerar Comprovante")
        print("4 - Sair")
        opcao_menu = input("Escolha uma opção: ")

        if opcao_menu == "1":
            pagamento.processar_pagamento()
        elif opcao_menu == "2":
            pagamento.cancelar_pagamento()
        elif opcao_menu == "3":
            pagamento.gerar_comprovante()
        elif opcao_menu == "4":
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()