menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        valor_deposito = float(input("Insira o valor: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"+ R$ {valor_deposito:.2f}\n"
        else:
            print("Valor inválido")

    elif opcao == 's':
        if numero_saques < LIMITE_SAQUES:
            saque = float(input("Insira o valor: "))
            if saque > 0:
                if saque <= limite:
                    if saque <= saldo:
                        numero_saques += 1
                        saldo -= saque
                        extrato += f"- R$ {saque:.2f}\n"
                    else:
                        print("Não há saldo suficiente")
                else:
                    print("Limite de valor de saque excedido")
            else:
                print("Valor inválido")
        else:
            print("Número máximo de saques excedido")

    elif opcao == 'e':
        print("Extrato: ")
        print(extrato)
        print(f"Saldo: R$ {saldo:.2f}")

    elif opcao == 'q':
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")