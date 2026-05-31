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

---

## 10. Alteração de Escopo

Durante o desenvolvimento do projeto, foi identificada uma oportunidade de melhoria relacionada à organização e priorização das atividades no quadro Kanban.

Inicialmente, o sistema possuía apenas o campo de status para controlar o progresso das tarefas, permitindo que elas fossem classificadas como "A Fazer", "Em Andamento" ou "Concluído". Entretanto, após a análise do fluxo de trabalho, observou-se que tarefas de diferentes níveis de importância eram exibidas sem qualquer mecanismo de priorização.

Dessa forma, foi realizada uma alteração no escopo original do projeto, com a inclusão do atributo **Prioridade da Tarefa**. Esse novo campo passou a permitir que cada tarefa fosse classificada como:

* Baixa Prioridade;
* Média Prioridade;
* Alta Prioridade.

A alteração trouxe benefícios importantes para a utilização do sistema, pois possibilitou uma melhor organização das atividades e facilitou a identificação das tarefas mais críticas pela equipe.

### Impactos da Alteração

A inclusão do campo de prioridade exigiu modificações em diferentes partes do sistema:

#### Banco de Dados

Foi necessário adicionar um novo atributo responsável por armazenar a prioridade de cada tarefa na estrutura de dados persistida em SQLite.

#### Interface do Usuário

A interface foi adaptada para exibir visualmente o nível de prioridade de cada tarefa, permitindo que o usuário identifique rapidamente atividades mais importantes.

#### Lógica de Negócio

As regras do sistema passaram a considerar a prioridade das tarefas durante a exibição das informações, favorecendo a organização das atividades dentro do quadro Kanban.

### Justificativa da Mudança

A alteração foi motivada pela necessidade de tornar o sistema mais aderente às práticas utilizadas em ambientes reais de desenvolvimento de software.

Em equipes de desenvolvimento, nem todas as tarefas possuem a mesma importância ou urgência. A utilização de níveis de prioridade permite que a equipe concentre esforços inicialmente nas atividades mais relevantes para o projeto.

Dessa forma, a mudança de escopo agregou valor ao produto final sem comprometer os objetivos originais definidos para o projeto.

---

## 11. Testes Automatizados e Integração Contínua

A garantia da qualidade do software foi realizada por meio da utilização de testes automatizados e de um processo de Integração Contínua (Continuous Integration – CI).

Os testes automatizados foram implementados utilizando o framework **Pytest**, amplamente utilizado no ecossistema Python para validação de funcionalidades e identificação precoce de falhas.

Os casos de teste desenvolvidos têm como objetivo verificar o correto funcionamento das principais funcionalidades do sistema, incluindo operações relacionadas ao gerenciamento de tarefas, validação de dados e regras de negócio implementadas na aplicação.

A utilização de testes automatizados oferece diversos benefícios, entre eles:

* Redução da ocorrência de erros durante o desenvolvimento;
* Maior confiabilidade das funcionalidades implementadas;
* Facilidade para identificar regressões após alterações no código;
* Agilidade na validação de novas funcionalidades.

### Integração Contínua com GitHub Actions

Além dos testes automatizados, o projeto utiliza o serviço **GitHub Actions** para executar verificações automáticas sempre que alterações são enviadas ao repositório.

O workflow de Integração Contínua foi configurado para ser executado em eventos de:

* Push para as branches principais do projeto;
* Abertura de Pull Requests.

Durante a execução do workflow, são realizadas as seguintes etapas:

1. Download do código-fonte do repositório;
2. Configuração do ambiente Python;
3. Instalação das dependências do projeto;
4. Execução automática dos testes utilizando Pytest.

Esse processo garante que o código enviado ao repositório seja validado continuamente, contribuindo para a manutenção da qualidade e da estabilidade do sistema.

### Benefícios para o Projeto

A combinação entre testes automatizados e Integração Contínua aproxima o projeto das práticas adotadas em ambientes profissionais de desenvolvimento de software.

Essas ferramentas permitem identificar problemas de forma antecipada, aumentar a confiabilidade da aplicação e reduzir riscos durante a evolução do sistema.

---

## 12. Respostas às Questões Norteadoras

12.1 Quais são as principais causas de falhas em projetos ágeis e como o GitHub pode ajudar a mitigá-las?

