import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    # fmt: off
    row_pins = (board.GP14, board.GP13, board.GP12, board.GP11, board.GP10)
    col_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP7, board.GP8, board.GP9)
    # fmt: on
    data_pin = board.GP15
    diode_orientation = DiodeOrientation.COL2ROW
    # fmt: off
    coord_mapping = [
     0,  1,  2,  3,  4,  5,  6,  35, 36, 37, 38, 39, 40, 41,
     7,  8,  9, 10, 11, 12, 13,  42, 43, 44, 45, 46, 47, 48,
    14, 15, 16, 17, 18, 19, 20,  49, 50, 51, 52, 53, 54, 55,
    21, 22, 23, 24, 25, 26, 27,  56, 57, 58, 59, 60, 61, 62,
                31, 32, 33, 34,  63, 64, 65, 66
    ]
    # fmt: on
