from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.split import Split, SplitType

keyboard = KMKKeyboard()

split = Split(
    split_type=SplitType.UART, split_flip=True, data_pin=keyboard.data_pin, use_pio=True
)
keyboard.modules.append(split)

# fmt: off
keyboard.keymap = [
    [
        KC.Q,  KC.W,  KC.E,  KC.R,
        KC.A,  KC.S,  KC.D,  KC.F
    ]
]

# fmt: on
if __name__ == '__main__':
    keyboard.go()
