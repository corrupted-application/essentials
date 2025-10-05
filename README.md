# Essentials

A simple Python module that implements some (maybe) useful features.  
It was originally made for my own use, but I figured someone might find it helpful.
This is still very early in development.

## Usage

For it to work properly, `essentials.py` must be in the same directory as the script you intend to use it in.
After you have moved `essentials.py` to your script's directory, import it by writing `import essentials` at the beginning of the script.

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
- Plays a beep using Powershell (This is only available for Windows for now.)
- The first parameter (800) is frequency in Hz, while the second parameter (500) is duration in milliseconds.
