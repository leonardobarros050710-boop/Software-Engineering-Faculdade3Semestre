from src.db import get_db

def test_index(client):
    """
    Testa se a página inicial carrega corretamente e exibe o título do Kanban.
    """
    response = client.get('/')
    assert response.status_code == 200
    assert b'Painel de Tarefas Kanban' in response.data
    assert b'A Fazer' in response.data
    assert b'Em Andamento' in response.data
    assert b'Concluido' in response.data or b'Conclu\xc3\xaddo' in response.data

def test_create_task(client, app):
    """
    Testa o fluxo completo de criação de uma tarefa com prioridade e status.
    """
    # 1. Acessa o formulário de criação
    response = client.get('/tarefa/nova')
    assert response.status_code == 200
    assert b'Nova Tarefa no Quadro' in response.data

    # 2. Envia o formulário de criação de tarefa
    response = client.post('/tarefa/nova', data={
        'title': 'Testar funcionalidade de prioridades',
        'description': 'Garantir que a prioridade seja exibida e salva corretamente no SQLite.',
        'priority': 'Alta',
        'status': 'Pendente'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b'Tarefa criada com sucesso!' in response.data
    assert b'Testar funcionalidade de prioridades' in response.data

    # 3. Valida no banco de dados se a tarefa realmente foi inserida
    with app.app_context():
        db = get_db()
        task = db.execute('SELECT * FROM tasks WHERE title = ?', ('Testar funcionalidade de prioridades',)).fetchone()
        assert task is not None
        assert task['description'] == 'Garantir que a prioridade seja exibida e salva corretamente no SQLite.'
        assert task['priority'] == 'Alta'
        assert task['status'] == 'Pendente'

def test_create_task_validation(client, app):
    """
    Testa se o sistema valida e impede a criação de tarefas sem título.
    """
    # Envia dados inválidos (título em branco)
    response = client.post('/tarefa/nova', data={
        'title': '   ',
        'description': 'Sem título',
        'priority': 'Média',
        'status': 'Pendente'
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'O t\xc3\xadtulo da tarefa \xc3\xa9 obrigat\xc3\xb3rio.' in response.data or b'titulo da tarefa' in response.data

    # Garante que nenhum registro foi criado
    with app.app_context():
        db = get_db()
        count = db.execute('SELECT COUNT(*) FROM tasks').fetchone()[0]
        assert count == 0

def test_edit_task(client, app):
    """
    Testa a edição de uma tarefa cadastrada, validando as atualizações no banco.
    """
    # 1. Cria uma tarefa inicial diretamente no banco
    with app.app_context():
        db = get_db()
        db.execute(
            'INSERT INTO tasks (title, description, priority, status) VALUES (?, ?, ?, ?)',
            ('Tarefa Inicial', 'Descrição Inicial', 'Baixa', 'Pendente')
        )
        db.commit()
        tarefa_id = db.execute('SELECT id FROM tasks').fetchone()['id']

    # 2. Testa o GET para a rota de edição
    response = client.get(f'/tarefa/editar/{tarefa_id}')
    assert response.status_code == 200
    assert b'Editar Tarefa' in response.data
    assert b'Tarefa Inicial' in response.data

    # 3. Envia o POST com dados atualizados (mudando prioridade e descrição)
    response = client.post(f'/tarefa/editar/{tarefa_id}', data={
        'title': 'Tarefa Editada',
        'description': 'Descrição Nova',
        'priority': 'Alta',
        'status': 'Em Andamento'
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'Tarefa atualizada com sucesso!' in response.data
    assert b'Tarefa Editada' in response.data

    # 4. Verifica se os novos valores foram aplicados no banco
    with app.app_context():
        db = get_db()
        task = db.execute('SELECT * FROM tasks WHERE id = ?', (tarefa_id,)).fetchone()
        assert task['title'] == 'Tarefa Editada'
        assert task['description'] == 'Descrição Nova'
        assert task['priority'] == 'Alta'
        assert task['status'] == 'Em Andamento'

def test_delete_task(client, app):
    """
    Testa se a exclusão de tarefa deleta o registro no banco de dados.
    """
    # 1. Cria tarefa inicial
    with app.app_context():
        db = get_db()
        db.execute(
            'INSERT INTO tasks (title, description, priority, status) VALUES (?, ?, ?, ?)',
            ('Tarefa para Deletar', 'Será excluída em breve', 'Média', 'Pendente')
        )
        db.commit()
        tarefa_id = db.execute('SELECT id FROM tasks').fetchone()['id']

    # 2. Envia requisição de exclusão (POST)
    response = client.post(f'/tarefa/deletar/{tarefa_id}', follow_redirects=True)
    assert response.status_code == 200
    assert b'Tarefa exclu\xc3\xadda com sucesso!' in response.data or b'excluida com sucesso' in response.data

    # 3. Confirma se o registro foi removido do banco
    with app.app_context():
        db = get_db()
        task = db.execute('SELECT * FROM tasks WHERE id = ?', (tarefa_id,)).fetchone()
        assert task is None

def test_move_task_flow(client, app):
    """
    Testa a rota rápida de transição de status (Kanban flow controls).
    """
    # 1. Insere tarefa "Pendente"
    with app.app_context():
        db = get_db()
        db.execute(
            'INSERT INTO tasks (title, priority, status) VALUES (?, ?, ?)',
            ('Tarefa Kanban', 'Média', 'Pendente')
        )
        db.commit()
        tarefa_id = db.execute('SELECT id FROM tasks').fetchone()['id']

    # 2. Move de "Pendente" para "Em Andamento"
    response = client.post(f'/tarefa/mover/{tarefa_id}', data={'status': 'Em Andamento'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Tarefa movida com sucesso!' in response.data
    
    with app.app_context():
        db = get_db()
        assert db.execute('SELECT status FROM tasks WHERE id = ?', (tarefa_id,)).fetchone()['status'] == 'Em Andamento'

    # 3. Move de "Em Andamento" para "Concluído"
    response = client.post(f'/tarefa/mover/{tarefa_id}', data={'status': 'Concluído'}, follow_redirects=True)
    assert response.status_code == 200
    
    with app.app_context():
        db = get_db()
        assert db.execute('SELECT status FROM tasks WHERE id = ?', (tarefa_id,)).fetchone()['status'] == 'Concluído'

def test_nonexistent_task(client):
    """
    Testa se rotas para tarefas inexistentes retornam status 404 (Not Found).
    """
    response = client.get('/tarefa/editar/999')
    assert response.status_code == 404

    response = client.post('/tarefa/deletar/999')
    assert response.status_code == 404
