import numpy as np
from scipy.io.wavfile import write

# Parámetros generales de la señal
sample_rate = 44100  # Frecuencia de muestreo en Hz
duration = 5  # Duración en segundos
N = int(sample_rate * duration)  # Número total de muestras

# Generar el tiempo
t = np.linspace(0, duration, N, endpoint=False)

# Parámetros para la primera señal de pulsos
pulse_frequency_1 = 2  # Frecuencia de repetición de pulsos (Hz)
pulse_duration_1 = 0.01  # Duración de cada pulso (en segundos)
amplitude_1 = 1.0  # Amplitud de la primera señal de pulsos

# Generar la primera señal de pulsos
pulse_signal_1 = np.zeros(N)
pulse_period_1 = int(sample_rate / pulse_frequency_1)  # Número de muestras entre pulsos
pulse_samples_1 = int(pulse_duration_1 * sample_rate)  # Duración del pulso en muestras

for i in range(0, N, pulse_period_1):
    pulse_signal_1[i:i + pulse_samples_1] = amplitude_1

# Parámetros para la segunda señal de pulsos
pulse_frequency_2 = 5  # Frecuencia de repetición de pulsos (Hz)
pulse_duration_2 = 0.02  # Duración de cada pulso (en segundos)
amplitude_2 = 0.8  # Amplitud de la segunda señal de pulsos

# Generar la segunda señal de pulsos
pulse_signal_2 = np.zeros(N)
pulse_period_2 = int(sample_rate / pulse_frequency_2)  # Número de muestras entre pulsos
pulse_samples_2 = int(pulse_duration_2 * sample_rate)  # Duración del pulso en muestras

for i in range(0, N, pulse_period_2):
    pulse_signal_2[i:i + pulse_samples_2] = amplitude_2

# Normalizar ambas señales
pulse_signal_1_normalized = np.int16(pulse_signal_1 / np.max(np.abs(pulse_signal_1)) * 32767)
pulse_signal_2_normalized = np.int16(pulse_signal_2 / np.max(np.abs(pulse_signal_2)) * 32767)

# Guardar la primera señal de pulsos en un archivo .wav
write("pulse_signal_1.wav", sample_rate, pulse_signal_1_normalized)

# Guardar la segunda señal de pulsos en otro archivo .wav
write("pulse_signal_2.wav", sample_rate, pulse_signal_2_normalized)

print("Dos señales de pulsos generadas: pulse_signal_1.wav y pulse_signal_2.wav")