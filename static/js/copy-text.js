// Função para copiar texto
function copyText() {
    const extractedMessage = document.querySelector('.extracted-message');
    const textToCopy = extractedMessage.textContent || extractedMessage.innerText;

    // Usar a API Clipboard para copiar o texto
    navigator.clipboard.writeText(textToCopy).then(() => {
        const copyStatusElement = document.getElementById('copyStatus');
        copyStatusElement.innerHTML = '<i class="fas fa-check"></i> Copiado'; // Alterar ícone e texto para "Copiado"

        // Voltar ao estado original ("Copiar") após 3 segundos
        setTimeout(() => {
            copyStatusElement.innerHTML = '<i class="fas fa-copy"></i> Copiar';
        }, 3000);
    }).catch((err) => {
        console.error('Erro ao copiar texto:', err);
    });
}