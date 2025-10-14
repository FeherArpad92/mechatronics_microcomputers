# --- Library Imports ---
# These lines load pre-written code modules that give us access to
# the microcontroller's hardware and timing functions.
import machine      # Provides functions to control GPIO pins.
import utime        # Provides functions for creating delays (sleeping).

# --- Hardware Configuration (Pin Setup) ---
# Here, we create variables to hold the GPIO pin numbers we are using.
# This makes the code easier to read and modify if we change the wiring.

# LEDs are our output indicators for progress.
# Y0 -> GP16
# Y1 -> GP17
# Y2 -> GP18
# Y3 -> GP19
led_pins = [16, 17, 18, 19]

# Buttons are our user inputs. The index of each button corresponds to a value
# that we will use in our secret combination.
# B0 -> GP10 (Index 0)
# B1 -> GP11 (Index 1)
# B2 -> GP12 (Index 2)
# B3 -> GP13 (Index 3)
button_pins = [10, 11, 12, 13]

# --- Hardware Initialization ---
# Now we create the actual objects that will control the hardware.

# Create a list of Pin objects for our LEDs, configured as OUTPUTs.
leds = [machine.Pin(pin, machine.Pin.OUT) for pin in led_pins]

# Create a list of Pin objects for our buttons, configured as INPUTS
# with PULL_DOWN resistors.
buttons = [machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_DOWN) for pin in button_pins]

# --- Global Variables and Constants ---
# This is the secret combination. The numbers correspond to the button indices.
# For example, [1, 3, 0] means the user must press B1, then B3, then B0.
# Feel free to change this sequence!
SECRET_COMBINATION = [1, 3, 0]

# This list will store the sequence of buttons the user has pressed so far.
# We will compare this list against the secret combination.
user_input_sequence = []

# --- Helper Functions for Animations and State ---
def all_leds_off():
    """A simple utility function to turn off all LEDs."""
    for led in leds:
        led.off()

def update_progress_leds():
    """Lights up LEDs to show how many correct inputs have been entered."""
    all_leds_off() # First, clear all LEDs.
    # Turn on one LED for each correct entry in the user's sequence.
    for i in range(len(user_input_sequence)):
        leds[i].on()

def success_animation():
    """Blinks all LEDs rapidly to indicate the lock is "unlocked"."""
    print("Unlocked!")
    # Repeat the blink sequence 10 times for a visible effect.
    for _ in range(10):
        for led in leds:
            led.on()
        utime.sleep(0.1)
        all_leds_off()
        utime.sleep(0.1)

def error_animation():
    """Flashes all LEDs once to indicate a wrong button press."""
    print("Wrong input. Resetting...")
    for led in leds:
        led.on()
    utime.sleep(0.5)
    all_leds_off()

def reset_lock():
    """Resets the lock state to the beginning."""
    global user_input_sequence
    user_input_sequence = [] # Empty the user's input list.
    all_leds_off()           # Turn off all progress LEDs.
    print("Enter the combination...")

# --- Startup ---
# This code block runs only once when the script starts.
print("Combination Lock is ready.")
reset_lock() # Call reset to ensure a clean starting state.

# --- Main Loop ---
# The 'while True:' statement creates an infinite loop. The code inside will
# run over and over, continuously checking for button presses.
while True:
    # We use enumerate to get both the index (i) and the button object itself.
    # The index 'i' (0, 1, 2, or 3) is what we use for our combination logic.
    for i, button in enumerate(buttons):
        # Check if a button is being pressed.
        if button.value() == 1:
            print(f"Button {i} pressed.")
            
            # Add the pressed button's index to our input sequence.
            user_input_sequence.append(i)
            
            # --- Check if the input so far is correct ---
            # We get the part of the secret code that we should be matching.
            # For example, if user has pressed 2 buttons, we check against the first 2
            # items of the SECRET_COMBINATION.
            expected_sequence_part = SECRET_COMBINATION[:len(user_input_sequence)]
            
            if user_input_sequence == expected_sequence_part:
                # --- Correct input ---
                print("Correct so far.")
                update_progress_leds() # Show the user their progress.
                
                # Check if the full combination has been entered correctly.
                if len(user_input_sequence) == len(SECRET_COMBINATION):
                    success_animation()
                    reset_lock() # Reset for the next attempt.
            else:
                # --- Incorrect input ---
                error_animation()
                reset_lock() # Reset on failure.
            
            # Debounce Logic: Wait here as long as the button is held down.
            # This ensures that one press is only registered once.
            while button.value() == 1:
                utime.sleep(0.05)
                
    # Add a small delay at the end of every loop to make the system more efficient.
    utime.sleep(0.01)