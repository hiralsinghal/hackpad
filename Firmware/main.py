import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Macros, Press, Release, Tap

keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)

# 1. Define your GPIO pins (Adjust these to your specific board pins)
keyboard.col_pins = (board.GP0, board.GP1, board.GP2)
keyboard.row_pins = (board.GP3, board.GP4, board.GP5)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# 2. Define Custom Macro to Open an App
# This uses Win+R -> type 'cmd' (or any app) -> Enter
OPEN_APP = KC.MACRO(
    Press(KC.LGUI), Tap(KC.R), Release(KC.LGUI),
    "cmd", 
    Tap(KC.ENT),
)

# 3. 3x3 Keymap
# [ Row 1 ]
# [ Row 2 ]
# [ Row 3 ]
keyboard.keymap = [
    [
        KC.MPRV,    KC.MPLY,    KC.MNXT,    # Prev Track | Play/Pause | Next Track
        KC.VOLU,    KC.VOLD,    KC.MUTE,    # Vol Up     | Vol Down   | Mute
        KC.ESC,     KC.BT_TOG,  OPEN_APP    # Escape     | BT On/Off  | Open App
    ]
]

if __name__ == '__main__':
    keyboard.go()