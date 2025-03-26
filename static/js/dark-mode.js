// Função para alternar modo escuro
function toggleDarkMode() {
    const body = document.body;
    const toggleButton = document.getElementById('darkModeToggle');

    // Alterna a classe do modo escuro
    body.classList.toggle('dark-mode');

    // Alterna o ícone do botão com base no estado
    if (body.classList.contains('dark-mode')) {
        toggleButton.innerHTML = '☀'; // Ícone de sol para modo claro
        toggleButton.title = 'Modo Claro';
    } else {
        toggleButton.innerHTML = '🌙'; // Ícone de lua para modo escuro
        toggleButton.title = 'Modo Escuro';
    }
}
