import time

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS as KeyboardLayout
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayout(keyboard)

mappings = {
    "WINDOWS": Keycode.WINDOWS,
    "GUI": Keycode.GUI,
    "MENU": Keycode.APPLICATION,
    "APP": Keycode.APPLICATION,
    "SHIFT": Keycode.SHIFT,
    "ALT": Keycode.ALT,
    "CONTROL": Keycode.CONTROL,
    "CTRL": Keycode.CONTROL,
    "DOWN": Keycode.DOWN_ARROW,
    "DOWNARROW": Keycode.DOWN_ARROW,
    "LEFT": Keycode.LEFT_ARROW,
    "LEFTARROW": Keycode.LEFT_ARROW,
    "RIGHT": Keycode.RIGHT_ARROW,
    "RIGHTARROW": Keycode.RIGHT_ARROW,
    "UP": Keycode.UP_ARROW,
    "UPARROW": Keycode.UP_ARROW
}

default_delay = 0


def convert_line_to_command(line):
    """Convert the plain line to a sequence of key presses."""
    
    command = []
    
    for key in filter(None, line.split(" ")):
        key = key.upper()
        keycode = mappings.get(key, None)
        
        if keycode:
            command.append(keycode)
        elif hasattr(Keycode, key):
            command.append(getattr(Keycode, key))
        else:
            print(f"Unknown key: <{key}>")
            
    return command
        
        
def execute_command(command):
    """Execute the sequence of key presses."""
    
    for key in command:
        keyboard.press(key)
    keyboard.release_all()


def write_line(string):
    """Perform a sequence of key presses to type a string."""
    
    keyboard_layout.write(string)


def parse_line(line):
    """Parse a line of the script."""
    
    if line.startswith("REM") or line.startswith("DEFAULT_DELAY") or line.startswith("DEFAULTDELAY"):
        pass
    elif line.startswith("DELAY"):
        delay = float(line.split("DELAY")[1])
        time.sleep(delay / 1000)
    elif line.startswith("STRING"):
        string = (line.split("STRING")[1]).strip()
        write_line(string)
    else:
        command = convert_line_to_command(line)
        execute_command(command)


def run_script(lines):
    """"Run the ducky script."""
    
    global default_delay
    
    for i, line in enumerate(lines):
        if line := line.strip():
            if i == 0:
                previous_line = None
                
                if line.startswith("DEFAULT_DELAY"):
                    default_delay = int(line.split("DEFAULT_DELAY")[1])
                elif line.startswith("DEFAULTDELAY"):
                    default_delay = int(line.split("DEFAULTDELAY")[1])
            else:
                previous_line = lines[i-1]
            
            if line.startswith("REPEAT"):
                parse_line(previous_line)
            else:
                parse_line(line)
            
            time.sleep(default_delay / 1000)


if __name__ == "__main__":
    time.sleep(1)
    
    with open("payload.txt", "r") as script:
        lines = script.readlines()
        run_script(lines)
