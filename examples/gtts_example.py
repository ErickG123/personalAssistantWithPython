# pip install gTTS
# pip install playsound

from gtts import gTTS
from playsound import playsound

def cria_audio(mensagem):
	tts = gTTS(mensagem, lang = 'pt-br')
	audio = 'hello.mp3'
	tts.save(audio)
	playsound(audio)

arquivo = open("examples/frase.txt", "r", encoding = "utf-8")
conteudo = arquivo.read()
cria_audio(conteudo)
arquivo.close()
