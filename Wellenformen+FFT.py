#Wellenform+FFT.py

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from numpy.fft import rfft, rfftfreq

def list_to_df_name(path):
	"""
	Sammelt alle Dateinamen des Ordners "Path". 
	Diese werden in einer Liste hinterlegt, welche anschließend der größe nach sotiert wird. 

	Rückgabe:
		Namen aller dateien, sortiert der Größe nach. Diese sind in den Variablen MU1-MU6 hinterlegt.
	"""

	dirs = [i for i in path.iterdir() if i.is_file()]
	dirs = sorted(dirs)

	MU1 = dirs[0]
	MU2 = dirs[1]
	MU3 = dirs[2]
	MU4 = dirs[3]
	MU5 = dirs[4]
	MU6 = dirs[5]

	return MU1,MU2,MU3,MU4,MU5,MU6
	  
def plot(MU1,MU2,MU3,MU4,MU5,MU6,waveforms,plot_name):

	"""
	Erstellt einen multi Plot aller Wellenformdarstellungen der Unwuchtmessungen einer Frequenzklasse.

	Rückgabe:
		Plot aller Unwuchtmessungen einer Frequenzklasse als .png.
	"""

	df1 = pd.read_csv(MU1, sep = ';', decimal=',',skiprows = [1],low_memory=False)
	df1.astype(float, errors='ignore')
	df1.columns = df1.columns.to_flat_index()


	fig, axs = plt.subplots(6, sharex=True, sharey=True,figsize=(20,10))
	fig.suptitle(plot_name)
	axs[0].plot(df1['Zeit'], df1['Kanal A'], label = 'W1')
	axs[0].plot(df1['Zeit'], df1['Kanal B'], label = 'V2')
	axs[0].plot(df1['Zeit'], df1['Kanal C'], label = 'U1')
	axs[0].plot(df1['Zeit'], df1['Kanal D'], label = 'Piezzo')

	axs[0].set_title('kein Gewicht')
	axs[0].set_xlim(0, 0.05)
	axs[0].set_ylim(-50, 50)


	df2 = pd.read_csv(MU2, sep = ';', decimal=',',skiprows = [1],low_memory=False)
	df2.astype(float, errors='ignore')
	df2.columns = df2.columns.to_flat_index()

			
	axs[1].plot(df2['Zeit'], df2['Kanal A'], label = 'W1')
	axs[1].plot(df2['Zeit'], df2['Kanal B'], label = 'V2')
	axs[1].plot(df2['Zeit'], df2['Kanal C'], label = 'U1')
	axs[1].plot(df2['Zeit'], df2['Kanal D'], label = 'Piezzo')
	
	axs[1].set_title('Gewicht: 14 Gramm')


	df3 = pd.read_csv(MU3, sep = ';', decimal=',',skiprows = [1])
	df3.astype(float, errors='ignore')
	df3.columns = df3.columns.to_flat_index()

			
	axs[2].plot(df3['Zeit'], df3['Kanal A'], label = 'W1')
	axs[2].plot(df3['Zeit'], df3['Kanal B'], label = 'V2')
	axs[2].plot(df3['Zeit'], df3['Kanal C'], label = 'U1')
	axs[2].plot(df3['Zeit'], df3['Kanal D'], label = 'Piezzo')
	
	axs[2].set_title('Gewicht: 19 Gramm')

	df4 = pd.read_csv(MU4, sep = ';', decimal=',',skiprows = [1])
	df4.astype(float, errors='ignore')
	df4.columns = df4.columns.to_flat_index()

	axs[3].plot(df4['Zeit'], df4['Kanal A'], label = 'W1')
	axs[3].plot(df4['Zeit'], df4['Kanal B'], label = 'V2')
	axs[3].plot(df4['Zeit'], df4['Kanal C'], label = 'U1')
	axs[3].plot(df4['Zeit'], df4['Kanal D'], label = 'Piezzo')
	
	axs[3].set_title('Gewicht: 24 Gramm')

	df5 = pd.read_csv(MU5, sep = ';', decimal=',',skiprows = [1])
	df5.astype(float, errors='ignore')
	df5.columns = df5.columns.to_flat_index()

	axs[4].plot(df5['Zeit'], df5['Kanal A'], label = 'W1')
	axs[4].plot(df5['Zeit'], df5['Kanal B'], label = 'V2')
	axs[4].plot(df5['Zeit'], df5['Kanal C'], label = 'U1')
	axs[4].plot(df5['Zeit'], df5['Kanal D'], label = 'Piezzo')
	
	axs[4].set_title('Gewicht: 29 Gramm')

					
	df6 = pd.read_csv(MU6, sep = ';', decimal=',',skiprows = [1])
	df6.astype(float, errors='ignore')
	df6.columns = df6.columns.to_flat_index()

	axs[5].plot(df6['Zeit'], df6['Kanal A'], label = 'W1')
	axs[5].plot(df6['Zeit'], df6['Kanal B'], label = 'V2')
	axs[5].plot(df6['Zeit'], df6['Kanal C'], label = 'U1')
	axs[5].plot(df6['Zeit'], df6['Kanal D'], label = 'Piezzo')
	
	axs[5].set_title('Gewicht: 31 Gramm')

	fig.text(0.5, 0.02, 'Zeit [s]', ha='center')
	fig.text(0.095, 0.5, 'Amplitude [mV]', va='center', rotation='vertical')
	
	plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),shadow=True, ncol=2)
   
	plt.savefig( waveforms + plot_name +  "Waveform"+ ".png")
	
	plt.close()

