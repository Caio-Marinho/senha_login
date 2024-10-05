
def cadastra_usuario(lista: list[list[str]], name: str, password: str) -> str:
    """
    Função Responsável por criar uma matriz de tamanho 2 ao adicionar uma sublista a lista passada.

    Args: lista(list[list]): onde cada usuário tem uma sublista com o name e password
    Args: name(str): o name do usuario a ser cadastrado
    Args: password(str): a password do usuario a ser cadastrado
    Returns:
        str: Uma mensagem indicando que o usuario foi cadastrado com sucesso
    """
    tamanho_sublista = len(lista[0])
    for j in range(tamanho_sublista):
        if lista[0][j] == '':
            lista[0][j] = name
            lista[1][j] = password
            return "Usuário Cadastrado com Sucesso!"
    return "Erro: Não há espaço disponível para cadastrar o usuário."


def listar_usuarios(lista: list[list[str]]):
    """
    Função responsável por percorrer a lista passada e exibir os indices dentro da lista principal e nas sublistas.
    """
    conte = 0
    tamanho_sublista = len(lista[0])
    for indice in range(tamanho_sublista):
        if lista[0][indice] != '' and lista[1][indice] != '':
            print(f"No índice {indice},está o usuário {lista[0][indice]}, com a senha {lista[1][indice]}")
            conte += 1
    if conte == 0:
        print("No momento não há nenhum usuário cadastrado!")


def login(lista: list[list[str]], name: str, password: str) -> bool and str:
    """
    Função para realizar o login de um usuário.

    Args: lista (list): Uma lista de tuplas, onde cada tupla contém dois elementos:
                  o name do usuário (str) e a password (str).
    Args: name (str): O name do usuário que está tentando fazer login.
    Args: password (str): A password fornecida pelo usuário para autenticação.

    Returns:
        tuple: um par (bool, str) onde o primeiro elemento indica se o login foi
           bem-sucedido (True) ou não (False), e o segundo elemento é uma
           mensagem de texto explicando o resultado do login.
    """
    tamanho_sublista = len(lista[0])
    for user in range(tamanho_sublista):
        if lista[0][user] == name:
            if lista[1][user] == password:
                return True, "Login efetuado com sucesso!"
            else:
                return False, "Senha incorreta!"
    return False, "Usuário não cadastrado!"


nomes = [''] * 5
senhas = [''] * 5
usuarios_cadastrados = [nomes, senhas]
print(usuarios_cadastrados)
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
