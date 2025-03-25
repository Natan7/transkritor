import os
import assemblyai as aai
from dotenv import load_dotenv
from django.shortcuts import render
from django.http import JsonResponse

# Configuração do transkritor com sua chave de API
load_dotenv()  # Carregar variáveis de ambiente do arquivo .env
API_KEY = os.getenv("AI_KEY") # Chave de acesso gratuita
aai.settings.api_key = os.getenv("AI_KEY")
TRANSCRIBER = aai.Transcriber(config=aai.TranscriptionConfig(language_code='pt'))

def index(request):
    if request.method == 'POST' and request.FILES.get('audio_file'):
        audio_file = request.FILES['audio_file']

        # Salvar o arquivo de áudio no disco temporariamente
        temp_audio_path = f"temp_{audio_file.name}"
        with open(temp_audio_path, 'wb') as temp_audio:
            for chunk in audio_file.chunks():
                temp_audio.write(chunk)

        try:
            # Enviar o áudio para o AssemblyAI e obter a transcrição
            transcription = TRANSCRIBER.transcribe(temp_audio_path).text

            # Remover o arquivo temporário
            os.remove(temp_audio_path)

            # Retornar a transcrição na resposta
            return transcribe_text(request, transcription)
        except Exception as e:
            # Em caso de erro, retornar como JSON
            return JsonResponse({'error': f'Erro ao transcrever o áudio: {str(e)}'})

    # Renderizar o template para upload do arquivo de áudio
    return render(request, 'index.html')

def transcribe_text(request, text=None):
    if(text):
        return render(request, 'transcribed_text.html', {'texto_recebido': text})
    
    return index(request)

def custom_404_view(request, exception=None):
    return render(request, '404.html', status=404)