def get_fft_plot_KanalA(MU1, MU2, MU3, MU4, MU5, MU6,KanalA_img,plot_name):

	
	"""
	Erstellt einen überlagerten Plot aller FFTs des Kanal A zu den jeweiligen Unwuchtmessungen.
	Es wird zu jedem Kanal eine FFT berechnet, sowie der Plot dessen erstellt.

	Rückgabe:
		Überlagerter Plot aller FFTs der jeweiligen Unwuchtmessung einer Frequenzklasse für Kanal A als .png.
	"""

	fig = plt.figure(figsize=(20,10))
	#fig, axs = plt.subplots(6, sharex=True, sharey=True,figsize=(10,5))
	dt=1/100000 # - 1/Abtastrate
	######################## Motor Unwucht 31 Gramm ##############################
	a=pd.read_csv(MU6, sep = ';', skiprows=[1,2],usecols = [1],dtype=float, decimal=',')


	n=len(a) #Zeitinkrement

	acc=a.values.flatten() #DataFrame in 1D-Array umwandeln


	fft=rfft(acc)*dt
	freq=rfftfreq(n,d=dt)

	FFT=abs(fft)

	plt.plot(freq,FFT, label = 'Gewicht: 31 Gramm')


    ######################## Motor Unwucht 29 Gramm ##############################	
	b=pd.read_csv(MU5, sep = ';', skiprows=[1,2],usecols = [1],dtype=float, decimal=',')


	n=len(b)
	

	acc=b.values.flatten() 

	fft=rfft(acc)*dt
	freq=rfftfreq(n,d=dt)

	FFT=abs(fft)

	plt.plot(freq,FFT, label = 'Gewicht: 29 Gramm')

	######################## Motor Unwucht 24 Gramm ##############################
	c=pd.read_csv(MU4, sep = ';', skiprows=[1,2],usecols = [1],dtype=float, decimal=',')


	n=len(c)
	
	acc=c.values.flatten() 

	fft=rfft(acc)*dt
	freq=rfftfreq(n,d=dt)

	FFT=abs(fft)

	plt.plot(freq,FFT, label = 'Gewicht: 24 Gramm')

	######################## Motor Unwucht 19 Gramm ##############################
	d=pd.read_csv(MU3, sep = ';', skiprows=[1,2],usecols = [1],dtype=float, decimal=',')


	n=len(d)
   

	acc=d.values.flatten() 
	

	fft=rfft(acc)*dt
	freq=rfftfreq(n,d=dt)

	FFT=abs(fft)

	plt.plot(freq,FFT, label = 'Gewicht: 19 Gramm')

	######################## Motor Unwucht 14 Gramm ##############################
	e=pd.read_csv(MU2, sep = ';', skiprows=[1,2],usecols = [1],dtype=float, decimal=',')


	n=len(e)
	
	acc=e.values.flatten()
	
	fft=rfft(acc)*dt
	freq=rfftfreq(n,d=dt)

	FFT=abs(fft)

	plt.plot(freq,FFT, label = 'Gewicht: 14 Gramm')

	######################## Motor Unwucht 0 Gramm ##############################
	f=pd.read_csv(MU1, sep = ';', skiprows=[1,2],usecols = [1],dtype=float, decimal=',')


	n=len(f)
   
	acc=f.values.flatten() 
	

	fft=rfft(acc)*dt
	freq=rfftfreq(n,d=dt)

	FFT=abs(fft)

	plt.plot(freq,FFT, label = 'kein Gewicht')

	plt.legend(ncol=2,loc=9)
	plt.ylabel('Amplitude [mV]')
	plt.xlabel('Frequenz [Hz]')
	plt.ylim([0, 200])
	plt.xlim([1,5000])
	plt.title(plot_name + " FFT" +" W1")
	plt.savefig( KanalA_img + plot_name + "Kanal A"+ ".png")
	plt.close()

