def cadastra_usuario(lista: list, nome: str, senha: str) -> str:
    """
    Função Responsável por criar uma matriz de tamanho 2 ao adicionar uma sublista a lista passada.

    Args: lista(list[list]): onde cada usuário tem uma sublista com o name e password
    Args: name(str): o name do usuario a ser cadastrado
    Args: password(str): a password do usuario a ser cadastrado
    Returns:
        str: Uma mensagem indicando que o usuario foi cadastrado com sucesso
    """
    if ['', ''] in lista:  # verifica se tem na lista, uma sublista ['','']
        for i in lista:
            if i[0] == '' and i[1] == '':
                i[0] = nome
                i[1] = senha
    else:
        lista.append([nome, senha])
    return "Usuário Cadastrado com Sucesso!"


def listar_usuarios(lista: list[list[str]]):
    """
    Função responsável por percorrer a lista passada e exibir os indices dentro da lista principal e nas sublistas.
    """
    for indice, item in enumerate(lista):
        print(f"No índice {indice},está o usuário {item[0]}, com a senha {item[1]}")
    if len(lista) == 0:
        print("No momento não há nenhum usuário cadastrado!")


def login(lista: list[list[str]], nome: str, senha: str) -> bool and str:
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
    for user in lista:  # Percorre a lista
        if user[0] == nome:  # Verifica se o nome está na posição 0
            if user[1] == senha:  # Verifica se a senha está na posição 1
                return True, "Login efetuado com sucesso!"
            else:
                return False, "Senha incorreta!"
    return False, "Usuário não cadastrado!"


def deletar(lista: list[list[str]], nome: str, senha: str) -> str:
    """
    Função para deletar item da lista e vaga a posição que aquele item possuia
    Args: lista(list[list[str]]): Matriz com nome e senha de usuário
    Args: nome(str): nome do usuário
    Args: senha(str): senha do usuário

    Returns:
        str: retorna um texto de string
    """
    tamanho = len(lista)
    for i in range(tamanho):
        if lista[i][0] == nome:
            if lista[i][1] == senha:
                lista[i] = ['', '']  # Substitui os dados do usuário por valores vazios
                return "Usuário removido e espaço esvaziado."
            else:
                return "Senha incorreta."
    return "Usuário não encontrado"


def atualizar(lista: list[list[str]], nome: str, senha: str, novo_nome: str = None, novo_senha: str = None) -> str:
    """
    Função responsável por atualizar a matriz
    Args: lista(list[list[str, str]]): recebe uma matriz de nome e senha
    Args: nome(str): recebe o nome
    Args: senha(str): recebe a senha
    Args:novo_nome(str): recebe o novo nome caso exista
    Args:novo_senha(str): recebe a nova senha caso exista

    Returns:
        str: retorna uma mensagem de string
    """
    for item in lista:
        if item[0] == nome:
            if item[1] == senha:
                if novo_nome:
                    item[0] = novo_nome
                if novo_senha:
                    item[1] = novo_senha
                return "Dados atualizados com sucesso!"
            return "Senha incorreta!"
    return "Usuário não cadastrado"


def salvar(lista: list[list[str]]):
    with open('dados.txt', 'w+') as dados:
        for item in lista:
            for idx, i in enumerate(item):
                if i == '':  # Ignora itens vazios
                    pass
                elif idx == len(item) - 1:  # Se for o último item da lista
                    dados.write(f'{i};')
                else:
                    dados.write(f'{i},')  # Adiciona vírgula se não for o último item
            dados.write('\n')  # Adiciona uma nova linha após cada item da lista


def carregar() -> list[list[str]]:
    try:
        with open('dados.txt', 'r') as dados:
            lista = []
            for indice, linha in enumerate(dados):
                lista.append(linha.strip().split(','))
                lista[indice][1] = lista[indice][1][:-1]
        return lista
    except IOError:
        return []
