import speech_recognition as sr
import sys
import os

from gtts import gTTS
from datetime import datetime
from playsound import playsound

# Create the assistant's "voice"
def make_audio(audio, message):
  tts = gTTS(message, lang='pt-br')

  audios_director = os.path.join(os.getcwd() + '.\\audios')
  audio_path = os.path.join(audios_director, audio)

  relative_audio_path = os.path.relpath(audio_path, os.getcwd())

  tts.save(audio_path)
  playsound(relative_audio_path)
  os.remove(audio_path)

# Check audio input
def check_audio():
  recognizer = sr.Recognizer()

  while True:
    with sr.Microphone() as source:
      print("Fale algo (ou pressione Ctrl+C para sair):")
      try:
        audio = recognizer.listen(source)
        message = recognizer.recognize_google(audio, language="pt-BR").lower()
        print("Você disse: " + message)
        execute_command(message)
        break
      except KeyboardInterrupt:
        print("Encerrando o reconhecimento de fala.")
      except sr.WaitTimeoutError:
        print("Nenhum áudio detectado. Por favor, fale novamente.")
      except sr.UnknownValueError:
        print("Não foi possível entender o áudio")
      except sr.RequestError as e:
        print("Erro na requisição ao serviço de reconhecimento de fala; {0}".format(e))

# Execute commands according to input
def execute_command(message):
  # Close personal assistent (Hikari)
  if 'fechar hikari' in message:
    sys.exit()

  # Get current hour
  elif 'hikari' in message and 'horas' in message:
    hour = datetime.now().strftime('%H:%M')
    make_audio('hour.mp3', f'Agora são {hour}')

# Main function
def main():
  make_audio('hello.mp3', 'Olá sou a Hikari, sua assistente virtual! Como posso ajudar?')
  
  while True:
    check_audio()

main()
