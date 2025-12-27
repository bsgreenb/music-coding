"""
Audio utilities for waveform generation and playback.
"""

import numpy as np
from IPython.display import Audio, display

# --- AUDIO CONSTANTS ---

# Standard CD-quality sample rate
SAMPLE_RATE_HZ = 44100

# Frequency reference (A4 = 440 Hz is the standard tuning pitch)
A4_FREQUENCY_HZ = 440

# MIDI conversion constants
A4_MIDI_NUMBER = 69
NOTES_PER_OCTAVE = 12


# --- WAVEFORM GENERATION ---

def generate_sine_wave(frequency_hz, duration_seconds, amplitude=1.0):
    """
    Generate a pure sine wave at the given frequency.
    
    Args:
        frequency_hz: Frequency in Hz (e.g., 440 for A4)
        duration_seconds: Length of the audio in seconds
        amplitude: Peak amplitude (0.0 to 1.0)
    
    Returns:
        Tuple of (time_array, waveform_array)
    """
    num_samples = int(SAMPLE_RATE_HZ * duration_seconds)
    t = np.linspace(0, duration_seconds, num_samples, endpoint=False)
    waveform = amplitude * np.sin(2 * np.pi * frequency_hz * t)
    return t, waveform


def generate_white_noise(duration_seconds, amplitude=1.0):
    """
    Generate white noise (random samples).
    
    Args:
        duration_seconds: Length of the audio in seconds
        amplitude: Peak amplitude (0.0 to 1.0)
    
    Returns:
        Tuple of (time_array, waveform_array)
    """
    num_samples = int(SAMPLE_RATE_HZ * duration_seconds)
    t = np.linspace(0, duration_seconds, num_samples, endpoint=False)
    # Random values between -1 and 1, scaled by amplitude
    waveform = amplitude * (2 * np.random.random(num_samples) - 1)
    return t, waveform


# --- AUDIO PLAYBACK ---

def play_audio(waveform, autoplay=True):
    """
    Play a waveform as audio in a Jupyter notebook.
    
    Args:
        waveform: NumPy array of audio samples (-1.0 to 1.0)
        autoplay: Whether to start playing immediately
    
    Returns:
        IPython Audio widget
    """
    audio = Audio(waveform, rate=SAMPLE_RATE_HZ, autoplay=autoplay)
    display(audio)
    return audio


# --- FREQUENCY CONVERSION ---

def hz_to_midi(freq):
    """Convert frequency (Hz) to MIDI note number. A4 (440 Hz) = 69."""
    import math
    return A4_MIDI_NUMBER + NOTES_PER_OCTAVE * math.log2(freq / A4_FREQUENCY_HZ)


def midi_to_hz(midi_note):
    """Convert MIDI note number to frequency (Hz). MIDI 69 = 440 Hz."""
    return A4_FREQUENCY_HZ * (2 ** ((midi_note - A4_MIDI_NUMBER) / NOTES_PER_OCTAVE))

