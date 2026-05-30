import os
from flask import Flask

def create_app(test_config=None):
    """
    Factory function para criar e configurar a instância da aplicação Flask.
    Configura os caminhos para templates e arquivos estáticos fora da pasta src.
    """
    # Encontra o caminho da raiz do projeto (um nível acima da pasta src)
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    template_dir = os.path.join(root_dir, 'templates')
    static_dir = os.path.join(root_dir, 'static')

    app = Flask(
        __name__, 
        instance_relative_config=True,
        template_folder=template_dir,
        static_folder=static_dir
    )

    # Configurações padrão da aplicação
    app.config.from_mapping(
        SECRET_KEY='dev_key_eng_software',
        DATABASE=os.path.join(app.instance_path, 'kanban.sqlite'),
    )

    if test_config is None:
        # Carrega as configurações do arquivo de instância, se houver
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Carrega configurações de teste
        app.config.from_mapping(test_config)

    # Garante que o diretório da instância (onde fica o SQLite) exista
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Inicializa o gerenciador do banco de dados (SQLite)
    from . import db
    db.init_app(app)

    # Registra o blueprint de rotas da aplicação
    from . import app as app_routes
    app.register_blueprint(app_routes.bp)

    return app
