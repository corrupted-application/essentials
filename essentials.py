"""
Essentials by corrupted-application
Version 0.0.5
"""

import subprocess
import warnings
import os
import time
import platform
if os.name == 'nt':
  import winsound # fix for POSIX systems, would result in hang due to winsound being loaded, which is not meant to be used on POSIX systems

ver = "0.0.5"

def clear():
 if os.name == "posix":
  subprocess.run("clear")
 elif os.name == "nt":
  subprocess.run("cls", shell=True)
 else:
     warnings.warn("Something went wrong during clear command execution,"
                   "or your operating system does not support clear command execution. (essentials.clear)",
                   RuntimeWarning, stacklevel=2)

def title(title_name):
 if os.name == "posix":
  print(f"\033]0;{title_name}\007", end="") # ansi escape sequence to change title on posix systems
 elif os.name == "nt":
  os.system(f'title {title_name}')
 else:
     warnings.warn("Something went wrong during title command execution,"
                   "or your operating system does not support title command execution. (essentials.title)",
                   RuntimeWarning, stacklevel=2)

def version():
  print(f"[essentials]: Essentials {ver}")

def beep(frequency=800, duration=500):
 if os.name == "nt":
    winsound.Beep(frequency, duration)
 elif os.name == "posix":
    print("\a", end="", flush=True) # works only if terminal supports bell (ascii bell character)
 else:
    warnings.warn("Something went wrong during beep command execution,"
                  "or your operating system does not support beep command execution. (essentials.beep)",
                  RuntimeWarning, stacklevel=2)

class Color:
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
    BLACK_BG = '\033[40m'
    RED_BG = '\033[41m'
    GREEN_BG = '\033[42m'
    YELLOW_BG = '\033[43m'
    BLUE_BG = '\033[44m'
    MAGENTA_BG = '\033[45m'
    CYAN_BG = '\033[46m'
    WHITE_BG = '\033[47m'
    BRIGHT_BLACK_BG = '\033[100m' # gray
    BRIGHT_RED_BG = '\033[101m'
    BRIGHT_GREEN_BG = '\033[102m'
    BRIGHT_YELLOW_BG = '\033[103m'
    BRIGHT_BLUE_BG = '\033[104m'
    BRIGHT_MAGENTA_BG = '\033[105m'
    BRIGHT_CYAN_BG = '\033[106m'
    BRIGHT_WHITE_BG = '\033[107m'

def cprint(text, color=Color.RESET):
    print(f"{color}{text}{Color.RESET}")

def sysinfo():
    cprint("[essentials]: System Information\n", Color.YELLOW)

    cprint(f"[Operating System]: {platform.system()} {platform.release()} {platform.version()}", Color.YELLOW)
    cprint(f"[Platform]: {platform.platform()}", Color.YELLOW)
    cprint(f"[Hostname]: {platform.node()}", Color.YELLOW)
    cprint(f"[Machine Type]: {platform.machine()}", Color.YELLOW)
    cprint(f"[Processor]: {platform.processor()}\n", Color.YELLOW)

    cprint("[essentials]: Python Details\n", Color.YELLOW)
    cprint(f"[Python Version]: {platform.python_version()}", Color.YELLOW)
    cprint(f"[Python Implementation]: {platform.python_implementation()}", Color.YELLOW)
    cprint(f"[Python Compiler]: {platform.python_compiler()}", Color.YELLOW)

if __name__ == '__main__':
    cprint("[essentials]: You have ran essentials as a script. This is very likely a mistake, as essentials is a module.", Color.YELLOW)
    time.sleep(2)
    for quitting in range(3, 0, -1): # reverse range
     clear()
     print(f"Quitting in {quitting} seconds...")
     time.sleep(1)
     if quitting == 0:
         clear()
         exit()
