import numpy as np
from scipy.io.wavfile import write

# Parámetros de la señal
sample_rate = 44100  # Frecuencia de muestreo en Hz
duration = 5  # Duración en segundos

# Parámetros para la primera señal sinesweep
f_start_1 = 20  # Frecuencia inicial del primer sinesweep (Hz)
f_end_1 = 20000  # Frecuencia final del primer sinesweep (Hz)

# Parámetros para la segunda señal sinesweep
f_start_2 = 50  # Frecuencia inicial del segundo sinesweep (Hz)
f_end_2 = 15000  # Frecuencia final del segundo sinesweep (Hz)

# Generar el tiempo
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Generar el primer sinesweep
sweep_signal_1 = np.sin(2 * np.pi * (f_start_1 + (f_end_1 - f_start_1) * t / duration) * t)

# Generar el segundo sinesweep
sweep_signal_2 = np.sin(2 * np.pi * (f_start_2 + (f_end_2 - f_start_2) * t / duration) * t)

# Normalizar ambas señales
sweep_signal_1_normalized = np.int16(sweep_signal_1 / np.max(np.abs(sweep_signal_1)) * 32767)
sweep_signal_2_normalized = np.int16(sweep_signal_2 / np.max(np.abs(sweep_signal_2)) * 32767)

# Guardar la primera señal sinesweep en un archivo .wav
write("sinesweep_1.wav", sample_rate, sweep_signal_1_normalized)

# Guardar la segunda señal sinesweep en otro archivo .wav
write("sinesweep_2.wav", sample_rate, sweep_signal_2_normalized)

print("Dos señales sinesweep diferentes generadas: sinesweep_1.wav y sinesweep_2.wav")