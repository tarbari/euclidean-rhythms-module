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
  - Digital encoder, changes BPM
- Clock input
- On-Off-On switch for choosing between internal - off - external clock

### TODO

- Cap to filter the clock input
  - In simulation the voltage does not seem to peak over 3.3V

