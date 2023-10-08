# pip install SpeechRecognition
# pip install pyaudio
import speech_recognition as sr

# Crie um objeto Recognizer
recognizer = sr.Recognizer()

with sr.Microphone() as source:
  print("Fale algo (ou pressione Ctrl+C para sair):")
  try:
    audio = recognizer.listen(source, timeout=5)  # Espera até 5 segundos de áudio
    text = recognizer.recognize_google(audio, language="pt-BR")  # Define o idioma como português brasileiro
    print("Você disse: " + text)
  except KeyboardInterrupt:
    print("Encerrando o reconhecimento de fala.")
  except sr.WaitTimeoutError:
    print("Nenhum áudio detectado. Por favor, fale novamente.")
  except sr.UnknownValueError:
    print("Não foi possível entender o áudio")
  except sr.RequestError as e:
    print("Erro na requisição ao serviço de reconhecimento de fala; {0}".format(e))
