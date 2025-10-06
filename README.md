# Essentials

A simple Python module that implements some (maybe) useful features.  
It was originally made for my own use, but I figured someone might find it helpful.
This is still very early in development.

## Usage

For it to work properly, `essentials.py` must be in the same directory as the script you intend to use it in.
After you have moved `essentials.py` to your script's directory, import it by writing `import essentials` at the beginning of the script.
If you find that one of the commands does not work for you, check the documentation to see if you are using it correctly. If any bugs occur,
feel free to report them in the Issues tab.

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
- Displays the version of `essentials` being ran.

### 4. `beep_nt`
essentials.beep_nt(800, 500)

**Description:**
- Variant of the `beep` command for Windows.
- Plays a beep using Powershell.
- The first parameter (800) is frequency in Hz, while the second parameter (500) is duration in milliseconds.

### 5. `beep_pos`
essentials.beep_pos()

**Description:**
- Variant of the `beep` command for both Unix-based and Unix-like operating systems (POSIX).
- Plays a beep using the ASCII bell character. It plays a beep when triggered, but it might not work for all terminals (not all terminals support the bell character.)
- The frequency and duration cannot be changed.
