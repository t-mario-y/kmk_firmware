import board
import digitalio
import storage

reset_pin = digitalio.DigitalInOut(board.GP28)
reset_pin.pull = digitalio.Pull.UP
if reset_pin.value:
    storage.disable_usb_drive()
