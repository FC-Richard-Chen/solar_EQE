# solar_EQE
calculate the photocurrent from the IPCE spectrum

This code is to calculate the theoritical photocurrent value of a solar cell illuminated at one sun.
You must provide a IPCE (EQE) spectrum.
The IPCE spectrum is a two column Excel file (.xlxs), name "EQE.xlxs". The first column is the wavelength in nm unit and 
the second one is the values of quantum efficiecy (%). 
Make sure the file name is "EQE.xlxs" and the key of the first column is 'nm'. Error might occur if the key is not correct.
In the sample folder, there is one sample Excel file that you can refer.
Once you place the EQE file with your own spectrum, run this script, and you will get the value of photocurrent.
