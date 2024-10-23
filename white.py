import numpy as np
from scipy.io.wavfile import write

# Parámetros generales de la señal
sample_rate = 44100  # Frecuencia de muestreo en Hz
duration = 5  # Duración en segundos
N = int(sample_rate * duration)  # Número total de muestras

# Generar la primera señal de ruido blanco
white_noise_1 = np.random.normal(0, 0.5, N)  # Media 0, desviación estándar 0.5

# Generar la segunda señal de ruido blanco
white_noise_2 = np.random.normal(0, 0.7, N)  # Media 0, desviación estándar 0.7

# Normalizar ambas señales
white_noise_1_normalized = np.int16(white_noise_1 / np.max(np.abs(white_noise_1)) * 32767)
white_noise_2_normalized = np.int16(white_noise_2 / np.max(np.abs(white_noise_2)) * 32767)

# Guardar la primera señal de ruido blanco en un archivo .wav
write("white_noise_1.wav", sample_rate, white_noise_1_normalized)

# Guardar la segunda señal de ruido blanco en otro archivo .wav
write("white_noise_2.wav", sample_rate, white_noise_2_normalized)

print("Dos señales de ruido blanco diferentes generadas: white_noise_1.wav y white_noise_2.wav")