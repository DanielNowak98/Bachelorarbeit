#FFT_Analyse_Vibration.py

from os import sep
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from numpy.fft import rfft, rfftfreq,irfft


path = Path(r'C:\Users\danie\Google Drive\Bachelorarbeit\Messungen2\multiplot+fft\auswertung\\')


BPFO = 179.5
BPFI = 270
CF = 20
BSF = 118




dirs = [i for i in path.iterdir() if i.is_file()]
dirs = sorted(dirs)

Datei = dirs[0]    

    
a=pd.read_csv(Datei, sep = ';',skiprows = [1,2],usecols = [4],dtype=float, decimal=',')
a.columns = a.columns.droplevel(1)  


n=len(a)
print(n)
dt = 1/10000
acc=a.values.flatten()



fft=rfft(acc)*dt
freq=rfftfreq(n,d=dt)

    

FFT=abs(fft)

plt.plot(freq,FFT, label = 'Gewicht: 31 Gramm')

########################Lagerfrequenzen######################


for i in range(1,6):
    plt.axvline(x= i* BPFO, ymin = 0, ymax=0.5, color  = 'red',alpha=0.4, label = str(i)+'BPFO')
    plt.axvline(x= i*BPFI, ymin = 0, ymax=0.5, color  = 'green',alpha=0.4, label =str(i)+ 'BPFI')
    plt.axvline(x= i*CF,  ymin = 0, ymax=0.5, color  = 'orange',alpha=0.4, label = str(i)+'CF')
    plt.axvline(x= i*BSF, ymin = 0, ymax=0.5, color  = 'black',alpha=0.4, label =str(i)+ 'BSF')



plt.legend()	
plt.ylabel('Amplitude [mV]')
plt.xlabel('Frequenz [Hz]')

    
#plt.savefig( KanalA_img + plot_name + "Kanal A"+ ".png")
plt.show()
plt.close()