// Simple sine wave
{
    var freq = 440;
    SinOsc.ar(freq, 0, 0.1)
}.play;

// Pattern example
Pbind(
    \instrument, \default,
    \degree, Pseq([0, 2, 4, 5, 7], inf),
    \dur, 0.25
).play;