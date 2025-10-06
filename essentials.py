"""
Essentials by corrupted-application
Version 0.0.3.1
"""

import subprocess
import os
import winsound

def clear():
 if os.name == "posix":
  subprocess.run("clear", shell=True)
 elif os.name == "nt":
  subprocess.run("cls", shell=True)
 else:
  print("[essentials]: Something went wrong during clear command execution")

def title(title_name):
 if os.name == "posix":
   print(f"\033]0;{title_name}\007", end="")
 elif os.name == "nt":
   os.system(f'title {title_name}')
 else:
    print("[essentials]: Something went wrong during title command execution, or your operating system does not support title changes")

def version():
    print("[essentials]: Essentials 0.0.3.1")

def beep(frequency=800, duration=500):
 if os.name == "nt":
     beep_nt(frequency, duration)
 elif os.name == "posix":
     beep_pos() # calls to beep_posix, still works only if terminal supports bell
 else:
     print("[essentials]: Something went wrong during beep command execution, or your operating system does not support beep command execution.")

def beep_nt(frequency=800, duration=500):
 if os.name == "nt":
    winsound.Beep(frequency, duration) # opted for winsound.Beep instead of powershell for better support for older windows hosts without powershell
 else:
    print("[essentials]: Something went wrong during beep_nt command execution, or you are running it on an operating system different from Windows, which beep_nt does not support.")

def beep_pos():
 if os.name == "posix":
     os.system("echo -e '\a'")  # bell, only works if terminal supports it
 else:
     print("[essentials]: Something went wrong during beep_pos command execution, or you are running it on a non-unix based operating system, which beep_pos does not support.")
