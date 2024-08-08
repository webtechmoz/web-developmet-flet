from manage_sql import MYSQL

db = MYSQL(
    host='localhost',
    database='users',
    user='root',
    password='Alex756545!'
)
nomeTabela='usuarios'
colunas=['nome', 'username', 'email', 'password', 'status']

def criar_tabela():
    db.criarTabela(
        nomeTabela=nomeTabela,
        Colunas=colunas,
        ColunasTipo=['VARCHAR(32)','VARCHAR(32)','VARCHAR(32)','VARCHAR(255)','VARCHAR(8)']
    )

def inserir_dados(dados: list):
    criar_tabela()

    db.inserirDados(
        nomeTabela=nomeTabela,
        Colunas=colunas,
        dados=dados
    )

def ver_dados(condition: str = ''):
    criar_tabela()

    dados = db.verDados(
        nomeTabela=nomeTabela,
        conditions=condition
    )

    return dados