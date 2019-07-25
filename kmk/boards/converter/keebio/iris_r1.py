import board

from kmk.keyboard_config import KeyboardConfig as _KeyboardConfig
from kmk.matrix import DiodeOrientation


class KeyboardConfig(_KeyboardConfig):
    col_pins = (board.A2, board.A3, board.A4, board.A5, board.SCK, board.MOSI)
    row_pins = (board.D11, board.D10, board.D9, board.D7, board.D13)
    diode_orientation = DiodeOrientation.COLUMNS
    rgb_pixel_pin = board.TX
    uart_pin = board.SCL
    split_type = 'UART'
    split_flip = True
    split_offsets = [6, 6, 6, 6, 6]
