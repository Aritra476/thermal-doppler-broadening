
import numpy as np
import matplotlib.pyplot as plt

k_B = 1.380649e-23      # Boltzmann constant (J/K)
c = 3.0e8               # speed of light (m/s)
m_H = 1.67e-27          # mass of hydrogen atom (kg)
h = 6.626e-34           # Planck constant (J s)

# Rest frequency of spectral line
nu0 = 5e24   # Hz

# Photon energy corresponding to this frequency
E = h * nu0

print("Photon energy:", E, "J")

N_atoms = 10000      # number of atoms in the gas

# Temperatures to test
temperatures = [3000, 60000, 1000000]

# ---------------------------------------------
# 4. Loop over different temperatures
# ---------------------------------------------

plt.figure(figsize=(10,6))

for T in temperatures:

    # Standard deviation of velocity distribution
    sigma_v = np.sqrt(k_B * T / m_H)

    # Generate random velocities (line-of-sight component)
    velocities = np.random.normal(0, sigma_v, N_atoms)

    # Doppler formula:
    # ν = ν0 (1 + v/c)

    shifted_freq = nu0 * (1 + velocities / c)

    plt.hist(
        shifted_freq,
        bins=15,
        alpha=0.5,
        label=f"T = {T} K",
        density=True
    )

plt.xlabel("Photon Frequency (Hz)")
plt.ylabel("Normalized Intensity")
plt.title("Thermal Doppler Broadening of Spectral Lines")
plt.legend()
plt.grid()
plt.show()