
import numpy as np
import matplotlib.pyplot as plt


def generate_grating(l: int, N: int=1024, linsize: float=0.001,
                     wavelength: float=700 * 1e-9, a: float=0, b: float=0.02):
    """Генерация fork-решетки

    Args:
        l (int): закрученность
        N (int): число точек на каждую ось
        linsize (float): размер решетки (м)
        wavelength (float): длина волны (м)
        a (float): наклон плоской волны по x (рад.)
        b (float): наклон плоской волны по y (рад.)
    
    """
 

    x = np.linspace(-linsize/2, linsize/2, N, endpoint=True, dtype=float)
    y = np.linspace(-linsize/2, linsize/2, N, endpoint=True, dtype=float)
  
    mesh_x, mesh_y = np.meshgrid(x, y)
    
    oam_wave = np.exp(1j * l * np.arctan2(mesh_y, mesh_x))
    
    tilted_plane_wave = np.exp(-1j * (2 * np.pi / wavelength * np.sin(a) * mesh_x + 
                                      2 * np.pi / wavelength * np.sin(b) * mesh_y))

    interference_pattern = tilted_plane_wave + oam_wave
    
    intensity_pattern = np.abs(interference_pattern) ** 2

    #phase_pattern = np.angle(interference_pattern)
    grating = np.zeros((N, N), dtype=float)
    for n in range(0, N):
        for m in range(0,N):
            grating[n, m] = 1 if intensity_pattern[n, m] > 2 else 0

    return grating, intensity_pattern

if __name__ == "__main__":
    grating, intensity = generate_grating(1)
    f1 = plt.figure(1)
    plt.imshow(grating, cmap='grey')
    plt.colorbar()


    f2 = plt.figure(2)
    plt.imshow(intensity, cmap='grey')
    plt.colorbar()
    plt.show()