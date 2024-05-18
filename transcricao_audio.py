import speech_recognition as sr
from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError
import os



class AudioTranscriptor:

    def __init__(self, caminho_audio):
        self.caminho_audio = caminho_audio

    def verificar_arquivo(self):
        try:
            with open(self.caminho_audio, 'rb') as file:
                pass
        except FileNotFoundError:
            return "Arquivo de áudio não encontrado."

    def carregar_audio(self):
        try:
            audio = AudioSegment.from_file(self.caminho_audio)
            audio = audio.set_channels(1)  # Converte para mono (se não for)
            audio.export("temp.wav", format="wav")
            return True
        except CouldntDecodeError:
            return "Não foi possível decodificar o arquivo de áudio. Formato não suportado ou arquivo corrompido."

    def transcrever(self):
        recognizer = sr.Recognizer()
        with sr.AudioFile("temp.wav") as source:
            try:
                audio_data = recognizer.record(source)
                texto_transcrito = recognizer.recognize_google(audio_data, language='pt-BR')
                return texto_transcrito
            except sr.UnknownValueError:
                return "Não foi possível entender o áudio."
            except sr.RequestError as e:
                return f"Não foi possível fazer a requisição ao serviço de reconhecimento de fala; {e}"
            except Exception as e:
                return f"Ocorreu um erro durante a transcrição: {e}"






if __name__ == "__main__":


    caminho_audio = "CR7.mp3"  # Substitua pelo caminho do seu arquivo de áudio
    transcriptor = AudioTranscriptor(caminho_audio)
    
    if transcriptor.verificar_arquivo():
        print(transcriptor.verificar_arquivo())
    elif transcriptor.carregar_audio() is not True:
        print(transcriptor.carregar_audio())
    else:
        texto = transcriptor.transcrever()
        if texto:
            print(f"Texto transcrito: {texto}")
            os.remove("temp.wav")  # Apaga o arquivo temporário
        else:
            print("Não foi possível transcrever o áudio.")