Entre as principais causas de falhas em projetos ágeis estão a falta de organização das tarefas, comunicação ineficiente entre os membros da equipe, ausência de documentação adequada e dificuldades no controle de versões do código.

O GitHub auxilia na mitigação desses problemas por meio de funcionalidades como controle de versão com Git, gerenciamento de tarefas através de quadros Kanban, rastreamento de alterações, revisão de código e integração com ferramentas de automação.

No contexto do projeto KanbanFlow, o GitHub foi utilizado para armazenar o código-fonte, registrar a evolução do projeto por meio de commits e possibilitar a execução automática de testes utilizando GitHub Actions.

12.2 Quem são os principais beneficiados por um sistema de gerenciamento ágil e como eles utilizam as funcionalidades desenvolvidas?

Os principais beneficiados são equipes de desenvolvimento de software, gerentes de projeto, analistas de sistemas e demais profissionais envolvidos na execução e acompanhamento de atividades.

O sistema desenvolvido permite que os usuários criem tarefas, acompanhem seu progresso, alterem status, definam prioridades e visualizem o fluxo de trabalho em um quadro Kanban.

Essas funcionalidades contribuem para uma melhor organização das atividades, aumento da produtividade e maior visibilidade sobre o andamento do projeto.

12.3 Como o uso de ferramentas de controle de qualidade, como GitHub Actions, pode garantir a entrega de um software confiável?

Ferramentas de controle de qualidade automatizam processos importantes de validação do software, reduzindo a possibilidade de erros humanos.

No projeto desenvolvido, o GitHub Actions foi configurado para executar automaticamente os testes sempre que alterações são enviadas ao repositório. Dessa forma, falhas podem ser identificadas rapidamente antes que novas versões sejam incorporadas ao projeto.

Essa abordagem aumenta a confiabilidade do sistema, melhora a qualidade do código e reduz riscos de regressão durante a evolução da aplicação.

12.4 Quais são os principais desafios ao implementar mudanças em um projeto ágil e como lidar com eles?

Projetos ágeis frequentemente passam por mudanças de requisitos durante seu desenvolvimento. Entre os principais desafios estão a necessidade de adaptação da equipe, atualização da documentação, alterações na modelagem de dados e impactos sobre funcionalidades já implementadas.

No KanbanFlow, um exemplo foi a inclusão do campo de prioridade das tarefas durante o desenvolvimento. Para lidar com essa mudança, foi necessário atualizar a estrutura do banco de dados, a interface do usuário e a lógica de negócio.

A utilização de práticas ágeis permitiu incorporar essa alteração de forma controlada, sem comprometer os objetivos principais do projeto.

12.5 Como as metodologias ágeis estudadas na disciplina podem ser aplicadas diretamente neste projeto?

As metodologias ágeis podem ser aplicadas diretamente por meio da organização do trabalho em pequenas tarefas, acompanhamento contínuo do progresso e adaptação rápida às mudanças de requisitos.

O Kanban foi a principal metodologia utilizada neste projeto. As tarefas foram organizadas em etapas de desenvolvimento e acompanhadas visualmente por meio de cartões que representam atividades específicas.

Além disso, conceitos como melhoria contínua, entregas incrementais, colaboração e adaptação constante foram aplicados durante todo o desenvolvimento do sistema.

---

## 13. Conclusão

O desenvolvimento do projeto KanbanFlow permitiu a aplicação prática dos conceitos estudados na disciplina de Engenharia de Software, abrangendo desde o levantamento de requisitos até a implementação, testes e documentação do sistema.

Durante a execução do projeto foram utilizadas ferramentas e práticas amplamente empregadas no mercado de tecnologia, incluindo controle de versão com Git e GitHub, gerenciamento de tarefas baseado em Kanban, testes automatizados com Pytest e Integração Contínua utilizando GitHub Actions.

Além dos aspectos técnicos, o projeto proporcionou uma melhor compreensão sobre a importância da organização, documentação e adaptação a mudanças durante o ciclo de desenvolvimento de software.

A implementação da funcionalidade de priorização de tarefas demonstrou, na prática, como alterações de requisitos podem ser incorporadas ao projeto de forma controlada, mantendo a qualidade e a consistência da aplicação.

Como resultado, o KanbanFlow atende aos objetivos propostos pela atividade, fornecendo uma solução funcional para gerenciamento de tarefas e servindo como exemplo da aplicação integrada dos conhecimentos adquiridos ao longo da disciplina.