def get_fft_plot_KanalB(MU1, MU2, MU3, MU4, MU5, MU6,KanalB_img,plot_name):
	"""
	Erstellt einen überlagerten Plot aller FFTs des Kanal B zu den jeweiligen Unwuchtmessungen.
	Es wird zu jedem Kanal eine FFT berechnet, sowie der Plot dessen erstellt.

	Rückgabe:
		Überlagerter Plot aller FFTs der jeweiligen Unwuchtmessung einer Frequenzklasse für Kanal B als .png.
	"""


	fig = plt.figure(figsize=(20,10))
	dt=1/100000
	######################## Motor Unwucht 31 Gramm ##############################
	a=pd.read_csv(MU6, sep = ';', skiprows=[1,2],usecols = [2],dtype=float, decimal=',')
	


	n=len(a)

	acc=a.values.flatten()

	fft=rfft(acc)
	freq=rfftfreq(n,d=dt)

	FFT=abs(fft)

	plt.plot(freq,FFT, label = 'Gewicht: 31 Gramm')

	######################## Motor Unwucht 29 Gramm ##############################
	b=pd.read_csv(MU5, sep = ';', skiprows=[1,2],usecols = [2],dtype=float, decimal=',')

	#print(a.head())

	n=len(b)
	

	acc=b.values.flatten()

	fft=rfft(acc)*dt
	freq=rfftfreq(n,d=dt)

	FFT=abs(fft)

	plt.plot(freq,FFT, label = 'Gewicht: 29 Gramm')

	######################## Motor Unwucht 24 Gramm ##############################
	c=pd.read_csv(MU4, sep = ';', skiprows=[1,2],usecols = [2],dtype=float, decimal=',')

	#print(a.head())

	n=len(c)
	
	acc=c.values.flatten()
	

	fft=rfft(acc)*dt
	freq=rfftfreq(n,d=dt)

	FFT=abs(fft)

	plt.plot(freq,FFT, label = 'Gewicht: 24 Gramm')

	######################## Motor Unwucht 19 Gramm ##############################
	d=pd.read_csv(MU3, sep = ';', skiprows=[1,2],usecols = [2],dtype=float, decimal=',')


	n=len(d)
   

	acc=d.values.flatten()


	fft=rfft(acc)*dt
	freq=rfftfreq(n,d=dt)

	FFT=abs(fft)

	plt.plot(freq,FFT, label = 'Gewicht: 19 Gramm')

	######################## Motor Unwucht 14 Gramm ##############################
	e=pd.read_csv(MU2, sep = ';', skiprows=[1,2],usecols = [2],dtype=float, decimal=',')

	#print(a.head())

	n=len(e)
	

	acc=e.values.flatten()


	fft=rfft(acc)*dt
	freq=rfftfreq(n,d=dt)

	FFT=abs(fft)

	plt.plot(freq,FFT, label = 'Gewicht: 14 Gramm')

	######################## Motor Unwucht 0 Gramm ##############################
	f=pd.read_csv(MU1, sep = ';', skiprows=[1,2],usecols = [2],dtype=float, decimal=',')



	n=len(f)
   
	acc=f.values.flatten()


	fft=rfft(acc)*dt
	freq=rfftfreq(n,d=dt)

	FFT=abs(fft)

	plt.plot(freq,FFT, label = 'kein Gewicht')


	plt.legend(ncol=2,loc=9)

	plt.ylabel('Amplitude [mV]')
	plt.xlabel('Frequenz [Hz]')
	plt.ylim([0, 200])
	plt.xlim([1,5000])
	plt.title(plot_name + " FFT" +" V2")

	plt.savefig( KanalA_img + plot_name + "Kanal B"+ ".png")
	plt.close()

