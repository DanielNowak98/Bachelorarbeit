#FFT_Analyse_Motorstrom.py

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from numpy.fft import rfft, rfftfreq,irfft


path = Path(r'C:\Users\danie\Google Drive\Bachelorarbeit\Messungen2\multiplot+fft\auswertung\\')

dirs = [i for i in path.iterdir() if i.is_file()]
dirs = sorted(dirs)

Datei = dirs[0]    


a=pd.read_csv(Datei, sep = ';',usecols = [1],skiprows = [1], decimal = ',',low_memory=False)
print(a.info())
a.astype(float, errors='ignore')
a.columns = a.columns.to_flat_index()

n=len(a)

dt = 1/10000
acc=a.values.flatten()


fft=rfft(acc)*dt
freq=rfftfreq(n,d=dt)

    
FFT=abs(fft)

plt.plot(freq,FFT)


#########Lagerfrequenzen###########

netzfreq = 50
BPFO = 180
BPFI = 270
CF = 20
BSF = 118
###################################

i = 1
plt.axvline(x= netzfreq + i *BPFO, ymin = 0, ymax=0.5, color  = 'red',alpha=0.4, label = 'BPFO')
plt.axvline(x=netzfreq+i*BPFI, ymin = 0, ymax=0.5, color  = 'green',alpha=0.4, label = 'BPFI')
plt.axvline(x=netzfreq+i*CF,  ymin = 0, ymax=0.5, color  = 'orange',alpha=0.4, label = 'CF')
plt.axvline(x=netzfreq+i*BSF, ymin = 0, ymax=0.5, color  = 'black',alpha=0.4, label = 'BSF')


plt.legend()	
plt.ylabel('Amplitude [mV]')
plt.xlabel('Frequenz [Hz]')


plt.show()
plt.close()