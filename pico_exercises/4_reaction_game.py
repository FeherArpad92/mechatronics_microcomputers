# --- Library Imports ---
# These lines load pre-written code modules that give us access to
# the microcontroller's hardware, timing functions, and random number generation.
import machine      # Provides functions to control GPIO pins.
import utime        # Provides functions for creating delays (sleep) and precise timing.
import urandom      # Provides functions for generating random numbers.

# --- Hardware Configuration (Pin Setup) ---
# Here, we create variables to hold the GPIO pin numbers we are using.
# This makes the code easier to read and modify if we change the wiring.

# LEDs are our output indicators.
# Y0 -> GP16
# Y1 -> GP17
# Y2 -> GP18
# Y3 -> GP19
led_pins = [16, 17, 18, 19]

# Buttons are our user inputs. The index of each button corresponds to the
# index of the LED it controls.
# B0 -> GP10 (Controls Y0)
# B1 -> GP11 (Controls Y1)
# B2 -> GP12 (Controls Y2)
# B3 -> GP13 (Controls Y3 and starts the game)
button_pins = [10, 11, 12, 13]

# --- Hardware Initialization ---
# Now we create the actual objects that will control the hardware pins.

# This line uses a "list comprehension" to create a list of Pin objects for our LEDs.
# Each pin is configured as an OUTPUT, as the Pico sends a signal OUT to the LED.
leds = [machine.Pin(pin, machine.Pin.OUT) for pin in led_pins]

# This creates a list of Pin objects for our buttons, configured as INPUTS.
# The microcontroller READS signals from these pins.
# 'machine.Pin.PULL_DOWN' activates an internal resistor that pulls the pin's
# voltage to 0V (LOW) when the button is NOT pressed. This ensures a stable
# signal. When pressed, the button connects the pin to 3.3V, and we read HIGH.
buttons = [machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_DOWN) for pin in button_pins]

# --- Global Variables ---
# These variables hold the state of the game and can be accessed from anywhere.
target_led_index = -1 # Stores the index (0-3) of the currently lit LED. -1 means the game is waiting to start.
start_time = 0        # Stores the timestamp when an LED turns on, used for calculating reaction time.

# --- Helper Functions for Animations ---
def all_leds_off():
    """A simple utility function to turn off all LEDs."""
    for led in leds:
        led.off()

def success_animation():
    """Flashes all LEDs twice quickly to indicate a correct answer."""
    print("Correct!")
    for _ in range(2): # Repeat the flash sequence twice
        for led in leds:
            led.on()
        utime.sleep(0.1)
        all_leds_off()
        utime.sleep(0.1)

def error_animation(wrong_led_index):
    """Blinks the LED corresponding to the wrong button pressed."""
    print(f"Wrong button! The target is LED {target_led_index}.")
    for _ in range(3): # Repeat the blink sequence three times
        leds[wrong_led_index].on()
        utime.sleep(0.25)
        leds[wrong_led_index].off()
        utime.sleep(0.25)
        
# --- Main Game Logic Function ---
def start_new_round():
    """
    This function prepares and starts a new round of the game.
    It's a "global" function because it modifies global variables.
    """
    global target_led_index, start_time
    
    utime.sleep(1) # Pause for a second before the next round starts.
    all_leds_off()
    
    # Pick a new random LED index from 0 to 3.
    target_led_index = urandom.randint(0, 3)
    print("--------------------")
    print(f"New round! Get ready for LED {target_led_index}...")
    
    # Turn on the randomly selected target LED.
    leds[target_led_index].on()
    
    # Record the precise moment the LED was turned on.
    start_time = utime.ticks_ms()

# --- Startup Message ---
# This code runs only once when the script starts.
print("Reaction Game Started!")
print("Press Button B3 (GP13) to begin the first round.")

# --- Main Loop ---
# The 'while True:' statement creates an infinite loop. The code inside this
# loop will run over and over again, continuously checking the buttons.
while True:
    # --- Game Start Logic ---
    # Check if the game is in the "waiting to start" state.
    if target_led_index == -1:
        # The game is started/triggered by Button B3 (index 3).
        if buttons[3].value() == 1:
            start_new_round()
            # Debounce: Wait for the button to be released.
            while buttons[3].value() == 1:
                pass 
    
    # --- Active Gameplay Logic ---
    # If the game is running (an LED is lit).
    else:
        # Loop through all our buttons to see if any are pressed.
        for i in range(len(buttons)):
            if buttons[i].value() == 1:
                # A button has been pressed!
                
                # --- Check if the Correct Button was Pressed ---
                if i == target_led_index:
                    # Calculate reaction time. utime.ticks_diff handles timer wrap-around.
                    end_time = utime.ticks_ms()
                    reaction_time = utime.ticks_diff(end_time, start_time)
                    print(f"Reaction time: {reaction_time} ms")
                    
                    # Run success animation.
                    success_animation()
                    
                    # Start the next round.
                    start_new_round()
                    
                # --- Handle Incorrect Button Press ---
                else:
                    # Run the error animation on the LED that corresponds to the WRONG button.
                    error_animation(i)
                    # Turn the target LED back on, as the round is not over.
                    leds[target_led_index].on()
                    
                # Debounce: After handling any press, wait for the button to be released
                # to prevent a single long press from registering multiple times.
                while buttons[i].value() == 1:
                    pass
                
                # We've handled a button press, so we can break out of the inner for-loop
                # and start the main while-loop's check from the beginning.
                break 

    # A small delay in each loop iteration to prevent the CPU from running at 100%.
    utime.sleep(0.01)