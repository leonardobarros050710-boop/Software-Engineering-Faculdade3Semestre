# Documentação do Projeto – KanbanFlow

## 1. Introdução

O projeto **KanbanFlow** foi desenvolvido como atividade prática da disciplina de Engenharia de Software, com o objetivo de aplicar conceitos relacionados ao desenvolvimento ágil, versionamento de código, controle de qualidade e documentação de software.

O sistema consiste em uma aplicação web para gerenciamento de tarefas baseada na metodologia Kanban. A ferramenta permite criar, visualizar, editar, excluir e acompanhar tarefas através de um quadro organizado por status, auxiliando equipes no controle do fluxo de trabalho.

Além da implementação do sistema, o projeto utiliza recursos amplamente empregados no mercado de tecnologia, como GitHub, GitHub Projects, GitHub Actions, testes automatizados e documentação técnica.

---

## 2. Escopo Inicial do Projeto

O escopo inicial previa o desenvolvimento de um sistema web capaz de gerenciar tarefas por meio de operações básicas de CRUD (Create, Read, Update e Delete).

As funcionalidades planejadas inicialmente foram:

* Cadastro de tarefas;
* Visualização das tarefas cadastradas;
* Edição das informações de uma tarefa;
* Exclusão de tarefas;
* Organização das tarefas em colunas Kanban.

O objetivo era fornecer uma solução simples para acompanhamento de atividades de uma equipe de desenvolvimento.

---

## 3. Metodologia Ágil Utilizada

A metodologia escolhida para o projeto foi o **Kanban**.

O Kanban é uma abordagem ágil baseada na visualização do fluxo de trabalho por meio de quadros organizados em colunas que representam os estados das tarefas.

Para o gerenciamento do projeto foi utilizado o GitHub Projects com as colunas:

* To Do (A Fazer)
* In Progress (Em Progresso)
* Done (Concluído)

As atividades do desenvolvimento foram registradas em cards distribuídos entre essas colunas, permitindo acompanhar a evolução do projeto de forma visual e organizada.

A utilização do Kanban contribuiu para:

* Melhor organização das atividades;
* Priorização de tarefas;
* Controle do andamento do projeto;
* Facilidade na gestão de mudanças de requisitos.

---

## 4. Importância da Modelagem na Engenharia de Software

A modelagem é uma etapa fundamental da Engenharia de Software, pois permite representar visualmente a estrutura e o comportamento do sistema antes ou durante sua implementação.

A utilização de diagramas UML auxilia na comunicação entre os membros da equipe, reduz ambiguidades e facilita a compreensão da arquitetura do software.

Neste projeto foram utilizados dois diagramas UML:

* Diagrama de Casos de Uso;
* Diagrama de Classes.

Esses diagramas permitem compreender tanto as funcionalidades disponibilizadas ao usuário quanto a estrutura lógica da aplicação.

---

## 5. Diagrama de Casos de Uso

O Diagrama de Casos de Uso representa as interações entre o usuário e o sistema.

O sistema permite que o usuário execute as seguintes ações:

* Criar tarefas;
* Visualizar tarefas;
* Editar tarefas;
* Excluir tarefas;
* Alterar o status das tarefas;
* Definir prioridades para as tarefas.

O diagrama completo encontra-se no arquivo:

`docs/casos_de_uso.md`

---

## 6. Diagrama de Classes

O Diagrama de Classes apresenta a estrutura interna do sistema e os principais elementos envolvidos na implementação.

A modelagem contempla:

* Entidade Tarefa;
* Controlador responsável pelas operações do sistema;
* Componente de gerenciamento do banco de dados SQLite.

O diagrama completo encontra-se no arquivo:

`docs/diagrama_classes.md`

---

## 7. Estrutura do Projeto

O projeto foi organizado seguindo uma estrutura modular:

```text
src/
├── __init__.py
├── app.py
├── db.py
└── schema.sql

tests/
└── test_tasks.py

docs/
├── casos_de_uso.md
├── diagrama_classes.md
└── documentacao_projeto.md
```

Essa organização facilita a manutenção do código e a separação de responsabilidades.

---

## 8. Tecnologias Utilizadas

As principais tecnologias utilizadas no desenvolvimento foram:

* Python 3.11
* Flask
* SQLite
* Pytest
* GitHub
* GitHub Actions
* HTML5
* CSS3
* JavaScript

---

## 9. Considerações Finais

O desenvolvimento do KanbanFlow permitiu aplicar conceitos fundamentais da Engenharia de Software em um cenário prático.

Durante a execução do projeto foram utilizados princípios de desenvolvimento ágil, versionamento de código, testes automatizados, integração contínua e documentação técnica.

A experiência proporcionou uma visão mais próxima das práticas utilizadas por equipes profissionais de desenvolvimento de software.
