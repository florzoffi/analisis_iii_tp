import numpy as np
from scipy.io.wavfile import write

# Parámetros generales de la señal
sample_rate = 44100  # Frecuencia de muestreo en Hz
duration = 5  # Duración en segundos
N = int(sample_rate * duration)  # Número total de muestras

# Generar el tiempo
t = np.linspace(0, duration, N, endpoint=False)

# Generar la primera señal exponencial (creciente)
tau_1 = 1.0  # Constante de tiempo para la primera exponencial
amplitude_1 = 0.5  # Amplitud de la primera señal exponencial
exp_signal_1 = amplitude_1 * np.exp(t / tau_1)  # Señal exponencial creciente

# Generar la segunda señal exponencial (decreciente)
tau_2 = 0.5  # Constante de tiempo para la segunda exponencial
amplitude_2 = 1.0  # Amplitud de la segunda señal exponencial
exp_signal_2 = amplitude_2 * np.exp(-t / tau_2)  # Señal exponencial decreciente

# Normalizar ambas señales
exp_signal_1_normalized = np.int16(exp_signal_1 / np.max(np.abs(exp_signal_1)) * 32767)
exp_signal_2_normalized = np.int16(exp_signal_2 / np.max(np.abs(exp_signal_2)) * 32767)

# Guardar la primera señal exponencial en un archivo .wav
write("exp_signal_1.wav", sample_rate, exp_signal_1_normalized)

# Guardar la segunda señal exponencial en otro archivo .wav
write("exp_signal_2.wav", sample_rate, exp_signal_2_normalized)

print("Dos señales exponenciales generadas: exp_signal_1.wav y exp_signal_2.wav")