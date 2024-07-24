def deposito(valor_deposito, saldo, extrato, /):
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"+ R$ {valor_deposito:.2f}\n"
    else:
        print("Valor inválido")
    return saldo, extrato

def saque(*, valor_saque, limite, saldo, numero_saques, extrato):
    if valor_saque > 0:
        if valor_saque <= limite:
            if valor_saque <= saldo:
                numero_saques += 1
                saldo -= valor_saque
                extrato += f"- R$ {valor_saque:.2f}\n"
            else:
                print("Não há saldo suficiente")
        else:
            print("Limite de valor de saque excedido")
    else:
        print("Valor inválido")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("Extrato: ")
    print(extrato)
    print(f"Saldo: R$ {saldo:.2f}")

def criar_usuario(usuarios):
    nome = input("Insira o nome: ")
    data_de_nascimento = input("Insira a data de nascimento: ")
    cpf = input("Insira o CPF: ")
    for i in usuarios:
        if i["cpf"] == cpf:
            print("CPF já cadastrado")
            return
    print("Insira o endereço")
    logradouro = input("Logradouro: ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    endereco = f"{logradouro}, {numero} - {bairro} - {cidade}/{estado}"
    novo_usuario = {"nome" : nome, "data de nascimento" : data_de_nascimento, "cpf" : cpf, "endereco" : endereco}
    usuarios.append(novo_usuario)
    print("Usuário registrado com sucesso.")

def criar_conta_corrente(contas, usuarios):
    agencia = "0001"
    numero_da_conta = len(contas) + 1
    cpf_usuario = input("Insira o CPF do titular: ")
    for i in usuarios:
        if i["cpf"] == cpf_usuario:
            contas.append({"agencia": agencia, "numero_da_conta" : int(numero_da_conta), "usuario" : cpf_usuario})
            print("Conta aberta com sucesso.")
            return
    print("Erro: Usuário não cadastrado")

def exibir_usuario(usuarios, cpf):
    for i in usuarios:
        if i["cpf"] == cpf:
            print(i)
            return
    print("Não há usuário cadastrado com o CPF informado")

def exibir_conta(contas, numero):
    if numero <= 0:
        print("Número de conta inválido")
        return
    if len(contas) >= numero - 1:
        print(contas[numero - 1])
        return
    print("Não há conta com o número informado")

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[nu] Criar novo usuário
[nc] Criar nova conta corrente
[eu] Exibir dados de usuário
[ec] Exibir dados de conta corrente
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
valor_deposito = 0
usuarios = []
contas = []

while True:

    opcao = input(menu)

    if opcao == 'd':
        valor_deposito = float(input("Insira o valor: "))
        saldo, extrato = deposito(valor_deposito, saldo, extrato)

    elif opcao == 's':
        if numero_saques < LIMITE_SAQUES:
            valor_saque = float(input("Insira o valor: "))
            saldo, extrato, numero_saques = saque(valor_saque = valor_saque, limite = limite, saldo = saldo, numero_saques = numero_saques, extrato = extrato)
        else:
            print("Número máximo de saques excedido")

    elif opcao == 'e':
        exibir_extrato(saldo, extrato = extrato)

    elif opcao == "nu":
        criar_usuario(usuarios)

    elif opcao == "nc":
        criar_conta_corrente(contas, usuarios)
    
    elif opcao == "eu":
        cpf_pesquisa = input("Insira o CPF do usuário desejado: ")
        exibir_usuario(usuarios, cpf_pesquisa)
    
    elif opcao == "ec":
        numero_pesquisa = int(input("Insira o número da conta desejada: "))
        exibir_conta(contas, numero_pesquisa)

    elif opcao == 'q':
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")