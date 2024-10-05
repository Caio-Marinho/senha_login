from function import cadastra_usuario, listar_usuarios, login

usuarios_cadastrados = []
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
            nome = input("Digite seu name: ")
            senha = input("Digite sua password: ")
            while senha == '':
                senha = input("A password não pode ficar vazia,"
                              "Digite Novamente sua password: ")
            while nome == '':
                nome = input("O seu name não pode ficar vazio,"
                             "Digite Novamente seu name: ")
            cadastro = cadastra_usuario(usuarios_cadastrados, nome, senha)
            print(cadastro)
        case 2:
            listar_usuarios(usuarios_cadastrados)
        case 3:
            print(f"você tem {3 - cont} de 3 tentativas para logar!")
            nome = input("Digite seu name: ")
            senha = input("Digite sua password: ")
            cond, texto = login(usuarios_cadastrados, nome, senha)
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
