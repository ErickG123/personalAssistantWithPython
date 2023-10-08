import os
import platform
import subprocess

def open_program():
  current_os = platform.system()

  if current_os == 'Teste':
    os.startfile("C:\\Users\\erick\\AppData\\Local\\Discord\\app-1.0.9018\\Discord.exe")
  else:
    subprocess.run("C:\\Users\\erick\\AppData\\Local\\Discord\\app-1.0.9018\\Discord.exe", shell=True)

open_program()
