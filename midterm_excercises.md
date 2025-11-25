# Embedded Systems & MicroPython: Practice Exercises

This document contains 12 practice exercises designed to prepare for the midterm exam based on the course material.

**Methodology:**
1.  **Part A (PC Simulation):** Solve the algorithmic logic in a standard Python environment on your PC. Focus on logical flow, variables, and conditional statements.
2.  **Part B (Pico Implementation):** Port the logic to the Microcontroller. Replace `print()` statements with LED outputs and keyboard `input()` with physical button presses.

---

## Hardware Reference
*Based on the course specifications and pinout.*

* **LEDs (Yellow):**
    * **Y0:** GP16
    * **Y1:** GP17
    * **Y2:** GP18
    * **Y3:** GP19
* **Buttons:**
    * **B0:** GP10
    * **B1:** GP11
    * **B2:** GP12
    * **B3:** GP13

---

### 1. "Staircase Light Timer" (Retriggerable Timer)
**Concept:** Implementing a non-blocking timer that can be reset while running. This simulates a hallway light switch.

* **A) PC Simulation:**
    * Create a `while` loop that decreases a `timer` variable by 1 every cycle (simulate 1 second with `time.sleep(1)`).
    * If user input is "button", force the `timer` variable back to `10` immediately, regardless of its current value.
    * **Output:** Print "LIGHT ON" if `timer > 0`, otherwise print "DARK".
    * **Goal:** Ensure the counter does not add time (e.g., 4+10=14) but resets it (4 becomes 10).
* **B) Pico Implementation:**
    * **Hardware:** Button B0 (Input), LED Y0 (Output).
    * **Logic:** Use `time.ticks_ms()` to track time instead of `time.sleep()`.
    * If B0 is pressed, set a variable `target_time = current_time + 5000` (5 seconds).
    * Turn LED Y0 **ON**.
    * In the main loop, check if `current_time > target_time`. If true, turn LED Y0 **OFF**.
    * **Crucial:** If B0 is pressed *while* the LED is already on, update `target_time` to the new future time, effectively extending the light's duration.

### 2. Hysteresis (Thermostat Logic)
**Concept:** Filtering noise and threshold switching to prevent rapid toggling (jitter) around a setpoint.

* **A) PC Simulation:**
    * Write a function `thermostat(measured_value, current_state)`.
    * **Rules:**
        1.  If `measured_value < 18`, return `True` (Heater ON).
        2.  If `measured_value > 22`, return `False` (Heater OFF).
        3.  If value is between 18 and 22, return `current_state` (Do nothing/Hold).
    * Test with a list of values: `[17, 19, 21, 23, 21, 19, 17]`.
* **B) Pico Implementation:**
    * **Hardware:** Buttons B0 (+) and B1 (-) to control a virtual temperature variable; LED Y0 as the "Heater".
    * **Logic:** Start the "temperature" at 20.
    * Update the temperature based on button presses and print it to the console.
    * Apply the logic from Part A to control LED Y0. The LED should not flicker when the temperature is exactly 20.

### 3. Double-Click Detector
**Concept:** Measuring the time difference (`dt`) between two events to distinguish input types.

* **A) PC Simulation:**
    * Input list of timestamps: `[1.0, 1.2, 5.0, 5.8, 8.0]`.
    * Iterate through the list. Calculate `diff = current_timestamp - previous_timestamp`.
    * If `diff < 0.5`, print "DOUBLE CLICK detected". Otherwise, print "SINGLE CLICK".
* **B) Pico Implementation:**
    * **Hardware:** Button B0.
    * **Logic:**
        1.  Detect first button press (Rising edge). Store `t1 = time.ticks_ms()`.
        2.  Wait for a second press or a timeout (400ms).
        3.  If a second press occurs inside the window (`ticks_diff < 400`), flash **LED Y1** (Double Click).
        4.  If timeout occurs without a second press, flash **LED Y0** (Single Click).
    * *Note:* You must handle button bouncing to avoid false double clicks.

### 4. Pattern Recorder & Player
**Concept:** Dynamic memory storage using Lists/Arrays.

* **A) PC Simulation:**
    * Initialize an empty list: `pattern = []`.
    * Loop 5 times asking for input (0-3). Append each input to the list.
    * After the loop, iterate through `pattern` and print each value.
* **B) Pico Implementation:**
    * **Hardware:** B0 (Record/Mode), B1 (Input), LED Y0 (Output).
    * **Logic:**
        * **Record Mode:** While B0 is held down, record the timestamps of when B1 is pressed relative to the start time. Store these in a list.
        * **Play Mode:** When B0 is released, replay the sequence. Check the current time against the stored timestamps and toggle LED Y0 to match the recorded rhythm.

### 5. Deadman's Switch
**Concept:** Safety systems, watchdog timer logic, and latching alarms.

* **A) PC Simulation:**
    * (Focus on Part B for this safety logic).
* **B) Pico Implementation:**
    * **Hardware:** B0 (Keep-Alive), B1 (Reset), Y0 (Status Green), Y1 (Alarm Red).
    * **Logic:**
        * The user must press B0 at least once every 2 seconds.
        * **State 1 (Normal):** Y0 is ON. Timer resets on every B0 press.
        * **State 2 (Alarm):** If timer > 2000ms, turn Y0 OFF and start blinking Y1.
        * **Latch Constraint:** Pressing B0 *cannot* stop the alarm once it has started. You must press **B1** to reset the system to State 1.

