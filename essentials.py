"""
Essentials by corrupted-application
Version 0.0.4
"""

import subprocess
import warnings
import os
if os.name == 'nt':
  import winsound # fix for POSIX systems, would result in hang due to winsound being loaded, which is not meant to be used on POSIX systems

def clear():
 if os.name == "posix":
  subprocess.run("clear", shell=True)
 elif os.name == "nt":
  subprocess.run("cls", shell=True)
 else:
     warnings.warn("Something went wrong during clear command execution,"
                   "or your operating system does not support clear command execution. (essentials.clear)",
                   RuntimeWarning, stacklevel=2)

def title(title_name):
 if os.name == "posix":
  print(f"\033]0;{title_name}\007", end="")
 elif os.name == "nt":
  os.system(f'title {title_name}')
 else:
     warnings.warn("Something went wrong during title command execution,"
                   "or your operating system does not support title command execution. (essentials.title)",
                   RuntimeWarning, stacklevel=2)

def version():
  print("[essentials]: Essentials 0.0.4")

def beep(frequency=800, duration=500):
 if os.name == "nt":
    winsound.Beep(frequency, duration)
 elif os.name == "posix":
    os.system("echo -e '\a'") # works only if terminal supports bell
 else:
    warnings.warn("Something went wrong during beep command execution,"
                  "or your operating system does not support beep command execution. (essentials.beep)",
                  RuntimeWarning, stacklevel=2)

def beep_pos():
    warnings.warn(
                  "Your code is using a deprecated command (essentials.beep.pos())."
                  "Please switch to the essentials.beep command. This command will be removed in a future release.",
                  DeprecationWarning, stacklevel=2)
    os.system("echo -e '\a'")

def beep_nt(frequency=800, duration=500):
    warnings.warn(
                "Your code is using a deprecated command (essentials.beep.nt())."
                "Please switch to the essentials.beep command. This command will be removed in a future release.",
                DeprecationWarning, stacklevel=2)
    winsound.Beep(frequency, duration)

class Color: # ansi escape sequences
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'

def cprint(text, color=Color.RESET):
    print(f"{color}{text}{Color.RESET}")

