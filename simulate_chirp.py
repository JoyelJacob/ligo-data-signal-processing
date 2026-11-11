import numpy as np

print("--- Simulating a Gravitational Wave 'Chirp' Signal ---")

sampling_rate = 4096
t = np.linspace(0, 1, sampling_rate)

start_freq = 30
end_freq = 250
f_t = start_freq + (end_freq - start_freq) * (t ** 2)

amplitude = t * 1e-21 
chirp_signal = amplitude * np.sin(2 * np.pi * f_t * t)

print(f"Generated time-series matrix array with {len(chirp_signal)} data points.")
print(f"Starting frequency: {start_freq} Hz -> Peak frequency at merger: {end_freq} Hz")
print("Signal simulation execution successful.")
