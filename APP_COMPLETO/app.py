from function import *

usuarios_cadastrados = carregar()
cont = 0
while cont < 3:
    menu = ['Cadastro', 'Mostrar Usuário', 'Login', 'Deletar', 'Atualizar', 'Sair']
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
            salvar(usuarios_cadastrados)
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
            nome = input("Digite seu name: ")
            senha = input("Digite sua password: ")
            delete = deletar(usuarios_cadastrados, nome, senha)
            print(delete)
            salvar(usuarios_cadastrados)
        case 5:
            nome = input("Digite seu name: ")
            senha = input("Digite sua password: ")
            while True:
                dados_atualizar = input("Deseja atualizar [N]nome, [S]senha ou [A] ambos? ")
                if dados_atualizar not in ['N', 'S', 'A']:
                    print("Informe uma Opção valida entre as oferecidas")
                else:
                    break
            if dados_atualizar == 'N':
                novo_nome = input("Digite seu novo nome: ")
                atualizado = atualizar(usuarios_cadastrados, nome, senha, novo_nome=novo_nome)
                print(atualizado)
            elif dados_atualizar == 'S':
                nova_senha = input("Digite sua nova senha: ")
                atualizado = atualizar(usuarios_cadastrados, nome, senha, novo_senha=nova_senha)
                print(atualizado)
            else:
                novo_nome = input("Digite seu novo nome: ")
                nova_senha = input("Digite sua nova senha: ")
                atualizado = atualizar(usuarios_cadastrados, nome, senha, novo_nome, nova_senha)
                print(atualizado)
                salvar(usuarios_cadastrados)
        case 6:
            print("Saindo...")
            break
        case _:
            print("Digite um dos códigos informados.")