def get_fft_plot_KanalC(MU1, MU2, MU3, MU4, MU5, MU6,KanalC_img,plot_name):

	
	"""
	Erstellt einen überlagerten Plot aller FFTs des Kanal C zu den jeweiligen Unwuchtmessungen.
	Es wird zu jedem Kanal eine FFT berechnet, sowie der Plot dessen erstellt.

	Rückgabe:
		Überlagerter Plot aller FFTs der jeweiligen Unwuchtmessung einer Frequenzklasse für Kanal C als .png.
	"""

	fig = plt.figure(figsize=(20,10))
	dt=1/100000
	######################## Motor Unwucht 31 Gramm ##############################
	a=pd.read_csv(MU6, sep = ';', skiprows=[1,2],usecols = [3],dtype=float, decimal=',')
	
	n=len(a)
	
	acc=a.values.flatten()


	fft=rfft(acc)*dt
	freq=rfftfreq(n,d=dt)

	FFT=abs(fft)

	plt.plot(freq,FFT, label = 'Gewicht: 31 Gramm')

	######################## Motor Unwucht 29 Gramm ##############################
	b=pd.read_csv(MU5, sep = ';', skiprows=[1,2],usecols = [3],dtype=float, decimal=',')


	n=len(b)
	

	acc=b.values.flatten()


	fft=rfft(acc)*dt
	freq=rfftfreq(n,d=dt)

	FFT=abs(fft)

	plt.plot(freq,FFT, label = 'Gewicht: 29 Gramm')

	######################## Motor Unwucht 24 Gramm ##############################
	c=pd.read_csv(MU4, sep = ';', skiprows=[1,2],usecols = [3],dtype=float, decimal=',')

	n=len(c)
	
	acc=c.values.flatten()


	fft=rfft(acc)*dt
	freq=rfftfreq(n,d=dt)

	FFT=abs(fft)

	plt.plot(freq,FFT, label = 'Gewicht: 24 Gramm')

	######################## Motor Unwucht 19 Gramm ##############################
	d=pd.read_csv(MU3, sep = ';', skiprows=[1,2],usecols = [3],dtype=float, decimal=',')

	#print(a.head())

	n=len(d)
   

	acc=d.values.flatten()


	fft=rfft(acc)*dt
	freq=rfftfreq(n,d=dt)

	FFT=abs(fft)

	plt.plot(freq,FFT, label = 'Gewicht: 19 Gramm')

	######################## Motor Unwucht 14 Gramm ##############################
	e=pd.read_csv(MU2, sep = ';', skiprows=[1,2],usecols = [3],dtype=float, decimal=',')


	n=len(e)
	

	acc=e.values.flatten() 
	

	fft=rfft(acc)*dt
	freq=rfftfreq(n,d=dt)

	FFT=abs(fft)

	plt.plot(freq,FFT, label = 'Gewicht: 14 Gramm')

	######################## Motor Unwucht 0 Gramm ##############################
	f=pd.read_csv(MU1, sep = ';', skiprows=[1,2],usecols = [3],dtype=float, decimal=',')


	n=len(f)
   
	acc=f.values.flatten()


	fft=rfft(acc)*dt
	freq=rfftfreq(n,d=dt)

	FFT=abs(fft)

	plt.plot(freq,FFT, label = 'kein Gewicht')


	plt.legend(ncol=2,loc=9)
		
	plt.ylabel('Amplitude [mV]')
	plt.xlabel('Frequenz [Hz]')
	plt.ylim([0, 200])
	plt.xlim([1,5000])  
	plt.title(plot_name + " FFT" +" U1")
	
	plt.savefig( KanalA_img + plot_name + "Kanal C"+ ".png")
	plt.close()

