import machine
import time 

led_pins = [16, 17, 18, 19]

leds = [machine.Pin(led_pins[0], machine.Pin.OUT), machine.Pin(led_pins[1], machine.Pin.OUT),
        machine.Pin(led_pins[2], machine.Pin.OUT), machine.Pin(led_pins[3], machine.Pin.OUT)]

#leds = [machine.Pin(pin, machine.Pin.OUT) for pin in led_pins]

delay = 0.050

animation_sequence = [0,1,2,3,2,1]

while True:
    for i in animation_sequence:
        leds[i].on()
        time.sleep(delay)
        leds[i].off()