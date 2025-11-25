import machine
import utime

led_pins = [16,17,18,19]
button_pins = [10,11,12,13]

leds = [machine.Pin(pin, machine.Pin.OUT) for pin in led_pins]

buttons = [machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_DOWN) for pin in button_pins]

SECRET_COMBINATION = [1,3,0]

user_input_sequence = []

def all_leds_off():
    for led in leds:
        led.off()


def update_pregress_leds():
    all_leds_off()
    for i in range(len(user_input_sequence)):
        leds[i].on()

def success_animation():
    print("Success")

def error_animation():
    print("Error")

def reset_lock():
    global user_input_sequence
    user_input_sequence = []
    all_leds_off()
    print("Enter combination")


reset_lock()

while True:

    for i, button in enumerate(buttons):

        if(button.value()==1):

            print("Button pressed")

            user_input_sequence.append(i)

            expected_sequance_part = SECRET_COMBINATION[:len(user_input_sequence)]

            if user_input_sequence == expected_sequance_part:
                print("correct")
                update_pregress_leds()

                if(len(user_input_sequence) == len(SECRET_COMBINATION)):
                    success_animation()
                    reset_lock()
            else:
                error_animation()
                reset_lock()
    utime.sleep(0.1)


