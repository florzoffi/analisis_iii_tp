import numpy as np
from scipy.io.wavfile import write

# Parámetros generales de la señal
sample_rate = 44100  # Frecuencia de muestreo en Hz
duration = 5  # Duración en segundos
N = int(sample_rate * duration)  # Número total de muestras

# Generar la primera señal de escalón
step_position_1 = 10000  # Posición donde ocurre el escalón en muestras
step_amplitude_1 = 1.0  # Amplitud del primer escalón
step_1 = np.zeros(N)  # Crear una señal de ceros
step_1[step_position_1:] = step_amplitude_1  # A partir de la posición, la señal toma el valor de amplitud

# Generar la segunda señal de escalón
step_position_2 = 30000  # Posición donde ocurre el escalón en muestras
step_amplitude_2 = 0.8  # Amplitud del segundo escalón
step_2 = np.zeros(N)  # Crear una señal de ceros
step_2[step_position_2:] = step_amplitude_2  # A partir de la posición, la señal toma el valor de amplitud

# Normalizar ambas señales (opcional, ya que la amplitud ya está bien ajustada)
step_1_normalized = np.int16(step_1 / np.max(np.abs(step_1)) * 32767)
step_2_normalized = np.int16(step_2 / np.max(np.abs(step_2)) * 32767)

# Guardar la primera señal de escalón en un archivo .wav
write("step_wave_1.wav", sample_rate, step_1_normalized)

# Guardar la segunda señal de escalón en otro archivo .wav
write("step_wave_2.wav", sample_rate, step_2_normalized)

print("Dos señales de escalón generadas: step_wave_1.wav y step_wave_2.wav")