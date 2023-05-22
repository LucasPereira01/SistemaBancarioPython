menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Digite o valor do deposito '))
        if valor <= 0:
            print('Operacão falhou! o Valor informado é invalido')
        else:
            saldo += valor
            extrato += f"deposito: R$ {valor:.2f}\n"

    if opcao == 's':
        valor = float(input('Digite o valor do saque '))

        excedeu_saldo = valor > saldo
        excedey_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print('Operação falhou! Voce nao tem saldo suficiente.')
        elif excedey_limite:
            print('Operação falhou! O valor do saque excede o limite.')
        elif excedeu_saques:
            print('Operação falhou! Numero maximo de saques excedido.')
        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.3f}\n"
            numero_saques +=1
        else:
            print('Operação falhou! o valor informado é invalido.')
            

    if opcao == 'e':
        print("\n================== EXTRATO ================")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nsaldo: R$ {saldo:.2f}")
        print("===========================================")
        
    if opcao == 'q':
        print("Fim da Operação")
        break
