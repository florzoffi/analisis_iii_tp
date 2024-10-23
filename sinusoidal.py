import numpy as np
from scipy.io.wavfile import write

# Parámetros generales de la señal
sample_rate = 44100  # Frecuencia de muestreo en Hz
duration = 5  # Duración en segundos

# Parámetros para la primera señal senoidal
frequency_1 = 440  # Frecuencia de la primera señal senoidal (Hz)
amplitude_1 = 0.5  # Amplitud de la primera señal senoidal

# Parámetros para la segunda señal senoidal
frequency_2 = 880  # Frecuencia de la segunda señal senoidal (Hz)
amplitude_2 = 0.7  # Amplitud de la segunda señal senoidal

# Generar el tiempo
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Generar la primera señal senoidal
sine_wave_1 = amplitude_1 * np.sin(2 * np.pi * frequency_1 * t)

# Generar la segunda señal senoidal
sine_wave_2 = amplitude_2 * np.sin(2 * np.pi * frequency_2 * t)

# Normalizar ambas señales
sine_wave_1_normalized = np.int16(sine_wave_1 / np.max(np.abs(sine_wave_1)) * 32767)
sine_wave_2_normalized = np.int16(sine_wave_2 / np.max(np.abs(sine_wave_2)) * 32767)

# Guardar la primera señal senoidal en un archivo .wav
write("sine_wave_1.wav", sample_rate, sine_wave_1_normalized)

# Guardar la segunda señal senoidal en otro archivo .wav
write("sine_wave_2.wav", sample_rate, sine_wave_2_normalized)

print("Dos señales senoidales diferentes generadas: sine_wave_1.wav y sine_wave_2.wav")