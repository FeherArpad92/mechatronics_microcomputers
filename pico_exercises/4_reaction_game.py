import machine
import utime
import urandom

button_pins = [10, 11, 12, 13]
# LEDs Y0, Y1, Y2, Y3 -> on pins GP16, GP17, GP18, GP19
led_pins = [16, 17, 18, 19]

# Create a list of 'Pin' objects to control the LEDs.
# The 'for' loop iterates through the 'led_pins' list.
# Each pin is configured as an OUTPUT (OUT) because the microcontroller sends signals to the LEDs.
leds = [machine.Pin(pin, machine.Pin.OUT) for pin in led_pins]

# Create a list of 'Pin' objects to monitor the buttons.
# Each pin is configured as an INPUT (IN) because we receive signals about the button's state.
# 'PULL_DOWN' connects an internal resistor between the pin and ground (GND).
# This ensures that when the button is not pressed, the pin is clearly at a 'LOW' (0) level.
# When the button is pressed (connecting it to 3.3V), the pin will read a 'HIGH' (1) signal.
buttons = [machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_DOWN) for pin in button_pins]

target_led_index = -1
start_time = 0

def all_leds_off():
    for led in leds:
        led.off()

def success_animation():
    print("Correct!")
    for _ in range(2):
        for led in leds:
            led.on()
        utime.sleep(0.1)
        all_leds_off()
        utime.sleep(0.1)

def error_amination(wrong_led_index):
    print("Wrong button")
    for _ in range(3):
        leds[wrong_led_index].on()
        utime.sleep(0.25)
        leds[wrong_led_index].off()
        utime.sleep(0.25)


def start_new_round():

    global target_led_index, start_time

    utime.sleep(1)
    all_leds_off()

    target_led_index = urandom.randint(0,3)
    print("New round")
    leds[target_led_index].on()
    start_time = utime.ticks_ms()


while True:
    if(target_led_index == -1):
        if(buttons[3].value()==1):
            start_new_round()
    else:
        for i in range(len(buttons)):
            if(buttons[i].value() ==1 ):
                if(target_led_index == i):
                    end_time = utime.ticks_ms()

                    reaction_time = utime.ticks_diff(end_time, start_time)

                    print(reaction_time)
                    success_animation()

                    start_new_round()
                else:
                    error_amination(i)
                    leds[target_led_index].on()
