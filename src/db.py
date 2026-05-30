import sqlite3
import os
import click
from flask import g, current_app

def get_db():
    """
    Retorna a conexão ativa com o banco de dados SQLite.
    A conexão é armazenada no contexto de requisição do Flask (flask.g)
    para ser reutilizada durante uma mesma requisição.
    """
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE']
        )
        # Permite acessar colunas pelo nome (ex: row['title']) em vez de apenas índices
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    """
    Fecha a conexão com o banco de dados caso ela exista no contexto da requisição.
    Executada automaticamente pelo Flask ao final de cada requisição.
    """
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    """
    Inicializa o banco de dados executando as instruções do arquivo schema.sql.
    """
    db = get_db()
    
    # Localiza o arquivo schema.sql no mesmo diretório deste script
    schema_path = os.path.join(os.path.dirname(__file__), 'schema.sql')
    
    with open(schema_path, 'r', encoding='utf-8') as f:
        db.executescript(f.read())
    
    db.commit()

@click.command('init-db')
def init_db_command():
    """Limpa os dados existentes e cria novas tabelas (comando CLI)."""
    init_db()
    click.echo('Banco de dados inicializado com sucesso.')

def init_app(app):
    """
    Registra as funções de ciclo de vida do banco e comandos CLI na aplicação Flask.
    """
    # Registra a função para fechar o banco ao fim da requisição
    app.teardown_appcontext(close_db)
    # Adiciona o comando flask init-db
    app.cli.add_command(init_db_command)
