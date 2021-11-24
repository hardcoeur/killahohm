#killaohm - Raspberry Pi PICO
import board
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.matrix import DiodeOrientation
from kmk.hid import HIDModes

killaohm = KMKKeyboard()

killaohm.col_pins = (board.GP3, board.GP4, board.GP5, board.GP1, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12)
killaohm.row_pins = (board.GP18, board.GP19, board.GP20, board.GP21)

killaohm.diode_orientation = DiodeOrientation.COLUMNS

killaohm.debug_enabled = True

killaohm.keymap = [
        [
            KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P, KC.LBRC,
            KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT,
            KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMMA, KC.DOT, KC.MINUS, KC.RSHIFT,
            KC.LCTRL,  KC.LGUI, KC.LALT, KC.LALT, KC.BSPC, KC.TAB, KC.SPACE, KC.RALT, KC.RALT, KC.RGUI, KC.ENTER,
        ],

]
if __name__ == '__main__':
        killaohm.go(hid_type=HIDModes.USB) # LETS GO!
