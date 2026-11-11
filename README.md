# Gravitational-Wave Signal Processing (Data & Noise)

A collection of Python scripts exploring time-series strain data, signal extraction, and noise analysis using open datasets from the LIGO Open Science Center (GWOSC).

## Overview
Gravitational-wave detectors capture faint cosmic signals buried inside heavy environmental and instrumental noise. This project implements core signal-processing techniques to fetch real event metadata, model binary merger waveforms, isolate buried signals, and diagnose narrow-band instrumentation noise.

## Subsystems & Scripts
* `ligo_analysis.py` – Queries the GWOSC public API v2 to retrieve calibrated event metadata (GPS merger time, active detectors, and catalog DOI) for GW150914.
* `simulate_chirp.py` – Generates a synthetic 4096 Hz time-series waveform modeling the accelerating frequency sweep ("chirp") of an inspiraling binary black hole merger (30 Hz to 250 Hz).
* `matched_filter_detector.py` – Uses time-domain cross-correlation (matched filtering) to locate a known waveform template hidden inside heavy Gaussian white noise.
* `fft_noise_spectral_analysis.py` – Applies a Fast Fourier Transform (FFT) to convert time-domain sensor data into a Power Spectral Density (PSD) spectrum to isolate narrow-band interference.
* `generate_plots.py` – Produces multi-panel visual diagnostics and logs quantitative metrics to [`results.txt`](./results.txt).

## Key Results & Diagnostic Takeaways
1. **Live Metadata Retrieval:** Confirmed automated API access to `GW150914-v3` (GPS time `1126259462.4` across detectors `H1` and `L1`).
2. **Waveform Modeling (Panel 1):** Simulated a 1-second inspiral chirp reaching a peak strain amplitude of `9.80e-22`, demonstrating how theoretical templates are constructed prior to matched-filter searches.
3. **Signal Extraction (Panel 2):** Recovered a buried signal from white noise with a clear matched-filter **Peak SNR of 3.30**, illustrating how cross-correlation isolates faint astrophysical events from static.
4. **Spectral Noise Diagnostics (Panel 3):** Isolated an artificial **`50.00 Hz` power-line hum** in the frequency domain, demonstrating how FFT diagnostics pinpoint terrestrial interference for targeted notch filtering.

## Requirements & Usage
```bash
pip install numpy matplotlib
python generate_plots.py
```

## Visual Diagnostics
![LIGO Signal Processing Results](./ligo_dsp_results.png)
