import numpy as np
from scipy.io.wavfile import write

def generate_pink_noise(N, amplitude=0.5):
    """
    Generar una señal de ruido rosa utilizando la técnica de filtrado de ruido blanco.
    """
    # Generar ruido blanco
    white_noise = np.random.normal(0, 1, N)

    # Transformada de Fourier del ruido blanco
    fft_noise = np.fft.rfft(white_noise)

    # Generar el filtro de caída de 1/f (frecuencia)
    freqs = np.fft.rfftfreq(N)
    fft_noise = fft_noise / np.sqrt(freqs + 1e-10)  # Evitar división por cero

    # Transformada inversa para volver al dominio del tiempo
    pink_noise = np.fft.irfft(fft_noise, n=N)

    # Normalizar el ruido rosa a la amplitud deseada
    pink_noise = pink_noise / np.max(np.abs(pink_noise)) * amplitude

    return pink_noise

# Parámetros generales de la señal
sample_rate = 44100  # Frecuencia de muestreo en Hz
duration = 5  # Duración en segundos
N = int(sample_rate * duration)  # Número total de muestras

# Generar la primera señal de ruido rosa
pink_noise_1 = generate_pink_noise(N, amplitude=0.5)

# Generar la segunda señal de ruido rosa
pink_noise_2 = generate_pink_noise(N, amplitude=0.7)

# Normalizar ambas señales
pink_noise_1_normalized = np.int16(pink_noise_1 / np.max(np.abs(pink_noise_1)) * 32767)
pink_noise_2_normalized = np.int16(pink_noise_2 / np.max(np.abs(pink_noise_2)) * 32767)

# Guardar la primera señal de ruido rosa en un archivo .wav
write("pink_noise_1.wav", sample_rate, pink_noise_1_normalized)

# Guardar la segunda señal de ruido rosa en otro archivo .wav
write("pink_noise_2.wav", sample_rate, pink_noise_2_normalized)

print("Dos señales de ruido rosa diferentes generadas: pink_noise_1.wav y pink_noise_2.wav")