# Euclidean Rhythms Eurorack Module

This is a mockup of an Eurorack Module that will at some point maybe possibly 
be a reality.

Very much in developement and not currently working.

---

## Plan

- RPi Pico board as the controller
- 6 trigger outputs
  - Send trigger signal when event occurs
- Encoder with a push button
  - Push button switches between setting steps and events
- Button to change which track the encoder controls (button in the encoder)
  - LED's to show which track is being manipulated
- LED track that shows the end step, pattern, and current step
  - 16x WS2812 led ring
- Internal clock
- Clock input
- On-Off-On switch for choosing between internal - off - external clock

### TODO

-[] Firmware (split this into smaller todo blocks)
-[] FW: Logic so when the pattern is stopped (switch to mid pos) it starts from 
    beginning when continued
-[] FW: LED logic (split this into smaller todo blocks)
-[] Schematics: Encoder
-[] Schematics: Button to change track (related to encoder)
-[] Schematics: Output circuitry (+5V output triggers of 5ms)
-[] Schematics: LED track circuitry
-[] Schematics: LED selected track circuitry
-[] Does the clock input need a cap to filter voltage spikes?
  - In simulation the voltage does not seem to peak over 3.3V
  - 555 output was spiking a lot, bet when added to the signal generator input
    the waveform was malformed like crazy
  - Need to test this in practice and check it with a scope
-[x] Clock input
-[x] Internal clock

