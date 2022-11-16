# ese5190-2022-lab2-2B

## 01_registers

### 1.1 Gif of Toggle the Qt Py's Neopixel LED When the BOOT Button is Pressed

Toggle the Qt Py's Neopixel LED when the BOOT button is pressed, using only direct register reads to access the boot button status. You may use the SDK to initialize the board and the pins, and the WS2812 example code to toggle the Neopixel.

See code [here](https://github.com/sueqixue/ese519-2022-lab2-2B/tree/main/01_registers/Code).

### 1.2 Result

<img src="./01_registers.gif" alt="01" width="600"/>

### 1.3 Notes
```
//------------- LED -------------//
// No normal LED
// #define PICO_DEFAULT_LED_PIN 13

#ifndef PICO_DEFAULT_WS2812_PIN
#define PICO_DEFAULT_WS2812_PIN 12
#endif

#ifndef PICO_DEFAULT_WS2812_POWER_PIN
#define PICO_DEFAULT_WS2812_POWER_PIN 11
#endif
```
