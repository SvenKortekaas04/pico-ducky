# pico-ducky
Run Ducky Scripts on a Raspberry Pi Pico.

## Installation

1. Download [CircuitPython](https://circuitpython.org/board/raspberry_pi_pico/).
2. Plug the Raspberry Pi Pico in a USB port while holding down the boot button. The Raspberry Pi Pico will show up as a storage device named `RPI-RP2`.
3. Place the .uf2 file, downloaded in step 1, in the root of the Raspberry Pi Pico. The device will reboot and reconnect as `CIRCUITPY`.
4. For a Ducky Script to run on a Raspberry Pi Pico using CircuitPython, a specific library needs to be installed. The Adafruit CircuitPython Library Bundle can be downloaded [here](https://circuitpython.org/libraries). Make sure the bundle version matches up with the version of CircuitPython you are running.
5. Extract the ZIP-folder and navigate to the lib folder. Copy `adafruit_hid` to the lib folder on the Raspberry Pi Pico.
6. Next, download this Github repository as a ZIP-folder, extract it and copy the `main.py` file to the root folder of your Raspberry Pi Pico.
7. Find a Ducky Script and save it as `payload.txt` on the Raspberry Pi Pico.
8. To execute a Ducky Script, plug the Raspberry Pi Pico in a USB port. Be careful, if the Raspberry Pi Pico is not in setup mode, the device will reboot and after one second the Ducky Script will be executed.
