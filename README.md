# ese519-2022-lab2-2B

## Outline
Question | State
:---: | :---:
01_registers | √
02_repl | √
03_sequencer | √
04_slow_motion | √
05_i2c_traffic | √
06_pioscope | √
07_pio_sequencer | *in-progress*
08_adps_protocol | not-started
09_lab_on_a_chip | not-started
10_protoboard | √
EC_analog_knob | not-started
EC_ansi_escapes | not-started
EC_asm_registers | not-started
EC_dma_i2c | not-started
EC_hardware_i2c | not-started
EC_interrupt_i2c | not-started
EC_lovr_viz | not-started
EC_pwm_scope | not-started
EC_socket_server | not-started
EC_speaker | not-started

## Lab Feedback Questions
- Which parts of the lab specification have you found most confusing or difficult to understand? Be specific, and quote any parts of the lab description relevant to your answer (e.g., "modify the PIO/DMA logic analyzer example to record a timestamped trace of an RP2040-ADPS9960 exchange while the BOOT button is pressed.") I will make particular notice of anything that seems underspecified (e.g., words whose meaning is not clear from context, or conflicting interpretations of a deliverable).
	- Part 08 and 09 are confusing. The description is not clear about what we need to implement and which code we should check for hints. I actually didn't know where to start untill I saw the submission of part 08 and 09 of Dang0v. I read their submission and their code really helped me.

- Which lab topics have you found most confusing or difficult to understand? E.g., "serial communication with Python," "aliased bitwise operations," "programming the PIO," etc. Be specific, and describe any lingering areas of confusion and/or anything that has helped you navigate them.
	- Bitwise operations is fine. The serial communication with Python confused me at first. For part 03, I first didn't know how to control the sequencer on my PC. I knew little about the communications between board and my device and my teammmate Junpeng helped me a lot about that. Programming the PIO is OK, since it was new for all of use, so we just needed to read the documents and examples to learn more about that. Besides, I didn't work with much hardware before sicne I did computer science for my undergrad, my teammates helped me and taught me a lot when I built my protoboard. 

- Which parts of the lab have you found most difficult to implement? Again, be specific, citing any parts of the lab materials & your own code that are relevant to your answer.
	- Part 07 was the part the most difficult to implement. As I mentioned above, me and my teammates didn't knwo where to start at first. 

- What steps have you taken to resolve these difficulties? Any other barriers you have faced to completing this assignment? Mention any students, repos, or other resources you have found helpful in completing the lab so far.
	- My teammates and I worked spent a lot of time in K-lab for this assigment. We discuss the questions and solutions with some other hardwroking students who also chose to be in K-lab to work on lab2. The submission of Dang0v and their teammates really help us to undertand what we should do for part 07, 08, and 09.