// Script para manipulação de exibição
function updateFileName() {
    const fileInput = document.getElementById('audio_file');
    const fileNameSpan = document.getElementById('fileName');
    const transcribeButton = document.getElementById('transcribeButton');
    const uploadLabel = document.getElementById('uploadLabel');

    if (fileInput.files.length > 0) {
        // Exibe o nome do arquivo
        const fileName = fileInput.files[0].name;
        fileNameSpan.textContent = `${fileName}`;
        uploadLabel.style.display = 'none'; // Esconde o texto "Clique aqui ou arraste o arquivo"
        transcribeButton.style.display = 'inline-block'; // Mostra o botão Transcrever
    } else {
        fileNameSpan.textContent = ''; // Reseta o nome do arquivo
        uploadLabel.style.display = 'block'; // Mostra novamente o texto padrão
        transcribeButton.style.display = 'none'; // Oculta o botão novamente
    }
}

function showSpinner() {
    const spinner = document.getElementById('spinner');
    const transcribeButton = document.getElementById('transcribeButton');

    // Exibir o spinner e desabilitar o botão enquanto a submissão ocorre
    spinner.style.display = 'block';
    transcribeButton.disabled = true;
}