def get_fft_plot_KanalD(MU1, MU2, MU3, MU4, MU5, MU6,Vibimages,plot_name):
	"""
	Erstellt einen überlagerten Plot aller FFTs des Kanal D zu den jeweiligen Unwuchtmessungen.
	Es wird zu jedem Kanal eine FFT berechnet, sowie der Plot dessen erstellt.

	Rückgabe:
		Überlagerter Plot aller FFTs der jeweiligen Unwuchtmessung einer Frequenzklasse für Kanal D als .png.
	"""


	fig = plt.figure(figsize=(20,10))
	dt=1/100000
	######################## Motor Unwucht 31 Gramm ##############################
	a=pd.read_csv(MU6, sep = ';', skiprows=[1,2],usecols = [4],dtype=float, decimal=',')
	

	n=len(a)

	acc=a.values.flatten()


	fft=rfft(acc)*dt
	freq=rfftfreq(n,d=dt)

	FFT=abs(fft)

	plt.plot(freq,FFT, label = 'Gewicht: 31 Gramm')

	######################## Motor Unwucht 29 Gramm ##############################
	b=pd.read_csv(MU5, sep = ';', skiprows=[1,2],usecols = [4],dtype=float, decimal=',')


	n=len(b)
	

	acc=b.values.flatten()


	fft=rfft(acc)*dt
	freq=rfftfreq(n,d=dt)

	FFT=abs(fft)

	plt.plot(freq,FFT, label = 'Gewicht: 29 Gramm')

	######################## Motor Unwucht 24 Gramm ##############################
	c=pd.read_csv(MU4, sep = ';', skiprows=[1,2],usecols = [4],dtype=float, decimal=',')

	#print(a.head())

	n=len(c)
	
	acc=c.values.flatten()


	fft=rfft(acc)*dt
	freq=rfftfreq(n,d=dt)

	FFT=abs(fft)

	plt.plot(freq,FFT, label = 'Gewicht: 24 Gramm')

	######################## Motor Unwucht 19 Gramm ##############################
	d=pd.read_csv(MU3, sep = ';', skiprows=[1,2],usecols = [4],dtype=float, decimal=',')

	#print(a.head())

	n=len(d)
   

	acc=d.values.flatten()
	

	fft=rfft(acc)*dt
	freq=rfftfreq(n,d=dt)

	FFT=abs(fft)

	plt.plot(freq,FFT, label = 'Gewicht: 19 Gramm')

	######################## Motor Unwucht 14 Gramm ##############################
	e=pd.read_csv(MU2, sep = ';', skiprows=[1,2],usecols = [4],dtype=float, decimal=',')


	n=len(e)
	

	acc=e.values.flatten()


	fft=rfft(acc)*dt
	freq=rfftfreq(n,d=dt)

	FFT=abs(fft)

	plt.plot(freq,FFT, label = 'Gewicht: 14 Gramm')

	######################## Motor Unwucht 0 Gramm ##############################
	f=pd.read_csv(MU1, sep = ';', skiprows=[1,2],usecols = [4],dtype=float, decimal=',')

	#print(a.head())

	n=len(f)
   
	acc=f.values.flatten()

	fft=rfft(acc)*dt
	freq=rfftfreq(n,d=dt)

	FFT=abs(fft)

	plt.plot(freq,FFT, label = 'kein Gewicht')


	plt.legend(ncol=2,loc=9)

	plt.ylabel('Amplitude [mV]')
	plt.xlabel('Frequenz [Hz]')
	plt.title(plot_name + " FFT" +" Piezzo")
	plt.savefig( Vibimages + plot_name + "Kanal D"+ ".png")
	plt.close()

def main(path,Vibimages,plot_name,KanalA_img,KanalB_img,KanalC_img,waveforms):
 
 MU1,MU2,MU3,MU4 ,MU5, MU6 = list_to_df_name(path)
 print("data listed from: " + str(path))

 print("Plotting and saving Files: \t")
 plot(MU1,MU2,MU3,MU4,MU5,MU6,waveforms,plot_name)
 print("Waveforms saved to: " + str(path))

 get_fft_plot_KanalA(MU1,MU2,MU3,MU4,MU5,MU6,KanalA_img,plot_name)
 print("KanalA FFT saved to:  " + str(KanalA_img))

 get_fft_plot_KanalB(MU1, MU2, MU3, MU4, MU5, MU6,KanalB_img,plot_name)
 print("KanalB FFT saved to:  " + str(KanalB_img))

 get_fft_plot_KanalC(MU1, MU2, MU3, MU4, MU5, MU6,KanalC_img,plot_name)
 print("KanalC FFT saved to:  " + str(KanalC_img))

 get_fft_plot_KanalD(MU1, MU2, MU3, MU4, MU5, MU6,Vibimages,plot_name)
 print("KanalD FFT saved to:  " +str(Vibimages))

 print("All Data saved to: " +str(path))
 
if __name__ == "__main__":

	path = Path(r'PFAD')
	plot_name = "5Hz neuer Motor"

	Vibimages= r"PFAD\\"
	KanalA_img = r"PFAD\\"
	KanalB_img = r"PFAD\\"
	KanalC_img = r"PFAD\\"
	waveforms = r"PFAD\\"
	main(path,Vibimages,plot_name,KanalA_img,KanalB_img,KanalC_img,waveforms)