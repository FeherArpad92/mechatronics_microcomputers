# --- Library Imports ---
# Load the necessary modules here.

# The 'machine' module contains hardware-specific functions,
# such as controlling the GPIO (General Purpose Input/Output) pins.
import machine
# The 'time' module provides timing functions, such as delays (sleep).
import time

# --- Hardware Configuration (Pin Setup) ---
# Here, we define what is connected to each pin of the microcontroller.

# Store the GPIO pin numbers for buttons and LEDs in lists.
# This approach is much cleaner and easier to expand.
# Buttons B0, B1, B2, B3 -> on pins GP10, GP11, GP12, GP13
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

# --- Startup Message ---
# Print to the console (e.g., in the Thonny IDE) to let the user know the program has started.
print("Program is running... Press a button to toggle the corresponding LED!")
print("B0 -> Y0, B1 -> Y1, and so on.")

# --- Main Loop ---
# 'while True:' creates an infinite loop.
# The microcontroller will continuously repeat this code block as long as it has power.
while True:
    # We iterate through the buttons using a 'for' loop.
    # 'range(4)' returns the numbers 0, 1, 2, and 3, which will be our 'i' indices.
    for i in range(4):
        # Check the state of the 'i'-th button.
        # 'buttons[i].value()' reads the state of the pin associated with the button (0 or 1).
        # If the value is 1 (HIGH), it means the button is pressed.
        if buttons[i].value() == 1:
            # If the button is pressed, we toggle the state of the corresponding LED.
            # The 'leds[i].toggle()' function changes the LED's state:
            # if the LED was off, it turns on; if it was on, it turns off.
            leds[i].toggle()
            
            # --- Debouncing ---
            # The contacts of physical buttons can "bounce" when pressed, creating multiple
            # rapid signals. This section prevents that.
            # The program waits here until the button is released.
            # This ensures that a single button press results in only one toggle.
            while buttons[i].value() == 1:
                time.sleep(0.01) # A short pause to avoid unnecessarily loading the processor.
    
    # We also wait for a very short time at the end of the main loop.
    # This reduces the processor load, as it doesn't need to check the buttons
    # thousands of times per second when they aren't being pressed.
    time.sleep(0.01)