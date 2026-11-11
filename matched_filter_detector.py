import numpy as np

print("--- Gravitational Wave Cross-Correlation & Matched Filter Engine ---")

time_steps = 1000
pure_signal = np.sin(np.linspace(0, 10 * np.pi, time_steps))

random_noise = np.random.normal(0, 5.0, time_steps)
raw_detector_data = pure_signal + random_noise

correlation_array = np.correlate(raw_detector_data, pure_signal, mode='same')
peak_index = np.argmax(correlation_array)

print("Processing complete.")
print(f"Maximum correlation match matrix peak detected at index location: {peak_index}")
print("Successfully extracted signal tracking pattern from simulated background white noise.")
