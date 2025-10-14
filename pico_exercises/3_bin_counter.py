# --- Library Imports ---
# These lines load pre-written code modules that give us access to
# the microcontroller's hardware and timing functions.
import machine # Provides functions to control GPIO pins.
import time    # Provides functions for creating delays (sleeping).

# --- Hardware Configuration (Pin Setup) ---
# Here, we create variables to hold the GPIO pin numbers we are using.
# This makes the code easier to read and modify if we change the wiring.

# LEDs will represent the 4 bits of a binary number.
# We list them from the Least Significant Bit (LSB) to the Most Significant Bit (MSB).
# LSB (1s place) -> Y0 -> GP16
#      (2s place) -> Y1 -> GP17
#      (4s place) -> Y2 -> GP18
# MSB (8s place) -> Y3 -> GP19
led_pins = [16, 17, 18, 19]

# Define the pins for our two control buttons.
increment_button_pin = 10 # Button 1 (GP10) will increase the count.
reset_button_pin = 11     # Button 2 (GP11) will reset the count to 0.

# --- Hardware Initialization ---
# Now we create the actual objects that will control the hardware pins.

# This line uses a "list comprehension" to create a list of Pin objects for our LEDs.
# Each pin in the 'led_pins' list is configured as an OUTPUT, because the Pico
# sends a signal OUT to the LED to turn it on or off.
leds = [machine.Pin(pin, machine.Pin.OUT) for pin in led_pins]

# We create Pin objects for the buttons, configured as INPUTS.
# The microcontroller will READ a signal from these pins to see if a button is pressed.
# 'machine.Pin.PULL_DOWN' activates an internal resistor that "pulls" the pin's
# voltage down to 0V (LOW) when the button is NOT pressed. This prevents a "floating"
# state and ensures we read a stable LOW signal. When pressed, the button connects
# the pin to 3.3V, and we read a HIGH signal.
increment_button = machine.Pin(increment_button_pin, machine.Pin.IN, machine.Pin.PULL_DOWN)
reset_button = machine.Pin(reset_button_pin, machine.Pin.IN, machine.Pin.PULL_DOWN)

# --- Global Variables ---
# This variable will store the current number in our counter.
# It's "global" because it's defined outside of any function and can be
# accessed and modified from anywhere in the script.
counter = 0

# --- Helper Function to Display Number in Binary ---
def display_binary(number):
    """
    This function takes an integer and turns the LEDs on or off
    to show its 4-bit binary representation.
    """
    # This loop iterates four times, once for each LED/bit (0, 1, 2, 3).
    for i in range(4):
        # This is the core logic using bitwise operations. Let's break it down:
        # 1. `(number >> i)`: This is a "right bit shift". It shifts the binary
        #    representation of 'number' to the right by 'i' places.
        #    Example: If number is 5 (binary 0101) and i is 2, `5 >> 2` results in 0001.
        #    This effectively isolates each bit, moving it to the 1s place.
        # 2. `& 1`: This is a "bitwise AND". It compares the result with 1 (binary 0001).
        #    If the isolated bit is 1, the result of the AND is 1 (True).
        #    If the isolated bit is 0, the result of the AND is 0 (False).
        if (number >> i) & 1:
            leds[i].on() # If the bit is 1, turn the corresponding LED on.
        else:
            leds[i].off() # If the bit is 0, turn the corresponding LED off.

# --- Startup ---
# This code block runs only once when the microcontroller is powered on or reset.
print("Binary counter is running...")
print("Press Button 1 (GP10) to increment, Button 2 (GP11) to reset.")
# Initially, display 0 on the LEDs to show the starting state.
display_binary(counter)

# --- Main Loop ---
# The 'while True:' statement creates an infinite loop. The code inside this
# loop will run over and over again, continuously checking the buttons.
while True:
    # --- Check for Increment Button Press ---
    # `increment_button.value() == 1` checks if a HIGH signal (3.3V) is read,
    # which means the button is currently being pressed.
    if increment_button.value() == 1:
        # Increment the counter. We use the modulo operator (%) to make it
        # wrap around. After 15, `(15 + 1) % 16` becomes `16 % 16`, which is 0.
        counter = (counter + 1) % 16
        
        # Call our helper function to update the LEDs.
        display_binary(counter)
        # Print the new value to the console for debugging.
        print(f"Counter incremented to: {counter}")
        
        # Debounce Logic: This is a simple but important technique.
        # Physical buttons can "bounce" when pressed, creating multiple rapid
        # signals. This inner loop pauses the code as long as the button is held
        # down, ensuring that one press only results in one count.
        while increment_button.value() == 1:
            time.sleep(0.05) # Wait a short moment before checking again.

    # --- Check for Reset Button Press ---
    # This logic is identical to the increment button check.
    if reset_button.value() == 1:
        # Reset the counter variable to zero.
        counter = 0
        
        # Update the LEDs to show the reset state.
        display_binary(counter)
        print("Counter reset to 0.")
        
        # Debounce for the reset button.
        while reset_button.value() == 1:
            time.sleep(0.05)
            
    # Add a very small delay at the end of every loop. This prevents the
    # microcontroller's CPU from running at 100% speed, which is more
    # efficient and saves a tiny amount of power.
    time.sleep(0.01)