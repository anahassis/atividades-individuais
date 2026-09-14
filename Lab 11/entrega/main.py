def main():
    entregas = []

    while True:
        print("\n--- MENU ---")
        print("1 - Criar nova entrega")
        print("2 - Listar entregas")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            tipo = input("Tipo de entrega (1 - Terrestre, 2 - Aérea): ")
            endereco = input("Endereço de destino: ")
            status = input("Status (em separação, a caminho, entregue): ")
            peso = float(input("Peso: "))

            if tipo == "1":
                distancia = float(input("Distância em km: "))
                entrega = EntregaTerrestre(endereco, status, peso, distancia)
                entregas.append(entrega)
            elif tipo == "2":
                taxa = float(input("Taxa de despacho: "))
                entrega = EntregaAerea(endereco, status, peso, taxa)
                entregas.append(entrega)

        elif opcao == "2":
            for entrega in entregas:
                print("-------------------")
                entrega.imprimir_dados()

        elif opcao == "3":
            break


if __name__ == "__main__":
    main()