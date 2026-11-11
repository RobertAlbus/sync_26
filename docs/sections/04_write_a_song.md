# 04: Write a Song

## 073_sync_conference 16 bar composition

- slide 1: title, no animation
- slide 2: notes on a piano roll
    - create a 2 octave piano roll over 2 bars with 2 different notes/lengths but they do not overlap in time
    - show an empty table of data with start time, duration, note
    - wait for me to progress
    - animate the start time as an arrow correlation of the first note's beginning to the beat/bar marker, the duration as a double ended horizontal arrow, and the pitch as a double ended vertical arrow
    - wait for me to progress
    - show the numerical value for the start time in beats, the numerical value for the duration in beats, the note with some arbitrary octave like F# 4. these numerical values should be next to the indicators and notes right on the timeline
    - wait for me to progress
    - animate the numerical values moving into the table
    - wait for me to progress
    - fade in a second identical table that is empty and in the same animation take the data from the second note and move it into the second table

## Pattern construction

- 4/4 kick and pattern algebra
    - construct 1 bar, tile 16 bars, trim_between
- chords
    - construct 2 bars, A and B version, tile
- chord automation clip
    - rise from bar 0 to 8, then loop 8-16
- bassline
    - lightweight stochastic search example, tile, trim
