#FFT_Analyse_Vibration_Lockerheit.py

from os import sep
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from numpy.fft import rfft, rfftfreq,irfft

path = Path(r'C:\Users\danie\Google Drive\Bachelorarbeit\Messungen2\multiplot+fft\auswertung\\')

label = 'neuer Motor: kein Gewicht' 
### Lauffrequenz definieren ###
LF = 50

dirs = [i for i in path.iterdir() if i.is_file()]
dirs = sorted(dirs)

Datei = dirs[0]   

a=pd.read_csv(Datei, sep = ';',skiprows = [1,2],usecols = [4],dtype=float, decimal=',')


n=len(a)
print(n)
dt = 1/10000
acc=a.values.flatten()



fft=rfft(acc)*dt
freq=rfftfreq(n,d=dt)


FFT=abs(fft)

plt.plot(freq,FFT, label = label)


plt.axvline(x= 0.5*LF , ymin = 0,color  = 'red', ymax=0.5,alpha=0.4, label = '0,5X')
plt.axvline(x= 1*LF , ymin = 0, color  = 'green',ymax=0.5, alpha=0.4, label = '1X')
plt.axvline(x= 1.5*LF , ymin = 0, color  = 'orange',ymax=0.5, alpha=0.4, label = '1,5X')
plt.axvline(x= 2*LF , ymin = 0,color  = 'black', ymax=0.5, alpha=0.4, label = '2X')
plt.axvline(x= 2.5*LF , ymin = 0,color = 'purple', ymax=0.5, alpha=0.4, label = '2,5X')
plt.axvline(x= 3*LF , ymin = 0,color = 'yellow', ymax=0.5,alpha=0.4, label = '3X')
plt.axvline(x= 4*LF , ymin = 0,color = 'grey', ymax=0.5, alpha=0.4, label = '4X')
plt.axvline(x= 5*LF , ymin = 0, color = 'brown',ymax=0.5,alpha=0.4, label = '5X')
plt.axvline(x= 6*LF , ymin = 0, ymax=0.5, alpha=0.4, label = '6X')

plt.legend()	
plt.ylabel('Amplitude [mV]')
plt.xlabel('Frequenz [Hz]')

plt.show()
plt.close()