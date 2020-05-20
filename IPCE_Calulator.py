import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.constants as const

# Define the constants
c = const.value('speed of light in vacuum')
h = const.value('Planck constant')
e = const.value('elementary charge')
k = const.value('Boltzmann constant')

def convert_spectrum(spectrum):
    lightSource = np.copy(spectrum)
    lightSource[:, 0] = lightSource[:, 0] * 1e-9  # wavelength: nm to m
    lightSource[:, 1] = lightSource[:, 1] / 1e-9  # irradiance: (W/m2/nm) to (W/m2/m)

    E = h * c / lightSource[:, 0] # change to energy unit
    d_lambda_d_E = h * c / E**2   # chain rule
    lightSource[:, 1] = lightSource[:, 1] * d_lambda_d_E * e / E
    lightSource[:, 0] = E / e #change the unit to eV
    return lightSource

# claculate the energy above the energy gap
def photons_above_bandgap(egap, spectrum):
    """Counts number of photons above given bandgap (egap)"""
    indexes = np.where(spectrum[:, 0] > egap) # return the elements chosen
    y = spectrum[indexes, 1][0]
    x = spectrum[indexes, 0][0]
    return np.trapz(y[::-1], x[::-1])

#integral to current
def jsc(egap, spectrum):
    return e * (photons_above_bandgap(egap, spectrum))

def photocurrent(spectrum):
    egap = spectrum[-1,0]
    current = jsc(egap, spectrum)
    result = "The photocurrent is " + str(current*0.1) + " " + "mAcm-2"    # convert Am-2 to mA cm-2
    return result

# Read the data and AM1.5 light source files
EQE = pd.read_excel("EQE.xlsx", header=0, dtype=float)  # nm vs EQE
spectrum = pd.read_csv("ASTMG173.csv", header=0, dtype=float)  # nm vs W m^-2 nm^-1 ; pandas DataFrame

# merge the two files
df_new = pd.merge(spectrum, EQE)

# muliplt the light source and QE number and convert the unit
df4 = df_new.iloc[:,1].mul(df_new.iloc[:,2])*0.01   # multiple EQE values; convert 1% to 0.01 

# combine the result and fit into the wavelength
df5 = pd.concat([df_new.iloc[:,0], df4], axis=1)

# convert the spectrum to energy nuit
solarCell = convert_spectrum(df5)

#calculate the photocurrent
result = photocurrent(solarCell)

if __name__ == "__main__":
    print(result)
