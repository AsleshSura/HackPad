# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
PINS = [board.D3, board.D2, board.D1]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
Sign = KC.MACROS("Warm regards,\nAslesh Sura")

Close_Tab = KC.MACROS(Press(KC.LCTL), Tap(KC.W), Release(KC.LCTL))

Reopen_Closed_Tab = KC.MACROS(Press(KC.LCTL, KC.LSHIFT), Tap(KC.T), Release(KC.LCTL, KC.LSHIFT))

# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [Sign, Close_Tab, Reopen_Closed_Tab]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()