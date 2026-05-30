/**
 * main.js - Comportamentos interativos do Kanban (Trabalho de Engenharia de Software)
 */

document.addEventListener('DOMContentLoaded', () => {
    console.log('KanbanFlow inicializado com sucesso.');
    
    // Fade-out automático para as flash messages após 5 segundos
    const flashes = document.querySelectorAll('.flash');
    flashes.forEach(flash => {
        setTimeout(() => {
            flash.style.transition = 'opacity 0.5s ease-out, transform 0.5s ease-out';
            flash.style.opacity = '0';
            flash.style.transform = 'translateY(-10px)';
            setTimeout(() => {
                flash.remove();
            }, 500);
        }, 5000);
    });
});

/**
 * Função de confirmação exibida antes da exclusão de uma tarefa.
 * Essencial para boas práticas de usabilidade (UX) avaliadas em Eng. de Software.
 * 
 * @param {string} title Título da tarefa a ser excluída
 * @returns {boolean} Confirmação do usuário
 */
function confirmarExclusao(title) {
    return confirm(`Tem certeza de que deseja excluir a tarefa "${title}"?\nEsta ação não poderá ser desfeita.`);
}
