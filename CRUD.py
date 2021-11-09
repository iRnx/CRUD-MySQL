import mysql.connector


def conectar():
    """
    Função para conectar ao servidor
    """
    try:
        conn = mysql.connector.connect(
            host='localhost',
            database='python',
            user='root',
            password='SUA SENHA')
        return conn

    except mysql.connector.Error as e:
        print(f'Erro na conexão ao MySQL Server {e}')


def desconectar(conn):
    """
    Função para desconectar do servidor.
    """
    if conn:
        conn.close()


def listar():
    """
    Função para listar os produtos
    """
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos')  # O python vai receber o resultado como uma tupla e podemos usar indices #
    produtos = cursor.fetchall()   # produtos vai receber o select e todas as linhas (fetchall) em formato de tuplas #

    if len(produtos) > 0:       # verificar se produtos esta cheia ou vazia #
        print('Listando produtos...')
        print('---------------------')
        for produto in produtos:     # O python vai receber o resultado como tupla. #
            print(f'ID: {produto[0]}')
            print(f'Produto: {produto[1]}')
            print(f'Preço: {produto[2]}')
            print(f'Estoque: {produto[3]}')
            print('---------------------')

    else:
        print('Não existem produtos cadastrados.')
    desconectar(conn)


def inserir():
    """
    Função para inserir um produto
    """

    nome = str(input('Informe o nome do produto: '))
    preco = float(input('Informe o preço do produto: '))
    estoque = int(input('Informe a quantidade em estoque: '))

    conn = conectar()
    cursor = conn.cursor()
    injetar = f"""INSERT INTO produtos
              (nome, preco, estoque)
              VALUES
              ('{nome}', {preco}, {estoque})"""
    cursor.execute(injetar)
    conn.commit()
    if cursor.rowcount == 1:
        print(f'O produto {nome} foi inserido com sucesso.')
    else:
        print('Não foi possível inserir o produto.')
    desconectar(conn)


def atualizar():
    """
    Função para atualizar um produto
    """
    conn = conectar()
    cursor = conn.cursor()

    codigo = int(input('Informe o código do produto: '))
    nome = str(input('Informe o novo nome do produto: '))
    preco = float(input('Informe o novo preço do produto: '))
    estoque = int(input('Informe a nova quantidade em estoque: '))
    att = f"""UPDATE produtos
             SET nome ='{nome}', preco={preco}, estoque ={estoque}
             WHERE id={codigo}"""

    cursor.execute(att)
    conn.commit()

    if cursor.rowcount == 1:
        print(f'O produto {nome} foi atualizado com sucesso.')
    else:
        print('Erro ao atualizar o produto.')
    desconectar(conn)


def deletar():
    """
    Função para deletar um produto
    """
    conn = conectar()
    cursor = conn.cursor()

    codigo = int(input('Informe o código do produto: '))
    apagar = f"""
              DELETE FROM produtos WHERE id={codigo}"""
    cursor.execute(apagar)
    conn.commit()

    if cursor.rowcount == 1:
        print('Produto excluído com sucesso.')
    else:
        print(f'Erro ao excluir o produto com id={codigo}')
    desconectar(conn)


def menu():
    """
    Função para gerar o menu inicial
    """
    while True:
        print('=========Gerenciamento de Produtos==============')
        print('Selecione uma opção: ')
        print('1 - Listar produtos.')
        print('2 - Inserir produtos.')
        print('3 - Atualizar produto.')
        print('4 - Deletar produto.')
        print('5 - Para Sair')
        opcao = int(input('Digite um numero: '))
        if opcao in [1, 2, 3, 4, 5]:
            if opcao == 1:
                listar()
            elif opcao == 2:
                inserir()
            elif opcao == 3:
                atualizar()
            elif opcao == 4:
                deletar()
            elif opcao == 5:
                exit()
            else:
                print('Opção inválida')
        else:
            print('Opção inválida')


if __name__ == '__main__':
    menu()
