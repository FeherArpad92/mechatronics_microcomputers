import machine
import time

led_pin = [16,17,18,19]

increment_button_pin = 10
reset_button_pin = 11

leds = [machine.Pin(pin, machine.Pin.OUT) for pin in led_pin]

increment_button = machine.Pin(increment_button_pin, machine.Pin.IN, machine.Pin.PULL_DOWN)
reset_button = machine.Pin(reset_button_pin, machine.Pin.IN, machine.Pin.PULL_DOWN)


counter = 0

def display_binary(number):
    for i in range(4):
        if((number >> i) & 1):
            leds[i].on()
        else:
            leds[i].off()

while True:
    if increment_button.value() == 1:
        counter = counter +1
    display_binary(counter)
    time.sleep(0.1)