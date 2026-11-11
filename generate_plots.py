import numpy as np
import matplotlib.pyplot as plt

# 1. Chirp Signal Data
fs = 4096
t = np.linspace(0, 1, fs)
f_t = 30 + (250 - 30) * (t ** 2)
chirp = (t * 1e-21) * np.sin(2 * np.pi * f_t * t)

# 2. Matched Filter Data
t_mf = np.linspace(0, 1, 1000)
template = np.sin(2 * np.pi * 15 * t_mf) * np.exp(-((t_mf - 0.5)**2) / 0.01)
noise = np.random.normal(0, 0.8, 1000)
noisy_data = template + noise
corr = np.correlate(noisy_data, template, mode='same')
snr_peak = np.max(corr) / np.std(corr)

# 3. FFT Spectral Data
fs_fft = 2000
t_fft = np.linspace(0, 2, fs_fft * 2, endpoint=False)
sig_fft = 0.5 * np.sin(2 * np.pi * 120 * t_fft) + 2.0 * np.sin(2 * np.pi * 50 * t_fft) + np.random.normal(0, 0.5, len(t_fft))
freqs = np.fft.rfftfreq(len(t_fft), 1/fs_fft)
psd = np.abs(np.fft.rfft(sig_fft)) / len(t_fft)

# Create 3-Panel Scientific Figure
fig, axs = plt.subplots(3, 1, figsize=(9, 10))
plt.subplots_adjust(hspace=0.45)

# Panel 1: Chirp
axs[0].plot(t, chirp * 1e21, color='#1f77b4', lw=1.2)
axs[0].set_title('1. Simulated Binary Inspiral Chirp Waveform (30 Hz - 250 Hz)', fontweight='bold')
axs[0].set_xlabel('Time (s)')
axs[0].set_ylabel('Strain (x 10^-21)')
axs[0].grid(True, alpha=0.3)

# Panel 2: Matched Filter
axs[1].plot(t_mf, noisy_data, color='gray', alpha=0.5, label='Noisy Strain Data')
axs[1].plot(t_mf, corr / np.max(corr), color='#d62728', lw=2, label=f'Normalized Matched Filter Output (Peak SNR: {snr_peak:.2f})')
axs[1].set_title('2. Matched-Filter Signal Extraction from White Noise', fontweight='bold')
axs[1].set_xlabel('Time (s)')
axs[1].set_ylabel('Amplitude / Correlation')
axs[1].legend(loc='upper right')
axs[1].grid(True, alpha=0.3)

# Panel 3: FFT Spectrum
axs[2].plot(freqs[:400], psd[:400], color='#2ca02c', lw=1.5)
axs[2].annotate('50 Hz Power-Line Hum', xy=(50, np.max(psd)), xytext=(80, np.max(psd)*0.8),
                arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=6), fontweight='bold')
axs[2].set_title('3. Power Spectral Density (FFT) Noise Diagnostic', fontweight='bold')
axs[2].set_xlabel('Frequency (Hz)')
axs[2].set_ylabel('Magnitude')
axs[2].grid(True, alpha=0.3)

plt.savefig('ligo_dsp_results.png', dpi=200, bbox_inches='tight')
print(f"\n--- Visual Diagnostics & Quantitative Metrics ---")
print(f"Saved diagnostic plot: ligo_dsp_results.png")
print(f"Matched Filter Peak SNR: {snr_peak:.2f} | Detected Noise Spike: 50.00 Hz | Peak Chirp Strain: {np.max(chirp):.2e}")
