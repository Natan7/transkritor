document.addEventListener('DOMContentLoaded', () => {
    const body = document.body;
    const toggleButton = document.getElementById('darkModeToggle');

    // Carregar estado do modo escuro do Local Storage
    const darkModeState = localStorage.getItem('dark-mode');
    if (darkModeState === 'enabled') {
        body.classList.add('dark-mode');
        toggleButton.innerHTML = '☀'; // Ícone de sol para modo claro
        toggleButton.title = 'Modo Claro';
    } else {
        body.classList.remove('dark-mode');
        toggleButton.innerHTML = '🌙'; // Ícone de lua para modo escuro
        toggleButton.title = 'Modo Escuro';
    }

    // Alternar o modo escuro
    toggleButton.addEventListener('click', () => {
        const isDarkMode = body.classList.contains('dark-mode');
        if (isDarkMode) {
            body.classList.remove('dark-mode');
            toggleButton.innerHTML = '🌙'; // Ícone de lua para modo escuro
            toggleButton.title = 'Modo Escuro';

            // Salvar estado no Local Storage
            localStorage.setItem('dark-mode', 'disabled');
        } else {
            body.classList.add('dark-mode');
            toggleButton.innerHTML = '☀'; // Ícone de sol para modo claro
            toggleButton.title = 'Modo Claro';

            // Salvar estado no Local Storage
            localStorage.setItem('dark-mode', 'enabled');
        }
    });
});
