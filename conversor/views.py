from django.shortcuts import render, redirect
from django.http import JsonResponse
import speech_recognition as sr

import os
import whisper
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

def index(request):
    if request.method == 'POST' and request.FILES.get('audio_file'):
        audio_file = request.FILES['audio_file']

        # Salvar o arquivo de áudio no disco temporariamente
        temp_audio_path = f"temp_{audio_file.name}"
        with open(temp_audio_path, 'wb') as temp_audio:
            for chunk in audio_file.chunks():
                temp_audio.write(chunk)

        try:
            # Carregar o modelo Whisper (pode usar 'base', 'small', 'medium', etc., dependendo do recurso disponível)
            model = whisper.load_model("tiny")

            # Realizar a transcrição
            result = model.transcribe(temp_audio_path, language='pt')
            transcription = result['text']

            # Remover o arquivo temporário após a transcrição
            os.remove(temp_audio_path)

            # Retornar a transcrição na resposta
            return transcribe_text(request, transcription)
        except Exception as e:
            # Em caso de erro, retornar como JSON
            return JsonResponse({'error': f'Erro ao transcrever o áudio: {str(e)}'})

    # Renderizar o template para upload do arquivo de áudio
    return render(request, 'conversao.html')

def transcribe_text(request, text=None):
    if(text):
        return render(request, 'texto_extraido.html', {'texto_recebido': text})
    
    return index(request)

def custom_404_view(request, exception=None):
    return render(request, '404.html', status=404)