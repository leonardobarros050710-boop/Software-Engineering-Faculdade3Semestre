
# KanbanFlow - Sistema de Gerenciamento Ágil de Tarefas

Trabalho prático desenvolvido para a disciplina de **Engenharia de Software**. O projeto consiste em uma aplicação web didática que implementa um quadro Kanban funcional utilizando o framework Flask para o back-end, SQLite para o banco de dados e testes automatizados com Pytest integrado ao GitHub Actions.

---

## 🎯 Objetivo

O objetivo deste projeto é demonstrar a aplicação prática de conceitos fundamentais de Engenharia de Software, tais como:
1. **Desenvolvimento Baseado em Metodologias Ágeis (Kanban)**.
2. **Arquitetura Web Limpa** com separação de responsabilidades (View, Controller e persistência).
3. **Persistência de Dados Relacional** utilizando SQLite.
4. **Garantia de Qualidade de Software** por meio de testes unitários e de integração automatizados.
5. **Integração Contínua (CI)** integrando automação de testes com o GitHub Actions.

---

## 📋 Escopo do Sistema

O sistema é focado no controle do fluxo de tarefas (Work Items) de uma equipe de desenvolvimento, contendo as seguintes funcionalidades:
* **Criar Tarefas:** Registro de novas atividades contendo Título, Descrição, Status inicial e Prioridade.
* **Listar Tarefas (Quadro Kanban):** Exibição das tarefas em 3 colunas de progresso (*A Fazer*, *Em Andamento* e *Concluído*).
* **Mover Tarefas:** Fluxo rápido de transição entre colunas através de um único clique.
* **Editar Tarefas:** Atualização completa das informações dos cartões de tarefa.
* **Excluir Tarefas:** Remoção segura de registros com confirmação de segurança (UX).
* **Priorização:** Classificação de criticidade com codificação por cores e ordenação dinâmica de importância.

---

## 🔄 Metodologia Ágil Utilizada (Kanban)

A ferramenta adota o modelo **Kanban** como metodologia ágil visual. O Kanban baseia-se em princípios de:
* **Visualização do Fluxo de Trabalho:** Onde cada coluna representa um estágio da tarefa.
* **Foco no Progresso:** Permitindo que os desenvolvedores vejam gargalos rapidamente (ex: excesso de tarefas na coluna *Em Andamento*).
* **Simplicidade de Transição:** As tarefas podem ser promovidas ou rebaixadas de status à medida que o trabalho avança, promovendo a autonomia dos membros do time.

---

## ⚡ Mudança de Escopo durante o Desenvolvimento

> [!NOTE]
> **Relatório de Engenharia de Software - Alteração de Requisitos:**
> Durante as reuniões de retrospectiva de Sprint, a equipe de engenharia identificou que apenas as colunas de status não eram suficientes para priorizar as atividades mais críticas. Para otimizar o fluxo de trabalho e evitar que bugs graves ficassem parados na coluna *A Fazer*, o escopo original foi expandido para incluir o campo **Prioridade da Tarefa** ("Baixa", "Média", "Alta").
>
> **Impactos da mudança:**
> 1. **Modelagem de Dados:** Inclusão do campo `priority` na tabela SQLite.
> 2. **Interface Visual:** Criação de tags visuais coloridas nos cards (Vermelho = Alta, Amarelo = Média, Verde = Baixa).
> 3. **Lógica de Negócio (Controller):** Ordenação dinâmica no banco de dados para exibir tarefas de maior prioridade sempre no topo de cada coluna.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** [Python 3.11+](https://www.python.org/)
* **Framework Web:** [Flask 3.0+](https://flask.palletsprojects.com/)
* **Banco de Dados:** [SQLite 3](https://www.sqlite.org/) (embutido no Python)
* **Framework de Testes:** [Pytest 8.0+](https://docs.pytest.org/)
* **CI/CD:** [GitHub Actions](https://github.com/features/actions)
* **Interface (Front-end):** HTML5 Semântico, CSS3 Vanilla (com variáveis nativas e design flexbox) e JavaScript Vanilla.

---

## 📂 Estrutura do Projeto

Abaixo está a disposição estruturada dos arquivos do projeto:

```text
/ (raiz do projeto)
├── .github/
│   └── workflows/
│       └── ci.yml             # Configuração da pipeline do GitHub Actions
├── docs/
│   ├── diagramas.md           # Modelagem UML (Classes e Casos de Uso com Mermaid)
│   └── documentacao.md        # Sugestões de commits semânticos e cartões Kanban
├── src/
│   ├── __init__.py            # Inicializador e configurações do Flask App
│   ├── app.py                 # Controlador de rotas (endpoints CRUD)
│   ├── db.py                  # Gerenciador de conexão com SQLite
│   └── schema.sql             # Estrutura das tabelas SQL
├── static/
│   ├── css/
│   │   └── style.css          # Estilização completa do Kanban (Slate Modern)
│   └── js/
│       └── main.js            # JavaScript para animações e confirmações de exclusão
├── templates/
│   ├── components/
│   │   └── task_card.html     # Componente parcial reutilizável do card de tarefa
│   ├── base.html              # Layout base comum (Header/Footer/Flashes)
│   ├── index.html             # Interface do painel Kanban
│   └── tarefa.html            # Formulário de criação e edição
├── tests/
│   ├── conftest.py            # Configuração do Pytest e banco de dados em memória
│   └── test_tasks.py          # Casos de teste do CRUD e regras de negócio
├── requirements.txt           # Lista de dependências Python
└── README.md                  # Manual de documentação do sistema (Este arquivo)
```

---

## 🚀 Como Executar o Projeto Localmente

### Pré-requisitos
Ter o Python 3.10 ou superior instalado na máquina.

### Passos para Instalação e Execução

1. **Clonar ou extrair o código** no diretório desejado.
2. **Criar o ambiente virtual (Virtualenv):**
   ```bash
   python -m venv venv
   ```
3. **Ativar o ambiente virtual:**
   * **Windows (PowerShell):**
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   * **Linux / macOS:**
     ```bash
     source venv/bin/activate
     ```
4. **Instalar as dependências:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Inicializar o Banco de Dados SQLite:**
   Este comando criará o arquivo do banco de dados SQLite e aplicará o script de schema:
   ```bash
   flask --app src init-db
   ```
6. **Iniciar o Servidor de Desenvolvimento:**
   ```bash
   flask --app src run --debug
   ```
7. **Acessar a Aplicação:**
   Abra o seu navegador e acesse: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 🧪 Como Executar os Testes Automatizados

Os testes cobrem a criação de tarefas, edições de dados, remoções e as restrições de validação de títulos nulos.

Para executar a suíte de testes com relatórios detalhados na linha de comando, certifique-se de que o ambiente virtual está ativo e execute:
```bash
pytest -v
```

---

## ⚙️ Integração Contínua (GitHub Actions)

O projeto possui um fluxo de CI (Continuous Integration) configurado. Toda vez que um desenvolvedor realiza um `git push` ou abre um `Pull Request` direcionado à branch `main` ou `master`, o GitHub Actions executa automaticamente o workflow definido em `.github/workflows/ci.yml`:

1. **Inicializa uma máquina virtual Linux** (Ubuntu-latest).
2. **Configura o ambiente Python 3.11**.
3. **Instala as dependências** descritas no `requirements.txt`.
4. **Executa a suite de testes** com o `pytest`.

Isso garante que novas atualizações não quebrem as regras de negócio existentes (Regressão de Software).
