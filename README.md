# The Cube

An interactive, microcontroller-based audio-visual project running CircuitPython / MicroPython. The device plays distinct audio feedback (`red.mp3`, `yellow.mp3`, `green.mp3`) corresponding to state changes, inputs, or color modes[cite: 1].

---

## Repository Structure

```text
├── LICENSE
├── README.md
└── code/
    ├── code.py      # Main entry point and control logic
    ├── green.mp3    # Audio asset for green state/trigger
    ├── red.mp3      # Audio asset for red state/trigger
    └── yellow.mp3   # Audio asset for yellow state/trigger
```

---

## Hardware Requirements

* CircuitPython-compatible microcontroller (e.g., Adafruit Feather, RP2040, SAMD51, or ESP32-S2/S3)
* I2S DAC decoder / amplifier (or onboard analog audio output / PWM pin)
* Speaker or 3.5mm audio jack output
* Color/state trigger inputs (buttons, touch pads, or accelerometer)

---

## Installation & Setup

1. **Prepare the Board**: Install the latest stable release of [CircuitPython](https://circuitpython.org/) on your board.
2. **Install Required Libraries**: Copy the necessary libraries (`adafruit_audiomp3`, `audiocore`, `audiopwmio` or `audiobusio`) to the `/lib` folder on your `CIRCUITPY` drive.
3. **Deploy Code & Assets**:
   * Copy `code/code.py` to the root of your `CIRCUITPY` drive[cite: 1].
   * Copy `green.mp3`, `red.mp3`, and `yellow.mp3` to the root directory alongside `code.py`[cite: 1].
4. **Run**: Reset or safely eject and power cycle the board. `code.py` executes automatically on boot[cite: 1].

---

## License

Distributed under the terms of the project [LICENSE](LICENSE)[cite: 1].
