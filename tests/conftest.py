import os
import tempfile
import pytest
from src import create_app
from src.db import init_db

@pytest.fixture
def app():
    """
    Fixture que cria uma instância da aplicação Flask configurada para testes.
    Cria um banco de dados SQLite temporário em disco para cada sessão de teste
    e o remove após a conclusão dos testes.
    """
    # Cria um arquivo temporário para o banco de dados
    db_fd, db_path = tempfile.mkstemp()
    
    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
        'SECRET_KEY': 'test_secret_key_123',
    })

    # Inicializa o banco de dados estruturando as tabelas
    with app.app_context():
        init_db()

    yield app

    # Remove o banco de dados temporário ao fim do teste
    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def client(app):
    """
    Fixture que fornece um cliente de teste do Flask para simular requisições HTTP.
    """
    return app.test_client()

@pytest.fixture
def runner(app):
    """
    Fixture que fornece um runner para testar comandos CLI do Flask (ex: init-db).
    """
    return app.test_cli_runner()
