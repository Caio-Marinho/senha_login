from function import cadastra_usuario, listar_usuarios, login

usarios_cadastrado = []
cont = 0
while cont < 3:
    menu = ['Cadastro', 'Mostrar Usuário', 'Login', 'Sair']
    print("Código\titem")
    for index, item in enumerate(menu):
        print(f'{index + 1}.{item}')
    try:
        opcao = int(input("Selecione o código opção que vc deseja: "))
    except ValueError:
        print("Informe somente o código!")
        continue
    match opcao:
        case 1:
            nome = input("Digite seu nome: ")
            senha = input("Digite sua senha: ")
            while senha == '':
                senha = input("A senha não pode ficar vazia,"
                              "Digite Novamente sua senha: ")
            while nome == '':
                nome = input("O seu nome não pode ficar vazio,"
                             "Digite Novamente seu nome: ")
            cadastro = cadastra_usuario(usarios_cadastrado, nome, senha)
            print(cadastro)
        case 2:
            listar_usuarios(usarios_cadastrado)
        case 3:
            print(f"você tem {3 - cont} de 3 tentativas para logar!")
            nome = input("Digite seu nome: ")
            senha = input("Digite sua senha: ")
            cond, texto = login(usarios_cadastrado, nome, senha)
            if not cond:
                print(texto)
                cont += 1
            else:
                print(texto)
                cont = 0
            if cont > 2:
                print(f"você tem {3 - cont} de 3 tentativas para logar!")
                print("Você atingiu o limite de tentativas!")
        case 4:
            print("Saindo...")
            break
