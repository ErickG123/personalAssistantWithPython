import os
import platform

def open_program():
  current_os = platform.system()

  if current_os == 'Teste':
    os.startfile("C:\\Users\\erick\\AppData\\Local\\Discord\\app-1.0.9018\\Discord.exe")
  else:
    os.system("C:\\Users\\erick\\AppData\\Local\\Discord\\app-1.0.9018\\Discord.exe")

open_program()
