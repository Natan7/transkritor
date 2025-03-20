from django.shortcuts import render, redirect
from django.http import JsonResponse
import speech_recognition as sr

def index(request):
    if request.method == 'POST' and request.FILES.get('audio_file'):
        audio_file = request.FILES['audio_file']
        recognizer = sr.Recognizer()

        with sr.AudioFile(audio_file) as source:
            audio_data = recognizer.record(source)
            try:
                transcription = recognizer.recognize_google(audio_data, language='pt-BR')
                return transcribe_text(request, transcription)
            except sr.UnknownValueError:
                return JsonResponse({'error': 'Não foi possível transcrever o áudio.'})
            except sr.RequestError as e:
                return JsonResponse({'error': f'Erro na API: {e}'})
    
    return render(request, 'conversao.html')

def transcribe_text(request, text=None):
    if(text):
        return render(request, 'texto_extraido.html', {'texto_recebido': text})
    
    return index(request)