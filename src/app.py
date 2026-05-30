from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from .db import get_db

# Blueprint que agrupa as rotas relacionadas a tarefas
bp = Blueprint('tasks', __name__)

def get_task_or_404(task_id):
    """
    Função auxiliar para recuperar uma tarefa pelo ID.
    Caso a tarefa não exista, interrompe a requisição com status 404 (Not Found).
    """
    db = get_db()
    task = db.execute(
        'SELECT id, title, description, status, priority, created_at '
        'FROM tasks '
        'WHERE id = ?',
        (task_id,)
    ).fetchone()
    
    if task is None:
        abort(404, f"Tarefa com ID {task_id} não encontrada.")
    
    return task

@bp.route('/')
def index():
    """
    Rota principal: exibe o painel Kanban.
    Busca todas as tarefas ordenadas por prioridade (Alta -> Média -> Baixa)
    e depois por data de criação. Em seguida, divide-as nas colunas correspondentes.
    """
    db = get_db()
    cursor = db.execute(
        'SELECT id, title, description, status, priority, created_at '
        'FROM tasks '
        'ORDER BY '
        '  CASE priority '
        '    WHEN "Alta" THEN 1 '
        '    WHEN "Média" THEN 2 '
        '    WHEN "Baixa" THEN 3 '
        '    ELSE 4 '
        '  END, '
        '  created_at DESC'
    )
    tasks = cursor.fetchall()

    # Divisão das tarefas por coluna do Kanban
    todo_tasks = [t for t in tasks if t['status'] == 'Pendente']
    doing_tasks = [t for t in tasks if t['status'] == 'Em Andamento']
    done_tasks = [t for t in tasks if t['status'] == 'Concluído']

    return render_template(
        'index.html', 
        todo=todo_tasks, 
        doing=doing_tasks, 
        done=done_tasks
    )

@bp.route('/tarefa/nova', methods=('GET', 'POST'))
def nova():
    """
    Rota para criação de novas tarefas.
    - GET: Renderiza o formulário vazio.
    - POST: Valida as informações e salva no banco de dados.
    """
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        priority = request.form.get('priority', '').strip()
        status = request.form.get('status', '').strip()

        # Validação simples de campos obrigatórios e valores válidos
        error = None
        if not title:
            error = 'O título da tarefa é obrigatório.'
        elif priority not in ('Baixa', 'Média', 'Alta'):
            error = 'A prioridade fornecida é inválida.'
        elif status not in ('Pendente', 'Em Andamento', 'Concluído'):
            error = 'O status fornecido é inválido.'

        if error is not None:
            flash(error, 'danger')
        else:
            db = get_db()
            db.execute(
                'INSERT INTO tasks (title, description, priority, status) '
                'VALUES (?, ?, ?, ?)',
                (title, description, priority, status)
            )
            db.commit()
            flash('Tarefa criada com sucesso!', 'success')
            return redirect(url_for('tasks.index'))

    return render_template('tarefa.html', tarefa=None)

@bp.route('/tarefa/editar/<int:id>', methods=('GET', 'POST'))
def editar(id):
    """
    Rota para edição de uma tarefa existente.
    - GET: Recupera a tarefa no banco e renderiza o formulário preenchido.
    - POST: Valida os novos dados e atualiza a tarefa no banco.
    """
    tarefa = get_task_or_404(id)

    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        priority = request.form.get('priority', '').strip()
        status = request.form.get('status', '').strip()

        # Validação simples
        error = None
        if not title:
            error = 'O título da tarefa é obrigatório.'
        elif priority not in ('Baixa', 'Média', 'Alta'):
            error = 'A prioridade fornecida é inválida.'
        elif status not in ('Pendente', 'Em Andamento', 'Concluído'):
            error = 'O status fornecido é inválido.'

        if error is not None:
            flash(error, 'danger')
        else:
            db = get_db()
            db.execute(
                'UPDATE tasks '
                'SET title = ?, description = ?, priority = ?, status = ? '
                'WHERE id = ?',
                (title, description, priority, status, id)
            )
            db.commit()
            flash('Tarefa atualizada com sucesso!', 'success')
            return redirect(url_for('tasks.index'))

    return render_template('tarefa.html', tarefa=tarefa)

@bp.route('/tarefa/deletar/<int:id>', methods=('POST',))
def deletar(id):
    """
    Rota para excluir uma tarefa.
    Exige requisição POST por questões de segurança (evitar deleção acidental via links GET).
    """
    get_task_or_404(id) # Valida existência da tarefa
    
    db = get_db()
    db.execute('DELETE FROM tasks WHERE id = ?', (id,))
    db.commit()
    
    flash('Tarefa excluída com sucesso!', 'success')
    return redirect(url_for('tasks.index'))

@bp.route('/tarefa/mover/<int:id>', methods=('POST',))
def mover(id):
    """
    Rota de atalho rápido para mover tarefas entre as colunas do Kanban.
    Permite transições rápidas (ex: mover de Pendente para Em Andamento).
    """
    get_task_or_404(id) # Valida existência da tarefa
    novo_status = request.form.get('status', '').strip()

    if novo_status not in ('Pendente', 'Em Andamento', 'Concluído'):
        flash('Status de destino inválido.', 'danger')
    else:
        db = get_db()
        db.execute(
            'UPDATE tasks SET status = ? WHERE id = ?',
            (novo_status, id)
        )
        db.commit()
        flash('Tarefa movida com sucesso!', 'success')

    return redirect(url_for('tasks.index'))
