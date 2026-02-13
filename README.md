# Essentials

A simple Python module that implements some (maybe) useful features.  
It was originally made for my own use, but I figured someone might find it helpful.
This is still very early in development.

## Usage

For it to work properly, `essentials.py` must be in the same directory as the script you intend to use it in.
After you have moved `essentials.py` to your script's directory, import it by appending `import essentials` to the beginning of the script.

If you find that one of the commands does not work for you, check the documentation to see if you are using it correctly.
**If any bugs occur, feel free to report them in the Issues tab.**

### 1. `title`
`essentials.title("Title")`

**Description:**  
- Changes the window title.

### 2. `clear`
`essentials.clear()`

**Description:**  
- Clears the console window.
- As of 0.0.5, no longer uses shell=True for POSIX systems.

### 3. `version`
`essentials.version()`

**Description:**  
- Displays the version of `essentials` being run.

### 4. `beep`
`essentials.beep(800, 500)`

**Description:**
- Universal beep command.
- Parameters can be changed, 800 is frequency in Hz, and 500 is duration of the beep in milliseconds. You can also run it without specifying parameters, 800, 500 is default.
- Detects the operating system, then plays the variant suitable for the operating system.
- Keep in mind, if it is being ran on a Unix-like or Unix-based system, the parameters will not change anything, they are only intended for Windows.
- It might not work for all terminals on POSIX systems (using ASCII bell character)

### 5. `cprint`
`essentials.cprint("Text", essentials.Color.COLORNAME)`

**Description:**
- Allows colorful text in the terminal using ANSI escape sequences.
- Allows colorful backgrounds for text.
- May not always work correctly on Windows 8.1 and older.
- Works on POSIX systems.
- Works correctly on Windows 10 and newer.
- It is important you use cprint like such: `essentials.cprint("Text", essentials.Color.RED)`, otherwise you will encounter an error.
- Text and background colours can be combined: `essentials.cprint("Text", essentials.Color.BRIGHT_WHITE + essentials.Color.BLACK_BG)`

**Supported text colours:**
- RED
- GREEN
- YELLOW
- BLUE
- MAGENTA
- CYAN
- WHITE
- BRIGHT_RED
- BRIGHT_GREEN
- BRIGHT_YELLOW
- BRIGHT_BLUE
- BRIGHT_MAGENTA
- BRIGHT_CYAN
- BRIGHT_WHITE

**Supported background colours:**
- BLACK_BG
- RED_BG
- GREEN_BG
- YELLOW_BG
- BLUE_BG
- MAGENTA_BG
- CYAN_BG
- WHITE_BG
- BRIGHT_BLACK_BG
- BRIGHT_RED_BG
- BRIGHT_GREEN_BG
- BRIGHT_YELLOW_BG
- BRIGHT_BLUE_BG
- BRIGHT_MAGENTA_BG
- BRIGHT_CYAN_BG
- BRIGHT_WHITE_BG

### 6. `sysinfo`
`essentials.sysinfo()`

**Description:**
- Shows system info.
- `processor` parameter may sometimes be blank for POSIX systems, will be fixed in 0.0.5.1

Special thanks to Lyra for some suggestions regarding this README
