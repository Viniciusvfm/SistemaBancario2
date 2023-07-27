import textwrap
def menu():
    menu = """\n
    ============= MENU ============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [x]\tSair
    =>"""
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Deposito R$ {valor:.2f}\n'
    else:
        print('Operação falhou!! O valor digitado não é valido')

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques= numero_saques >= limite_saques

    if excedeu_saldo:
        print('Operação falhou, você esta sem saldo')
    elif excedeu_limite:
        print('Operação falhou! Você excedeu o valor limite de saque por dia')
    elif excedeu_saques:
        print('Operação falhou! Você excedeu a quantidade de saques por dia ')
    elif valor > 0:
        saldo -= valor
        extrato += f'saque R$ {valor:.2f}\n'
        numero_saques += 1
    else:
        print('Operação falhou! valor informado invalido')

    return saldo, extrato


def exibir_extrato(saldo, /,*, extrato):
    print('\n==============EXTRATO============')
    print('Não houve movimentações bancarias'if not extrato else extrato)
    print(f'\nSaldo:\t\tR$ {saldo:.2f}')
    print('=================================')


def criar_usuario(usuarios):
    cpf = input('Informe o CPF (Somente números)')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n Já existe usuário com esse CPF')
        return
    
    nome = input('Informe o nome completo:')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa):')
    endereco = input('Informe o endereço (Logradouro, nro - bairro - cidade/sigla estado):')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf':cpf, 'endereco': endereco})

    print('===Usuárioo criado com sucesso"==')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_contas(agencia, numero_conta, usuarios):
    cpf= input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n==Conta criada com sucesso! ==')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    
    print('\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@')

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['none']}
        """
        print('=' *100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []


    while True:
        opcao = menu()

        if opcao == 'd':
            valor = float(input('Digite o valor do deposito'))
    
        elif opcao == 's':
            valor = float(input('Informe o valor do saque '))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,



            )
            
        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)
    
        elif opcao == 'nu':
            criar_usuario(usuarios)

        elif opcao == 'nc':
            numero_conta = len(contas) -1
            conta = criar_contas(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)
    
        elif opcao == 'lc':
            listar_contas(contas)

        elif opcao == 'x':
            break

        else:
            print('Opção invalida')


main()