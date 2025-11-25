Íme az elkészített `.md` fájl angol nyelven, amely tartalmazza mind a 20 generált feladatot, a megfelelő struktúrában (PC szimuláció vs. Pico implementáció).

A feladatok elején összefoglaltam a hardveres bekötést a PDF alapján, hogy ne kelljen minden feladatnál külön keresgélni.

```markdown
# Embedded Systems & MicroPython: Practice Exercises

This document contains 20 practice exercises designed to prepare for the midterm exam.
**Methodology:**
1.  **Part A (PC Simulation):** Solve the algorithmic logic in a standard Python environment on your PC (using `print` for output and `input` or variables for input).
2.  **Part B (Pico Implementation):** Port the logic to the Microcontroller, replacing `print` with LEDs and `input` with Buttons/Sensors.

---

## Hardware Reference (Based on Course PDF)

* **LEDs (Yellow):**
    * Y0: GP16
    * Y1: GP17
    * Y2: GP18
    * Y3: GP19
* **Buttons:**
    * B0: GP10
    * B1: GP11
    * B2: GP12
    * B3: GP13
* [cite_start]**Documentation:** [cite: 556-559][cite_start], [cite: 490-492][cite_start], [cite: 502]

---

## Set 1: Timing, Logic & Data Structures

### 1. Morse Encoder
**Concept:** String manipulation and timing sequences.
* **A) PC Simulation:** Write a function that converts an input string (e.g., "SOS") into a list of 0s and 1s.
    * Rule: "." = 1 unit signal, "-" = 3 units signal. 1 unit pause between signals, 3 units pause between letters.
    * Input: `"A"` (.-) -> Output: `[1, 0, 1, 1, 1]` (short, pause, long).
* **B) Pico Implementation:** The Pico waits for a hardcoded string (e.g., "HELLO"). Iterate through the generated list:
    * If `1`: Turn LED ON for 200ms.
    * If `0`: Turn LED OFF for 200ms.

### 2. "Staircase Timer" (Retriggerable Timer)
**Concept:** Non-blocking timer reset logic.
* **A) PC Simulation:** Simulate a loop where a `timer` variable counts down.
    * If you input "button", set `timer` to 10.
    * If `timer > 0`, print "LIGHT ON". If 0, print "DARK".
    * *Crucial:* If "button" is input while the timer is at 4, it must jump back to 10 immediately (not add up).
* **B) Pico Implementation:** Use Button B0 and LED Y0.
    * Pressing B0 turns Y0 ON for 5 seconds.
    * Pressing B0 *again* during those 5 seconds resets the timer to 5 seconds (preventing the light from turning off).

### 3. Hysteresis (Thermostat Logic)
**Concept:** Filtering noise and threshold switching.
* **A) PC Simulation:** Write a function `thermostat(measured_value, current_state)`.
    * Target: 20.
    * Switch ON (return True) only if `measured_value < 18`.
    * Switch OFF (return False) only if `measured_value > 22`.
    * Between 18 and 22, maintain the `current_state`.
* **B) Pico Implementation:** Simulate temperature with buttons.
    * B0 increases virtual temp, B1 decreases it. Print the temp to console.
    * LED Y0 indicates "Heating" based on the hysteresis logic above (prevents flickering around the target).

### 4. Double-Click Detector
**Concept:** Time difference measurement (`dt`).
* **A) PC Simulation:** Given a list of timestamps: `[1.0, 1.2, 5.0, 5.8, 8.0]`.
    * Iterate through. If `current - previous < 0.5`, print "DOUBLE CLICK".
    * Else, print "SINGLE CLICK".
* **B) Pico Implementation:** Monitor Button B0.
    * Single press: Flash LED Y0 briefly.
    * Two presses within 400ms: Flash LED Y1 (different color/position).
    * *Hint:* Use `time.ticks_ms()` and `time.ticks_diff()`.

### 5. Parking Sensor Simulation
**Concept:** Mapping a value range to frequency.
* **A) PC Simulation:** Logic that monitors a `distance` variable (0-100).
    * Create a formula/if-structure for `delay`.
    * Small distance (10) -> Small delay (0.1s).
    * Large distance (100) -> Large delay (1.0s).
* **B) Pico Implementation:** Use B0 and B1 to adjust a virtual "distance" variable.
    * LED Y0 blinks continuously.
    * The blinking speed (frequency) changes dynamically based on the virtual distance.

---

## Set 2: Advanced Control & Input Handling

### 6. "Soft Start" (Light Ramp)
**Concept:** PWM (Pulse Width Modulation) and Duty Cycle loops.
* **A) PC Simulation:** Generate a list of numbers from 0 to 100 and back to 0 with a step of 5.
    * Output: `[0, 5, 10, ... 100, 95, ... 0]`. This represents brightness levels.
* [cite_start]**B) Pico Implementation:** Use hardware PWM on an LED[cite: 601].
    * On Button Press: Do not turn ON instantly. "Fade in" from 0% to 100% duty cycle over 1 second.
    * On Button Release: "Fade out" to 0%.

### 7. Pattern Recorder & Player
**Concept:** Arrays and Memory storage.
* **A) PC Simulation:** Create an empty list.
    * Ask user for 5 numbers (0-3), append to list.
    * "Playback": Print the numbers in the list sequentially.
* **B) Pico Implementation:**
    * **Record Mode (Hold B0):** Listen for B1 presses. Save the timestamps or states to a list.
    * **Play Mode (Release B0):** LED flashes back the exact rhythm recorded.

### 8. Deadman's Switch
**Concept:** Safety logic, timeout resets, and latching alarms.
* **A) PC Simulation:** A loop running every second.
    * Check: `current_time - last_signal_time > 3`?
    * If yes: Print "ALARM!". If no: "OK".
    * Randomly update `last_signal_time` (simulating a button press).
* **B) Pico Implementation:** User must press B0 at least every 2 seconds.
    * Normal state: Green LED (Y0) ON.
    * Timeout ( > 2s): Red LED (Y1) starts blinking (Alarm).
    * *Constraint:* The Alarm cannot be stopped by B0. You must press B1 (Reset) to clear the error.

### 9. Binary to Decimal Converter
**Concept:** Bitwise operations and weighting.
* **A) PC Simulation:** Given a list of 4 booleans: `bits = [1, 0, 1, 0]`.
    * Calculate the decimal integer (1*8 + 0*4 + 1*2 + 0*1). Output: 10.
* **B) Pico Implementation:** Use buttons B0-B3 as bits.
    * B3=8, B2=4, B1=2, B0=1.
    * Continuously read the state of all 4 buttons (pressed/held).
    * Print the calculated decimal value to the Shell/REPL in real-time.

### 10. Software Debounce Logic
**Concept:** Signal stability verification.
* **A) PC Simulation:** Noisy data array: `[0, 0, 1, 0, 1, 1, 1, 1, 0, 0]`.
    * Goal: Detect when the signal *stably* changes from 0 to 1.
    * Logic: Only consider it a "Press" if 3 consecutive values are `1`.
* **B) Pico Implementation:** Write a custom function `debounce(pin)`.
    * Read pin. If High, wait 10ms, read again.
    * Return `True` only if both reads are High.
    * Use this to toggle an LED reliably.

---

## Set 3: State Machines & Logic Gates

### 11. Traffic Light Simulator
**Concept:** Finite State Machine (FSM).
* **A) PC Simulation:** Define states: `RED`, `RED_YELLOW`, `GREEN`, `YELLOW`.
    * Infinite loop cycling through states.
    * Print visual representation: `[O] [ ] [ ]` (Red), etc.
* **B) Pico Implementation:** Map states to LEDs (Y0=Red, Y1=Yellow, Y2=Green).
    * Implement standard timing (e.g., Red 3s, Yellow 1s).
    * *Extra:* Button B0 triggers "Night Mode" (blinking Yellow only).

### 12. "Tug of War" Game
**Concept:** Competitive counters and race conditions.
* **A) PC Simulation:** Variable `rope_position = 0`.
    * Random events increment (Player B) or decrement (Player A) the value.
    * If value hits -10 or +10, declare winner.
* **B) Pico Implementation:**
    * B0 = Left Player, B3 = Right Player.
    * LEDs Y0-Y3 represent the rope. Start at center (Y1+Y2 ON).
    * Fastest button masher moves the light to their side. Reaching the edge wins.

### 13. Bit Shifter
**Concept:** Shift Registers logic.
* **A) PC Simulation:** List: `register = [0, 0, 1, 0]`.
    * Command "left": `[0, 1, 0, 0]`.
    * Command "right": `[0, 0, 0, 1]`.
* **B) Pico Implementation:** Only one LED is ON at a time.
    * B0 shifts the active LED to the left.
    * B1 shifts the active LED to the right.
    * Implement bounds checking (don't shift off the board).

### 14. "Breathing" LED
**Concept:** Mathematical functions (Sine) applied to hardware.
* **A) PC Simulation:** Loop from 0 to 360 degrees.
    * Calculate `y = (sin(x) + 1) / 2`.
    * Print `*` characters proportional to `y` to visualize the wave.
* **B) Pico Implementation:** Select LED Y0.
    * Configure as PWM.
    * Update Duty Cycle continuously using the sine wave formula to create a smooth pulsing effect (not linear fading).

### 15. Logic Gate Simulator
**Concept:** Boolean Algebra.
* **A) PC Simulation:** Function `gate(a, b, type)`.
    * Returns result of `a AND b` or `a OR b` based on type.
* **B) Pico Implementation:**
    * Inputs: Buttons B0 and B1.
    * Output Y0: Visualizes **AND** (On if B0 & B1 pressed).
    * Output Y1: Visualizes **OR** (On if B0 | B1 pressed).
    * Output Y2: Visualizes **XOR** (On if only one is pressed).

---

## Set 4: Measurement & Visualization

### 16. Stopwatch
**Concept:** Precise Time Measurement.
* **A) PC Simulation:** Use `time.time()`.
    * Enter key starts timer.
    * Enter key stops timer.
    * Print duration.
* **B) Pico Implementation:**
    * Button B0 toggles Start/Stop.
    * LED Y0 indicates "Running".
    * On Stop, print precise duration (e.g., "4.52 seconds") to Serial using `ticks_ms`.

### 17. Latching Safety Circuit
**Concept:** Industrial Logic (Start vs. E-Stop).
* **A) PC Simulation:** Variables `running = False`, `emergency = False`.
    * START command: Sets running=True (only if not emergency).
    * STOP command: Sets running=False, emergency=True.
    * RESET command: Sets emergency=False.
* **B) Pico Implementation:**
    * B0 (Start): Turns Y0 ON.
    * B1 (E-Stop): Turns Y0 OFF, Turns Y3 ON (Error).
    * *Latch:* B0 cannot turn Y0 back ON until B2 (Reset) is pressed to clear Y3.

### 18. Electronic Die
**Concept:** Random Number Generation (RNG).
* **A) PC Simulation:** Import `random`.
    * Generate number 1-4. Print "Rolled: 3".
* **B) Pico Implementation:** Use `urandom`.
    * Button B0 triggers animation (LEDs cycling fast).
    * Stops on a random LED (Y0-Y3) representing the dice roll 1-4.

### 19. Bargraph Display
**Concept:** Visualizing magnitude.
* **A) PC Simulation:** Variable `charge = 0` (max 4).
    * `+` increments, `-` decrements.
    * Visual: 1=`[*]`, 3=`[***]`.
* **B) Pico Implementation:**
    * B0 increases value, B1 decreases value.
    * LEDs act as a battery bar:
        * Level 1: Y0 ON.
        * Level 2: Y0, Y1 ON.
        * Level 3: Y0, Y1, Y2 ON...

### 20. Rhythm Detector
**Concept:** Interval comparison.
* **A) PC Simulation:** User presses Enter 3 times.
    * Measure interval T1 (press 1-2) and T2 (press 2-3).
    * If `abs(T1 - T2) < threshold`, print "Good Rhythm".
* **B) Pico Implementation:**
    * User taps B0 to a beat.
    * Pico measures time between taps.
    * If the rhythm is consistent (intervals are similar), blink Green (Y0). If erratic, blink Red (Y3).
```