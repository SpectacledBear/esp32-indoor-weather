import board
import digitalio
from adafruit_debouncer import Debouncer

# Buttons
pin_a = digitalio.DigitalInOut(board.D15)
pin_a.direction = digitalio.Direction.INPUT
pin_a.pull = digitalio.Pull.UP

# pin_b = digitalio.DigitalInOut(board.D32)
# pin_b.direction = digitalio.Direction.INPUT
# pin_b.pull = digitalio.Pull.UP

# pin_c = digitalio.DigitalInOut(board.D14)
# pin_c.direction = digitalio.Direction.INPUT
# pin_c.pull = digitalio.Pull.UP

button_a = Debouncer(pin_a)  # 15
# button_b = Debouncer(pin_b) #32
# button_c = Debouncer(pin_c) #14


class Buttons:
    def __init__(self):
        self.button_a_state = True  # Default to unpressed

    def button_a_pressed(self):
        button_a_current_state = button_a.value

        if button_a_current_state != self.button_a_state:
            self.button_a_state = button_a_current_state

            if button_a_current_state == False:
                print("Button A pressed!")
                return True
            else:
                return False

    def update(self):
        button_a.update()
