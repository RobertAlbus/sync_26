# OUTLINE: Making Electronic Music With Code From First Principles in C++

* 01: intro
    * bio
    * quick overview of presentation
        * landscape survey: generative art, live coding, etc.
        * explain my practice
        * what is an audio engine? (technical deep dive)
        * 
    * goals for this talk
* 02: code-music landscape
    * live coding: strudel, supercollider
        * slide
        * couple of video clips
    * DSP: vst plugings, visual programming, supercollider
        * slide
        * couple of video clips
    * Generative art
        * Symbolic algorithmic composition, stochastic composition 
            * video clip of music.py
        * Vera Molnar and/or other example(s) (a visual example of this kind of approach)
* 03: my practice
    * DEFINE MY PRACTICE
        * not live; compositional. compare production vs. live performance
        * succinct summary: engine, primitives => instruments, sequencing. all in code. live ui for tweaking patches.
    * unifying diagram
    * engine
        * digital audio primer
        * digital audio => engine example (repeatedly shovel audio into)
    * dsp primitives => instruments
        * what "primitives" refers to (oscs, filters, delays, envelopes)
        * simple oscillator explanation (osc.next() + plot)
        * combining primitives into instruments
        * diagram of my subtractive synth
        * live example of my subtractive synth
        * code example for the patch
    * sequencing
        * define: do this musical task at this time
        * piano roll screenshot
        * example from my code
        * overlay pictoral explanation of pattern algebra
        * live example of notes in timeline, automation clips
    * unifying diagram
* 04: live noise performance system 
    * fdn diagram
    * demo
* 05: practical advice
* 06: conclusion
