import machine
import utime

led_pins = [16, 17, 18, 19]

increase_button_pin = 10
decrease_button_pin = 11
toggle_button_pin = 12

led_pwms = [machine.PWM(machine.Pin(pin)) for pin in led_pins]

for pwm in led_pwms: pwm.freq(1000)

brigthness_level = 50
saved_brightness_level = 50
leds_on = True

increase_button = machine.Pin(increase_button_pin, machine.Pin.IN, machine.Pin.PULL_DOWN)
decrease_button = machine.Pin(decrease_button_pin, machine.Pin.IN, machine.Pin.PULL_DOWN)
toggle_button = machine.Pin(toggle_button_pin, machine.Pin.IN, machine.Pin.PULL_DOWN)

def set_all_leds_brightness(level):

    if level<=0:
        duty_cycle = 0
    elif level>=100:
        duty_cycle = 65535
    else:
        duty_cycle = int((level/100)* 65535)

    for pwm in led_pwms: pwm.duty_u16(duty_cycle)

while True:
    if(increase_button.value() == 1):

        leds_on = True

        brigthness_level = min(100, brigthness_level+10)

        set_all_leds_brightness(brigthness_level)
        print(brigthness_level)

        #while increase_button.value() == 1:
        utime.sleep(0.05)

    if(decrease_button.value() == 1):

        leds_on = True

        brigthness_level = max(0, brigthness_level-10)

        set_all_leds_brightness(brigthness_level)
        print(brigthness_level)

        #while increase_button.value() == 1:
        utime.sleep(0.05)

    if(toggle_button.value() == 1):

        leds_on = not leds_on

        if(leds_on):
            brigthness_level = saved_brightness_level
            set_all_leds_brightness(brigthness_level)
            print("Turn ON LEDs")
        else:
            if(brigthness_level>0): saved_brightness_level = brigthness_level

            set_all_leds_brightness(0)
            print("Turn OFF LEDs")

        utime.sleep(0.05)
    utime.sleep(0.1)

    