### 6. Binary to Decimal Converter
**Concept:** Bitwise operations, binary weighting, and reading multiple inputs.

* **A) PC Simulation:**
    * Define a list representing 4 bits: `bits = [1, 0, 1, 0]`.
    * Calculate the integer: `value = (bits[0]*8) + (bits[1]*4) + (bits[2]*2) + (bits[3]*1)`.
    * Output the result (10).
* **B) Pico Implementation:**
    * **Hardware:** Buttons B3, B2, B1, B0 representing bits 3, 2, 1, 0 .
    * **Logic:**
        * Run a `while True` loop.
        * Read the state (`.value()`) of all 4 buttons.
        * Calculate the total: `(B3.value() << 3) + (B2.value() << 2) + (B1.value() << 1) + B0.value()`.
        * Print the decimal number to the console in real-time.

### 7. Traffic Light Simulator
**Concept:** Finite State Machine (FSM) implementation.

* **A) PC Simulation:**
    * Define a state variable `state` with values 0 (Red), 1 (Red-Yellow), 2 (Green), 3 (Yellow).
    * Loop through states using `time.sleep()`. Print the current state visually (e.g., `[R]`, `[RY]`, `[G]`).
* **B) Pico Implementation:**
    * **Hardware:** LEDs Y0 (Red), Y1 (Yellow), Y2 (Green).
    * **Logic:**
        * Implement the standard sequence: Red (3s) -> Red+Yellow (1s) -> Green (3s) -> Yellow (1s).
        * **Interrupt:** Configure Button B0 to trigger "Night Mode".
        * **Night Mode:** Stop the sequence and blink only Y1 (Yellow) continuously until B0 is pressed again.

### 8. "Tug of War" Game
**Concept:** Competitive counters, race conditions, and edge detection.

* **A) PC Simulation:**
    * Initialize `rope_pos = 0`.
    * Simulate two players. If Player A inputs, `rope_pos -= 1`. If Player B inputs, `rope_pos += 1`.
    * Win condition: If `abs(rope_pos) == 10`, print Winner.
* **B) Pico Implementation:**
    * **Hardware:** B0 (Left Player), B3 (Right Player), LEDs Y0-Y3 (Rope).
    * **Logic:**
        * Start with LEDs Y1 and Y2 ON (Center).
        * Wait for **rising edge** button presses (do not count holding the button).
        * Shift the lit LEDs left or right based on who pressed.
        * If the light shifts past Y0 (Left win) or Y3 (Right win), flash all LEDs to declare victory.

### 9. Logic Gate Simulator
**Concept:** Emulating digital logic circuits in software.

* **A) PC Simulation:**
    * Create a function `logic_gate(input_a, input_b, gate_type)`.
    * Based on `gate_type` ("AND", "OR", "XOR"), return the boolean result of the inputs.
* **B) Pico Implementation:**
    * **Hardware:** Buttons B0 (Input A), B1 (Input B). LEDs Y0, Y1, Y2 as outputs.
    * **Logic:**
        * **Y0 (AND):** Turn ON only if `B0==1` and `B1==1`.
        * **Y1 (OR):** Turn ON if `B0==1` or `B1==1`.
        * **Y2 (XOR):** Turn ON if `B0 != B1` (one is pressed, but not both).

### 10. Stopwatch
**Concept:** High-precision time measurement and display.

* **A) PC Simulation:**
    * Use `input("Press Enter to Start")` -> save `start_time`.
    * Use `input("Press Enter to Stop")` -> save `end_time`.
    * Print `end_time - start_time`.
* **B) Pico Implementation:**
    * **Hardware:** Button B0 (Toggle), LED Y0 (Status).
    * **Logic:**
        * Press B0: Turn Y0 ON, record `start = time.ticks_ms()`.
        * Press B0 again: Turn Y0 OFF, record `end = time.ticks_ms()`.
        * Calculate `duration = time.ticks_diff(end, start)`.
        * Print: "Elapsed time: X ms" to the serial console.

### 11. Electronic Die
**Concept:** Random Number Generation (RNG) and visual feedback.

* **A) PC Simulation:**
    * Import `random`. Generate `result = random.randint(1, 4)`.
    * Print the result.
* **B) Pico Implementation:**
    * **Hardware:** Button B0, LEDs Y0-Y3.
    * **Logic:**
        * **Animation:** When B0 is pressed, cycle through LEDs Y0->Y3 rapidly to simulate "rolling".
        * **Result:** When B0 is released (or after a set time), stop on a random number. Use `random.randint(0, 3)` to select which LED stays lit.

### 12. Bargraph Display
**Concept:** Visualizing scalar values on a discrete display.

* **A) PC Simulation:**
    * Variable `charge_level` (0 to 4).
    * Inputs `+` and `-` change the level.
    * Print visualization: `[` + `*` * level + ` ` * (4-level) + `]`.
* **B) Pico Implementation:**
    * **Hardware:** B0 (Increase), B1 (Decrease), LEDs Y0-Y3.
    * **Logic:**
        * Limit the variable between 0 and 4.
        * If level = 1: Turn Y0 ON.
        * If level = 2: Turn Y0, Y1 ON.
        * If level = 3: Turn Y0, Y1, Y2 ON, etc.
        * Ensure LEDs above the current level are turned OFF.