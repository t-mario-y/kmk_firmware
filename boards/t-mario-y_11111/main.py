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
        KC.ESC,   KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,    KC.MINS,  KC.EQL,   KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.GRV,
        KC.TAB,   KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,     KC.LBRC,  KC.RBRC,  KC.Y,     KC.U,     KC.I,     KC.O,     KC.P,     KC.BSPC,
        KC.LCTL,  KC.A,     KC.S,     KC.D,     KC.F,     KC.G,     KC.BSLS,  KC.SLSH,  KC.H,     KC.J,     KC.K,     KC.L,     KC.SCLN,  KC.QUOT,
        KC.LSFT,  KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,     KC.LANG2, KC.LANG1, KC.N,     KC.M,     KC.COMM,  KC.DOT,   KC.HOME,  KC.RSFT,
                                      KC.LALT,  KC.LGUI,  LOWER,    KC.SPC,   KC.ENT,   RAISE,    KC.RALT,  KC.END,
    ],
    [
        KC.ESC,   KC.F1,    KC.F2,    KC.F3,    KC.F4,    KC.F5,    KC.F11,   KC.F12,   KC.F6,    KC.F7,    KC.F8,    KC.F9,    KC.F0,    KC.GRV,
        KC.TAB,   KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,     KC.LBRC,  KC.RBRC,  KC.Y,     KC.U,     KC.I,     KC.O,     KC.P,     KC.BSPC,
        KC.LCTL,  KC.A,     KC.S,     KC.D,     KC.F,     KC.G,     KC.BSLS,  KC.SLSH,  KC.LEFT,  KC.DOWN,  KC.UP,    KC.RIGHT, KC.SCLN,  KC.QUOT,
        KC.LSFT,  KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,     KC.LANG2, KC.LANG1, KC.N,     KC.M,     KC.COMM,  KC.DOT,   KC.HOME,  KC.RSFT,
                                      KC.LALT,  KC.LGUI,  LOWER,    KC.SPC,   KC.ENT,   RAISE,    KC.RALT,  KC.END,
    ],
    [
        KC.ESC,   KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,    KC.MINS,  KC.EQL,   KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.GRV,
        KC.TAB,   KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,     KC.LBRC,  KC.RBRC,  KC.Y,     KC.U,     KC.I,     KC.O,     KC.P,     KC.DEL,
        KC.LCTL,  KC.A,     KC.S,     KC.D,     KC.F,     KC.G,     KC.BSLS,  KC.SLSH,  KC.LEFT,  KC.DOWN,  KC.UP,    KC.RIGHT, KC.SCLN,  KC.QUOT,
        KC.LSFT,  KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,     KC.LANG2, KC.LANG1, KC.N,     KC.M,     KC.COMM,  KC.DOT,   KC.HOME,  KC.RSFT,
                                      KC.LALT,  KC.LGUI,  LOWER,    KC.SPC,   KC.ENT,   RAISE,    KC.RALT,  KC.END,
    ]
]

# fmt: on
if __name__ == '__main__':
    keyboard.go()
