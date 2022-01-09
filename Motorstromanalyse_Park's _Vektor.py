
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot
from pathlib import Path

path = Path(r'C:\Users\danie\Google Drive\Bachelorarbeit\Messungen2\multiplot+fft\auswertung\\')

dirs = [i for i in path.iterdir() if i.is_file()]
dirs = sorted(dirs)

Datei = dirs[0]   

a = pd.read_csv(Datei, sep=';', decimal=',', header=[0,1])


a.columns = a.columns.droplevel(1)


v1 = np.sqrt(2/3)
v2 = 1 / np.sqrt(6)
v3 = v2
v4 = 1 / np.sqrt(2)
v5 = v4

df = pd.DataFrame(dict(
    id_ =  v1 * a['Kanal A'] - v2 * a['Kanal B'] - v3 * a['Kanal C'],
    iq = v4 * a['Kanal B'] - v5 * a['Kanal C'],
))


sns.jointplot(
    data=df, x='id_', y='iq', kind='hex'
    )


plt.show()


plt.close()


