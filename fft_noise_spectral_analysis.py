import numpy as np

print("--- Fast Fourier Transform (FFT) Frequency Analysis Engine ---")

sampling_frequency = 2000
total_time = 2.0
t = np.linspace(0, total_time, int(sampling_frequency * total_time), endpoint=False)

power_line_hum = np.sin(2 * np.pi * 50 * t)

fft_matrix_output = np.fft.fft(power_line_hum)
frequencies = np.fft.fftfreq(len(t), 1/sampling_frequency)

positive_frequencies = frequencies[:len(frequencies)//2]
magnitude_spectrum = np.abs(fft_matrix_output[:len(fft_matrix_output)//2])
dominant_noise_frequency = positive_frequencies[np.argmax(magnitude_spectrum)]

print(f"Spectral analysis complete. Isolated structural noise peak at: {dominant_noise_frequency:.2f} Hz")
print("Frequency domain mapping executed successfully.")
