# solar_EQE
calculate the photocurrent from the IPCE spectrum

This code can be used for calculating the theoretical photocurrent value of a solar cell illuminated at one sun with a IPCE (EQE) spectrum provided.
The IPCE spectrum is a two column Excel file (.xlxs), name "EQE.xlxs". The first column lists the wavelength values in nm unit and 
the second one lists the values of quantum efficiecies (%). 
Make sure the name of the Excel file is "EQE.xlxs" and the key of the first column is 'nm'. Error might occur if the key is not correct.
In the sample folder, there is one sample Excel file that you can refer.
After you place the EQE file with your own spectrum and run this script, you will get the value of photocurrent.
