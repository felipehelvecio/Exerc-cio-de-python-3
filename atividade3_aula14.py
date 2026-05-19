saldo = 500
arroz = 25
refri = 8
carne = 90

while True:

    print("1 - Ver saldo")
    print("2 - Comprar arroz")
    print("3 - Comprar refrigerante")
    print("4 - Comprar carne")
    print("5 - Sair")

    opcao = input("Escolha a opção desejada: ")

    # =====================
    # VER SALDO
    # =====================

    if opcao == "1":

        print("Seu saldo atual é de: R$", saldo)

    # =====================
    # COMPRAR ARROZ
    # =====================

    elif opcao == "2":

        quantidade = int(input("Quantas unidades?: "))

        comprar1 = arroz * quantidade

        if comprar1 <= saldo:

            saldo -= comprar1

            print("Valor da compra:", comprar1)
            print("Saldo atual:", saldo)

        else:

            print("Sem saldo")

    # =====================
    # COMPRAR REFRIGERANTE
    # =====================

    elif opcao == "3":

        quantidade = int(input("Quantas unidades?: "))

        comprar2 = refri * quantidade

        if comprar2 <= saldo:

            saldo -= comprar2
            print("Valor da compra:", comprar2)
            print("Saldo atual:", saldo)

        else:

            print("Sem saldo")
    
    # =====================
    # COMPRAR CARNE
    # =====================

    elif opcao == "4":

        quantidade = int(input("Quantas unidades?: "))

        comprar3 = carne * quantidade

        if comprar3 <= saldo:

            saldo -= comprar3
            print("Valor da compra:", comprar3)
            print("Saldo atual:", saldo)

        else:

            print("Sem saldo")        

    # =====================
    # SAIR
    # =====================

    elif opcao == "5":

        break  
