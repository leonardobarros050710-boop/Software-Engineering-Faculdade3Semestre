# Documentação Complementar - Engenharia de Software

Este documento contém o planejamento de entregas e gerenciamento ágil recomendados para o projeto, incluindo commits semânticos e cartões para o quadro Kanban.

---

## 1. Sugestão de 10 Commits Semânticos (Conventional Commits)

Seguir boas práticas de controle de versão é um critério de avaliação comum em Engenharia de Software. Abaixo está a sequência recomendada de 10 commits para simular o desenvolvimento evolutivo do projeto:

1. **`chore: inicializar estrutura do projeto e dependencias`**
   * Criação do `requirements.txt` e definição básica da árvore de diretórios.
2. **`feat: modelar banco de dados com schema tasks`**
   * Adiciona o arquivo `src/schema.sql` definindo a tabela e campos iniciais.
3. **`feat: implementar gerenciamento de conexao com sqlite`**
   * Adiciona o módulo `src/db.py` com o ciclo de vida da conexão do banco de dados.
4. **`feat: configurar application factory no flask`**
   * Adiciona o arquivo `src/__init__.py` para iniciar a aplicação modularmente.
5. **`feat: desenvolver rotas do controller CRUD`**
   * Implementa o arquivo `src/app.py` com rotas para criar, listar, editar e remover tarefas.
6. **`style: estilizar painel Kanban moderno com flexbox`**
   * Criação do `static/css/style.css` com foco na divisão em 3 colunas e responsividade.
7. **`feat: adicionar funcionalidade de prioridade das tarefas`**
   * *Mudança de Escopo:* Atualização do banco de dados, formulários e estilo visual para suportar prioridades (Alta, Média, Baixa).
8. **`test: implementar testes automatizados com pytest`**
   * Adiciona a pasta `tests/` com testes unitários e fixtures para testar todo o CRUD.
9. **`ci: configurar workflow de teste automatico no github actions`**
   * Adiciona o arquivo `.github/workflows/ci.yml` para rodar o Pytest a cada push.
10. **`docs: redigir README.md completo e modelagem UML`**
    * Adiciona os manuais de execução, diagramas e encerra a entrega acadêmica.

---

## 2. Sugestão de Cards para o Kanban da Equipe

Para simular o acompanhamento das tarefas usando a metodologia ágil Kanban, sugere-se a divisão dos seguintes cartões (cards) em seu quadro de planejamento (ex: Trello, Jira ou GitHub Projects):

### Card 01: Setup do Ambiente
* **Título:** Configurar Ambiente de Desenvolvimento e Dependências
* **Descrição:** Criar repositório git, definir estrutura de diretórios `/src`, `/templates` e `/tests`, e configurar arquivo `requirements.txt` com as dependências do Flask e Pytest.
* **Critério de Aceitação:** Aplicação executando um "Hello World" básico.

### Card 02: Modelagem e Conectividade do Banco
* **Título:** Criar Tabela de Tarefas no SQLite e Script de Inicialização
* **Descrição:** Desenvolver o script `schema.sql` e encapsular as conexões em `db.py` usando `g` do Flask. Adicionar comando `flask init-db` na CLI.
* **Critério de Aceitação:** Rodar o comando CLI e ver o arquivo de banco gerado no diretório da instância.

### Card 03: Controlador do CRUD (Back-end)
* **Título:** Desenvolver Endpoints para Gestão de Tarefas
* **Descrição:** Criar rotas para listar tarefas divididas por status, criar tarefas através de formulário, atualizar tarefas e excluir registros por ID.
* **Critério de Aceitação:** Endpoints respondendo a requisições HTTP e manipulando registros no SQLite.

### Card 04: Interface de Colunas (Front-end)
* **Título:** Interface Visual do Quadro Kanban e Formulários
* **Descrição:** Construir layouts em HTML semântico com estilo moderno. Separar visualmente as tarefas em colunas: "A Fazer", "Em Andamento" e "Concluído".
* **Critério de Aceitação:** Layout responsivo, com cards exibindo as prioridades e botões rápidos para mover o status das tarefas.

### Card 05: Testes Unitários de Negócio
* **Título:** Implementar Testes de Validação e CRUD
* **Descrição:** Criar testes automatizados com Pytest utilizando banco em memória para testar: criação de tarefas, edições, deleções e validações de campo obrigatório.
* **Critério de Aceitação:** Cobertura dos fluxos principais com 100% de sucesso na execução do comando `pytest`.

### Card 06: Integração Contínua (CI)
* **Título:** Automatizar Pipeline de Testes com GitHub Actions
* **Descrição:** Configurar arquivo de workflow do GitHub Actions `.github/workflows/ci.yml` para rodar os testes unitários a cada Pull Request enviado à branch principal.
* **Critério de Aceitação:** Pipeline com status verde (sucesso) nas execuções de teste do GitHub.
