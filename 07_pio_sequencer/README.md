# 07_pio_sequencer

## 7.1 Pio Sequencer

- Modify your sequencer to use the PIO as its primary I/O engine, including the ability to R/W any register.

## 7.2 Result


## 7.3 Notes
- [x] Modify the sequencer to use the PIO as primary I/O engine:

	- According to the datasheet, the PIO is not suitable for button use, we decided to add PIO-I2C in the sequencer for the I2C device use such as APDS9960.

	- The interface from PC side is:
        `i <address> <read length>`
        `o <address> <write value>`

- [x] The ability to R/W any register:

    | functions |command |
    | :--| :--  |
    | record  |`# <seconds>  <frequency(op)>`|
    | replay | `$ <filename> <frequency(op)>`|
    | read address|`r <address(8bits)>`|
    | write address|`w <address(8bits)> <value>`|
    |Input gpio|`< <Pin>`|
    |Output gpio|`> <Pin>` |
    |I2C read|`i <address uint8_t> <read length>`|
    |I2C write|`o <address> <write value>`|
