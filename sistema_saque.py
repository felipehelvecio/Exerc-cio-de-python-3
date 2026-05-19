saldo = 1000

while True:

    print("1 - Saldo")
    print("2 - Sacar")
    print("3 - Depositar")
    print("4 - Sair")

    opcao = input("Escolha: ")

    # =====================
    # VER SALDO
    # =====================

    if opcao == "1":

        print("Seu saldo é de R$", saldo)

    # =====================
    # SACAR
    # =====================

    elif opcao == "2":

        saque = float(input("Qual quantia você deseja sacar? R$ "))

        if saque <= saldo:

            saldo -= saque

            print("Seu saldo agora é de R$", saldo)
            print("Saque de R$", saque, "realizado com sucesso")

        else:

            print("Saldo insuficiente")

    # =====================
    # DEPOSITAR
    # =====================

    elif opcao == "3":

        deposito = float(input("Qual valor deseja depositar? R$ "))

        saldo += deposito

        print("Depósito realizado com sucesso")
        print("Seu saldo agora é de R$", saldo)

    # =====================
    # SAIR
    # =====================

    elif opcao == "4":

        print("Sistema encerrado")
        break

    # =====================
    # VALOR INVÁLIDO
    # =====================

    else:

        print("Valor inválido")
