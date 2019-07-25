import board

from kmk.keyboard_config import KeyboardConfig as _KeyboardConfig
from kmk.matrix import DiodeOrientation


class KeyboardConfig(_KeyboardConfig):
    col_pins = (board.A2, board.A3, board.A4, board.A5, board.SCK, board.MOSI)
    row_pins = (board.D13, board.D11, board.D10, board.D9)
    diode_orientation = DiodeOrientation.COLUMNS

    split_type = 'UART'
    split_flip = True
    split_offsets = [6, 6, 6, 6, 6]
    uart_pin = board.SCL
    extra_data_pin = board.SDA
    rgb_pixel_pin = board.TX
    # led_pin = board.D7
