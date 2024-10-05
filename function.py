def cadastra_usuario(lista: list, nome: str, senha: str) -> str:
    """
    Função Responsável por criar uma matriz de tamanho 2 ao adicionar uma sublista a lista passada.

    Args: lista(list[list]): onde cada usuário tem uma sublista com o name e password
    Args: name(str): o name do usuario a ser cadastrado
    Args: password(str): a password do usuario a ser cadastrado
    Returns:
        str: Uma mensagem indicando que o usuario foi cadastrado com sucesso
    """
    lista.append([nome, senha])
    return "Usuário Cadastrado com Sucesso!"


def listar_usuarios(lista: list[list[str, str]]):
    """
    Função responsável por percorrer a lista passada e exibir os indices dentro da lista principal e nas sublistas.
    """
    for indice, item in enumerate(lista):
        print(f"No índice {indice},está o usuário {item[0]}, com a senha {item[1]}")
    if len(lista) == 0:
        print("No momento não há nenhum usuário cadastrado!")


def login(lista: list[list[str, str]], nome: str, senha: str) -> bool and str:
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
    for user in lista:
        if user[0] == nome:
            if user[1] == senha:
                return True, "Login efetuado com sucesso!"
            else:
                return False, "Senha incorreta!"
    return False, "Usuário não cadastrado!"
