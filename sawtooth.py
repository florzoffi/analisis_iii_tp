import numpy as np
from scipy.io.wavfile import write
from scipy import signal

# Parámetros generales de la señal
sample_rate = 44100  # Frecuencia de muestreo en Hz
duration = 5  # Duración en segundos

# Parámetros para la primera señal de onda diente de sierra
frequency_1 = 440  # Frecuencia de la primera señal de onda diente de sierra (Hz)
amplitude_1 = 0.5  # Amplitud de la primera señal de onda diente de sierra

# Parámetros para la segunda señal de onda diente de sierra
frequency_2 = 880  # Frecuencia de la segunda señal de onda diente de sierra (Hz)
amplitude_2 = 0.7  # Amplitud de la segunda señal de onda diente de sierra

# Generar el tiempo
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Generar la primera señal de onda diente de sierra
sawtooth_wave_1 = amplitude_1 * signal.sawtooth(2 * np.pi * frequency_1 * t)

# Generar la segunda señal de onda diente de sierra
sawtooth_wave_2 = amplitude_2 * signal.sawtooth(2 * np.pi * frequency_2 * t)

# Normalizar ambas señales
sawtooth_wave_1_normalized = np.int16(sawtooth_wave_1 / np.max(np.abs(sawtooth_wave_1)) * 32767)
sawtooth_wave_2_normalized = np.int16(sawtooth_wave_2 / np.max(np.abs(sawtooth_wave_2)) * 32767)

# Guardar la primera señal de onda diente de sierra en un archivo .wav
write("sawtooth_wave_1.wav", sample_rate, sawtooth_wave_1_normalized)

# Guardar la segunda señal de onda diente de sierra en otro archivo .wav
write("sawtooth_wave_2.wav", sample_rate, sawtooth_wave_2_normalized)

print("Dos señales de onda diente de sierra diferentes generadas: sawtooth_wave_1.wav y sawtooth_wave_2.wav")