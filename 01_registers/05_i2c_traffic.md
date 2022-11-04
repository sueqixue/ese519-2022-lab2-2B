# ese5190-2022-lab2-2B

## 01_registers

### 1.1 Gif of Toggle the Qt Py's Neopixel LED When the BOOT Button is Pressed

<img src="./01_registers.gif" alt="01" width="600"/>

### 1.2 Notes
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
