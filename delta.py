import numpy as np
from scipy.io.wavfile import write

# Parámetros generales de la señal
sample_rate = 44100  # Frecuencia de muestreo en Hz
duration = 5  # Duración en segundos
N = int(sample_rate * duration)  # Número total de muestras

# Generar la primera señal de impulso (Delta de Dirac)
impulse_position_1 = 10000  # Posición del impulso en muestras
impulse_amplitude_1 = 1.0  # Amplitud del primer impulso
impulse_1 = np.zeros(N)  # Crear una señal de ceros
impulse_1[impulse_position_1] = impulse_amplitude_1  # Poner el impulso en la posición definida

# Generar la segunda señal de impulso (Delta de Dirac)
impulse_position_2 = 30000  # Posición del impulso en muestras
impulse_amplitude_2 = 0.8  # Amplitud del segundo impulso
impulse_2 = np.zeros(N)  # Crear una señal de ceros
impulse_2[impulse_position_2] = impulse_amplitude_2  # Poner el impulso en la posición definida

# Normalizar ambas señales (opcional, ya que la amplitud ya está bien ajustada)
impulse_1_normalized = np.int16(impulse_1 / np.max(np.abs(impulse_1)) * 32767)
impulse_2_normalized = np.int16(impulse_2 / np.max(np.abs(impulse_2)) * 32767)

# Guardar la primera señal de impulso en un archivo .wav
write("impulse_1.wav", sample_rate, impulse_1_normalized)

# Guardar la segunda señal de impulso en otro archivo .wav
write("impulse_2.wav", sample_rate, impulse_2_normalized)

print("Dos señales de impulso (Delta de Dirac) generadas: impulse_1.wav y impulse_2.wav")