-- Drop tables if they exist to start fresh
DROP TABLE IF EXISTS tasks;

-- Table structure for tasks (Kanban)
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    status TEXT NOT NULL DEFAULT 'Pendente', -- Pendente, Em Andamento, Concluído
    priority TEXT NOT NULL DEFAULT 'Média',  -- Baixa, Média, Alta
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
