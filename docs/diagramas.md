# Diagramas do Projeto - Engenharia de Software

Este documento contém a modelagem visual do sistema utilizando diagramas UML expressos em formato Mermaid.

---

## 1. Diagrama de Casos de Uso

O diagrama de casos de uso ilustra as interações entre o ator principal (Membro da Equipe) e as funcionalidades expostas pelo sistema de gerenciamento Kanban.

```mermaid
graph TD
    %% Atores
    User["👤 Membro da Equipe (Usuário)"]
    
    %% Casos de Uso
    UC1((Visualizar Quadro Kanban))
    UC2((Criar Nova Tarefa))
    UC3((Editar Detalhes da Tarefa))
    UC4((Mover Card de Status))
    UC5((Excluir Tarefa))
    UC6((Definir Prioridade da Tarefa))
    
    %% Relacionamentos de Uso
    User --> UC1
    User --> UC2
    User --> UC3
    User --> UC4
    User --> UC5
    
    %% Includes e Extends
    UC2 -.->|include| UC6
    UC3 -.->|include| UC6
    
    %% Estilização
    style User fill:#6366f1,stroke:#4f46e5,stroke-width:2px,color:#fff
    style UC1 fill:#1f2937,stroke:#374151,stroke-width:2px,color:#fff
    style UC2 fill:#1f2937,stroke:#374151,stroke-width:2px,color:#fff
    style UC3 fill:#1f2937,stroke:#374151,stroke-width:2px,color:#fff
    style UC4 fill:#1f2937,stroke:#374151,stroke-width:2px,color:#fff
    style UC5 fill:#1f2937,stroke:#374151,stroke-width:2px,color:#fff
    style UC6 fill:#111827,stroke:#4b5563,stroke-width:1px,color:#9ca3af,stroke-dasharray: 5 5
```

---

## 2. Diagrama de Classes

O diagrama de classes detalha a arquitetura lógica do sistema. Ele mostra a separação de responsabilidades entre a fábrica de aplicação (`create_app`), a conexão com o banco SQLite (`db.py`), as rotas controladoras (`app.py`), e a estrutura lógica do dado (`Task`).

```mermaid
classDiagram
    class FlaskApp {
        <<Factory>>
        +create_app(test_config: dict) Flask
    }

    class DatabaseManager {
        +get_db() Connection
        +close_db(e: Exception)
        +init_db()
        +init_app(app: Flask)
    }

    class TaskRoutes {
        +index() HTML
        +nova() HTML/Redirect
        +editar(id: int) HTML/Redirect
        +deletar(id: int) Redirect
        +mover(id: int) Redirect
    }

    class Task {
        +id: int
        +title: str
        +description: str
        +status: str
        +priority: str
        +created_at: datetime
    }

    %% Relacionamentos
    FlaskApp --> DatabaseManager : "inicializa e configura"
    FlaskApp --> TaskRoutes : "registra rotas (Blueprint)"
    TaskRoutes ..> DatabaseManager : "solicita conexão g.db"
    TaskRoutes ..> Task : "gerencia CRUD e exibe"
    DatabaseManager ..> Task : "persiste registros na tabela tasks"
```
