import pyaudio
import numpy as np

def generate_sine_wave(frequency, duration, sampling_rate=44100):
    # Generate time values from 0 to duration seconds
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

    # Generate a sine wave signal
    sine_wave = 0.5 * np.sin(2 * np.pi * frequency * t)

    return sine_wave

def play_sound(signal, sampling_rate=44100):
    p = pyaudio.PyAudio()

    # Open a stream with the specified sampling rate
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=sampling_rate,
                    output=True)

    # Play the signal
    stream.write(signal.astype(np.float32).tobytes())

    # Close the stream and PyAudio
    stream.stop_stream()
    stream.close()
    p.terminate()

def play_morse_sound(morse_code: str, Speed:int=2, Pitch:int=2):

    Speed =  (10 - int(Speed)) * 0.1

    Pitch = (int(Pitch) * 0.1) * 500
    print(Pitch)

    for m in morse_code:
        if m == '.':
            frequency = 300 + Pitch
            duration = 0.1 * Speed
            sine_wave = generate_sine_wave(frequency, duration)
            play_sound(sine_wave)
        elif m == '-':
            frequency = 300 + Pitch
            duration = 0.3 * Speed
            sine_wave = generate_sine_wave(frequency, duration)
            play_sound(sine_wave)
        elif m == ' ':
            frequency = 300 + Pitch
            duration = 0.1 * Speed
            sine_wave = generate_sine_wave(frequency, duration)
            play_sound(sine_wave)
        else:
            continue