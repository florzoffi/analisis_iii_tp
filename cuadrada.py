import numpy as np
from scipy.io.wavfile import write
from scipy import signal

# Parámetros de la señal
sample_rate = 44100  # Frecuencia de muestreo en Hz
duration = 5  # Duración en segundos
frequency_1 = 440  # Frecuencia de la primera señal cuadrada (Hz)
frequency_2 = 880  # Frecuencia de la segunda señal cuadrada (Hz)

# Generar el tiempo
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Generar la primera señal cuadrada
square_wave_1 = signal.square(2 * np.pi * frequency_1 * t)

# Generar la segunda señal cuadrada
square_wave_2 = signal.square(2 * np.pi * frequency_2 * t)

# Normalizar ambas señales
square_wave_1_normalized = np.int16(square_wave_1 / np.max(np.abs(square_wave_1)) * 32767)
square_wave_2_normalized = np.int16(square_wave_2 / np.max(np.abs(square_wave_2)) * 32767)

# Guardar la primera señal cuadrada en un archivo .wav
write("square_wave_1.wav", sample_rate, square_wave_1_normalized)

# Guardar la segunda señal cuadrada en otro archivo .wav
write("square_wave_2.wav", sample_rate, square_wave_2_normalized)

print("Señal cuadrada 1 guardada como square_wave_1.wav")
print("Señal cuadrada 2 guardada como square_wave_2.wav")