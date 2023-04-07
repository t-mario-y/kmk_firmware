from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType

print("Starting 11111 keyboard.")

keyboard = KMKKeyboard()

layers_ext = Layers()
split = Split(
    split_type=SplitType.UART, split_flip=True, data_pin=keyboard.data_pin, use_pio=True
)
keyboard.modules = [layers_ext, split]

LOWER = KC.MO(1)
RAISE = KC.MO(2)
# fmt: off
keyboard.keymap = [
    [
        KC.Q,    KC.W,    KC.E,    KC.R,
        KC.A,    LOWER,   RAISE,   KC.F,
    ],
    [
        KC.N1,   KC.N2,   KC.N3,   KC.N4,
        KC.N5,   LOWER,   RAISE,   KC.N6,
    ],
    [
        KC.LEFT, KC.UP,   KC.DOWN, KC.RIGHT,
        KC.LANG1,LOWER,   RAISE,   KC.LANG2,
    ]
]

# fmt: on
if __name__ == '__main__':
    keyboard.go()
