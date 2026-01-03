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
essentials.title("Title")

**Description:**  
- Changes the window title.

### 2. `clear`
essentials.clear()

**Description:**  
- Clears the console window.

### 3. `version`
essentials.version()

**Description:**  
- Displays the version of `essentials` being run.

### 4. `beep`
essentials.beep(800, 500)

**Description:**
- Universal beep command.
- Parameters can be changed, 800 is frequency in Hz, and 500 is duration of the beep in milliseconds. You can also run it without specifying parameters, 800, 500 is default.
- Detects the operating system, then plays the variant suitable for the operating system.
- Keep in mind, if it is being ran on a Unix-like or Unix-based system, the parameters will not change anything, they are only intended for Windows.
- It might not work for all terminals on POSIX systems (using ASCII bell character)

### 5. `beep_nt`
essentials.beep_nt(800, 500)

**Description:**
- Variant of the `beep` command for Windows.
- Plays a beep using winsound.
- The first parameter (800) is frequency in Hz, while the second parameter (500) is duration in milliseconds.
- You can also call the command without specifying parameters, it is 800, 500 by default.
- It is a deprecated command and will be removed in a future update. Use essentials.beep instead.

### 6. `beep_pos`
essentials.beep_pos()

**Description:**
- Variant of the `beep` command for both Unix-based and Unix-like operating systems (POSIX).
- Plays a beep using the ASCII bell character. It plays a beep when triggered, but it might not work for all terminals (not all terminals support the bell character.)
- The frequency and duration cannot be changed.
- It is a deprecated command and will be removed in a future update. Use essentials.beep instead.

### 7. `cprint`
essentials.cprint("Text", essentials.Color.COLORNAME)

**Description:**
- Allows colorful text in the terminal using ANSI escape sequences.
- May not always work correctly on Windows 8.1 and older.
- Works on POSIX systems.
- Works correctly on Windows 10 and newer.

**Supported colours:**
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

Special thanks to Lyra for some suggestions regarding this README
