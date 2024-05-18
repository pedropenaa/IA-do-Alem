from transcricao_audio import AudioTranscriptor
from analise_sentimento import SentimentoAnalyzer
import os 
import numpy as np




# Dados de exemplo: sentimentos positivos e negativos
textos = [
    "Eu amo programar!",
    "Isso é incrível!",
    "Adorei esse filme.",
    "Estou muito feliz com meu novo trabalho.",
    "Eu odeio isso.",
    "Que horror!",
    "Não gostei desse produto.",
    "Estou muito chateado com o serviço." ]

# 1 para sentimentos positivos e 0 para sentimentos negativos
labels = np.array([1, 1, 1, 1, 0, 0, 0, 0])




caminho_audio = "CR7.mp3"  
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






# Instanciar e treinar o modelo
analyzer = SentimentoAnalyzer()
analyzer.train(textos, labels)


# Aqui damos o predict do sentimento do texto
texto_sentimento = texto
print(f"Sentimento do texto: {analyzer.predict_sentiment(texto_sentimento)}")