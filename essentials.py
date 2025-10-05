"""
Essentials by corrupted-application
Version 0.0.2.4
"""

import subprocess
import os

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
    print("[essentials]: Essentials 0.0.2.4")

def beep(frequency=800, duration=500):
 if os.name == "nt":
    ps_command = f"[console]::beep({frequency}, {duration})"
    subprocess.run(["powershell", "-Command", ps_command])
 else:
    print("[essentials]: Something went wrong during beep command execution, or you are running it on an operating system different from Windows, which essentials does not currently support.")
