import numpy as np
from scipy.io.wavfile import write

# Parámetros generales de la señal
sample_rate = 44100  # Frecuencia de muestreo en Hz
duration = 5  # Duración en segundos
N = int(sample_rate * duration)  # Número total de muestras

# Generar el tiempo
t = np.linspace(0, duration, N, endpoint=False)

# Parámetros para la primera señal multitono (combinación de frecuencias)
frequencies_1 = [440, 880, 1320]  # Frecuencias en Hz (A4, A5, A6)
amplitude_1 = 0.5  # Amplitud de la primera señal multitono

# Generar la primera señal multitono combinando varias señales senoidales
multi_tone_1 = np.zeros(N)
for f in frequencies_1:
    multi_tone_1 += amplitude_1 * np.sin(2 * np.pi * f * t)

# Parámetros para la segunda señal multitono (combinación de frecuencias diferentes)
frequencies_2 = [500, 1000, 1500]  # Frecuencias en Hz
amplitude_2 = 0.7  # Amplitud de la segunda señal multitono

# Generar la segunda señal multitono combinando varias señales senoidales
multi_tone_2 = np.zeros(N)
for f in frequencies_2:
    multi_tone_2 += amplitude_2 * np.sin(2 * np.pi * f * t)

# Normalizar ambas señales
multi_tone_1_normalized = np.int16(multi_tone_1 / np.max(np.abs(multi_tone_1)) * 32767)
multi_tone_2_normalized = np.int16(multi_tone_2 / np.max(np.abs(multi_tone_2)) * 32767)

# Guardar la primera señal multitono en un archivo .wav
write("multi_tone_1.wav", sample_rate, multi_tone_1_normalized)

# Guardar la segunda señal multitono en otro archivo .wav
write("multi_tone_2.wav", sample_rate, multi_tone_2_normalized)

print("Dos señales multitono generadas: multi_tone_1.wav y multi_tone_2.wav")