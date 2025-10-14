# --- Library Imports ---
# These lines load pre-written code modules that give us access to
# the microcontroller's hardware and timing functions.
import machine      # Provides functions to control GPIO pins, including PWM.
import utime        # Provides functions for creating delays (sleeping).

# --- Hardware Configuration (Pin Setup) ---
# Here, we create variables to hold the GPIO pin numbers we are using.
# This makes the code easier to read and modify if we change the wiring.

# LEDs will be controlled via PWM to adjust their brightness.
# Y0 -> GP16
# Y1 -> GP17
# Y2 -> GP18
# Y3 -> GP19
led_pins = [16, 17, 18, 19]

# Define the pins for our three control buttons.
increase_button_pin = 10 # Button B0 (GP10) will increase brightness.
decrease_button_pin = 11 # Button B1 (GP11) will decrease brightness.
toggle_button_pin = 12   # Button B2 (GP12) will toggle the LEDs on/off.

# --- Hardware Initialization ---
# Now we create the actual objects that will control the hardware.

# This line creates a list of PWM objects, one for each LED pin.
# PWM (Pulse-Width Modulation) works by turning a pin on and off very quickly.
# The 'duty cycle' is the percentage of time the pin is ON. A higher duty cycle
# means the LED is on for longer in each cycle, making it appear brighter to the human eye.
# The 'freq' (frequency) is how many on/off cycles happen per second. 1000 Hz is
# fast enough to be completely invisible and prevent any flickering.
led_pwms = [machine.PWM(machine.Pin(pin)) for pin in led_pins]
for pwm in led_pwms:
    pwm.freq(1000)

# We create Pin objects for the buttons, configured as INPUTS with PULL_DOWN resistors.
# This setup ensures we read a stable LOW signal when a button is not pressed.
increase_button = machine.Pin(increase_button_pin, machine.Pin.IN, machine.Pin.PULL_DOWN)
decrease_button = machine.Pin(decrease_button_pin, machine.Pin.IN, machine.Pin.PULL_DOWN)
toggle_button = machine.Pin(toggle_button_pin, machine.Pin.IN, machine.Pin.PULL_DOWN)

# --- Global Variables ---
# These variables store the state of our dimmer and can be accessed from anywhere.
# We store brightness as a percentage (0-100) to make it user-friendly.
brightness_level = 50 # Start at 50% brightness.
saved_brightness = 50 # Stores the brightness when the LEDs are toggled off.
leds_on = True        # A flag to track the toggle state. True means on, False means off.

# --- Helper Function to Set LED Brightness ---
def set_all_leds_brightness(level):
    """
    This function takes a brightness level percentage (0-100) and applies it
    to all LEDs by setting their PWM duty cycle.
    """
    # The duty cycle on the Pico is a 16-bit value, from 0 (0% on) to 65535 (100% on).
    # We must convert our 0-100 percentage scale to this 0-65535 scale.
    # Formula: duty = (percentage / 100) * 65535
    if level <= 0:
        duty_cycle = 0
    elif level >= 100:
        duty_cycle = 65535
    else:
        duty_cycle = int((level / 100) * 65535)
    
    # Apply the calculated duty cycle to every PWM object in our list.
    for pwm in led_pwms:
        pwm.duty_u16(duty_cycle)

# --- Startup ---
# This code block runs only once when the microcontroller is powered on or reset.
print("PWM Dimmer is running...")
print("B0 (GP10): Increase | B1 (GP11): Decrease | B2 (GP12): Toggle On/Off")
# Set the initial brightness of the LEDs when the program starts.
set_all_leds_brightness(brightness_level)

# --- Main Loop ---
# The 'while True:' statement creates an infinite loop. The code inside will
# run over and over, continuously checking for button presses.
while True:
    # --- Check for Increase Button Press ---
    if increase_button.value() == 1:
        # If the LEDs were toggled off, pressing a brightness button should turn them back on.
        leds_on = True
        
        # Increase brightness by 10, but not past 100.
        # The min() function is a clean way to "clamp" the value to a maximum of 100.
        brightness_level = min(100, brightness_level + 10)
        
        # Update the hardware.
        set_all_leds_brightness(brightness_level)
        print(f"Brightness: {brightness_level}%")
        
        # Debounce: Pause the code as long as the button is held down to ensure
        # one physical press results in only one action.
        while increase_button.value() == 1:
            utime.sleep(0.05)

    # --- Check for Decrease Button Press ---
    if decrease_button.value() == 1:
        leds_on = True # Also turn LEDs on if they were off.
        
        # Decrease brightness by 10, but not below 0.
        # The max() function clamps the value to a minimum of 0.
        brightness_level = max(0, brightness_level - 10)
        
        set_all_leds_brightness(brightness_level)
        print(f"Brightness: {brightness_level}%")
        
        # Debounce for the decrease button.
        while decrease_button.value() == 1:
            utime.sleep(0.05)

    # --- Check for Toggle Button Press ---
    if toggle_button.value() == 1:
        # Flip the state of our toggle flag (True becomes False, False becomes True).
        leds_on = not leds_on
        
        if leds_on:
            # If we are turning the LEDs ON:
            # Restore the main brightness level from our saved variable.
            brightness_level = saved_brightness
            set_all_leds_brightness(brightness_level)
            print(f"LEDs Toggled ON to {brightness_level}%")
        else:
            # If we are turning the LEDs OFF:
            # First, save the current brightness so we can restore it later.
            # We only save if the brightness is not already 0.
            if brightness_level > 0:
                saved_brightness = brightness_level
            # Then, set the actual brightness to 0.
            set_all_leds_brightness(0)
            print("LEDs Toggled OFF")
        
        # Debounce for the toggle button.
        while toggle_button.value() == 1:
            utime.sleep(0.05)
            
    # Add a very small delay at the end of every loop to make the system more efficient.
    utime.sleep(0.01)