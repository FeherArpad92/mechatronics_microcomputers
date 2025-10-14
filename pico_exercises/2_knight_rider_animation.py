# --- Library Imports ---
# Load the necessary modules here.

# The 'machine' module contains hardware-specific functions,
# such as controlling the GPIO (General Purpose Input/Output) pins.
import machine
# The 'time' module provides timing functions, such as delays (sleep).
import time

# --- Hardware Configuration (Pin Setup) ---
# Here, we define what is connected to each pin of the microcontroller.

# Store the GPIO pin numbers for the LEDs in a list.
# LEDs Y0, Y1, Y2, Y3 -> on pins GP16, GP17, GP18, GP19
led_pins = [16, 17, 18, 19]

# Create a list of 'Pin' objects to control the LEDs.
# The 'for' loop iterates through the 'led_pins' list.
# Each pin is configured as an OUTPUT (OUT) because the microcontroller sends signals to the LEDs.
leds = [machine.Pin(pin, machine.Pin.OUT) for pin in led_pins]

# --- Animation Configuration ---
# Set the delay between each step of the animation in seconds.
# 150 milliseconds is 0.150 seconds.
delay = 0.150

# Define the sequence of LED indices for one full back-and-forth animation.
# This makes the main loop cleaner and separates the animation "data" from the "logic".
animation_sequence = [0, 1, 2, 3, 2, 1]

# --- Startup Message ---
# Print to the console to let the user know the program has started.
print("Program is running... Knight Rider animation started!")

# --- Main Loop ---
# 'while True:' creates an infinite loop for the animation.
while True:
    # Iterate through the predefined animation sequence.
    # For each number in the list, we light up the corresponding LED.
    for i in animation_sequence:
        leds[i].on()      # Turn the current LED on.
        time.sleep(delay) # Wait for the specified delay time.
        leds[i].off()     # Turn the current LED off before moving to the next