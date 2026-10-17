# OUTLINE: Making Electronic Music With Code From First Principles in C++

* 01: [slides] intro
    * bio
        * Rob, music producer and computer programmer
        * I make music using C++ programming
        * I am fully self-taught
    * quick overview of presentation
    * goals for this talk
* 02: my practice
    * [slide] compositional, not live. compare production vs. live performance
    * [demo]: 067_dj_tool
    * [slide] the composition is expressed in code. the live ui is a helpful tool but not the authority.
    * [demo+slides] composition 16 bars (needs to be constructed)
        * 4/4 kick and algebra constructed (1 bar, tile 16 bars, trim_between)
        * chords (construct 2 bars A and B version, tile)
        * automation clip for chords (rise from bar 0 to 8, then loop for 8-16)
        * bassline (light weight stochastic search example, tile, trim)
* 03: [slides] engine technical deep dive (succinct)
    * engine
        * digital audio primer
        * digital audio => engine example (repeatedly shovel audio into buffer)
    * dsp primitives => instruments
        * what "primitives" refers to (oscs, filters, delays, envelopes)
        * simple oscillator explanation (osc.next() + plot)
        * combining primitives into instruments (diagram of my subtractive synth)
    * sequencing
        * controls pitch, on/off, etc. over time
    * unifying diagram animation
* 04: [slides] why I like to work this way
* 05: live noise performance system (optional time permitting)
    * [slide] fdn diagram
    * [demo]
* 06: [slide] conclusion
