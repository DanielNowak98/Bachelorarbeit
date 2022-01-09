#Maximum- und Mittelwerte berechnen.py

import pandas as pd
from pathlib import Path
import xlsxwriter

def list_to_df_name(path):	
    dirs = [i for i in path.iterdir() if i.is_file()]
    dirs = sorted(dirs)

    MU1 = dirs[0]
    MU2 = dirs[1]
    MU3 = dirs[2]
    MU4 = dirs[3]
    MU5 = dirs[4]
    MU6 = dirs[5]

    return MU1,MU2, MU3, MU4, MU5, MU6
      
def get_df(MU1, MU2, MU3, MU4, MU5, MU6):
    df = pd.read_csv(MU1, sep = ';', skiprows=[1,2],dtype=float, decimal=',')
    df2 = pd.read_csv(MU2, sep = ';', skiprows=[1,2],dtype=float, decimal=',')
    df3 = pd.read_csv(MU3, sep = ';', skiprows=[1,2],dtype=float, decimal=',')
    df4 = pd.read_csv(MU4, sep = ';', skiprows=[1,2],dtype=float, decimal=',')
    df5 = pd.read_csv(MU5, sep = ';', skiprows=[1,2],dtype=float, decimal=',')
    df6 = pd.read_csv(MU6, sep = ';', skiprows=[1,2],dtype=float, decimal=',')
    return df, df2, df3, df4, df5, df6

def get_maximum(df,df2, df3, df4, df5, df6):
    mm1A = df['Kanal A'].max()
    mm2A = df2['Kanal A'].max()
    mm3A = df3['Kanal A'].max()
    mm4A = df4['Kanal A'].max()
    mm5A = df5['Kanal A'].max()
    mm6A = df6['Kanal A'].max()


    mm1B = df['Kanal B'].max()
    mm2B = df2['Kanal B'].max()
    mm3B = df3['Kanal B'].max()
    mm4B = df4['Kanal B'].max()
    mm5B = df5['Kanal B'].max()
    mm6B = df6['Kanal B'].max()



    mm1C = df['Kanal C'].max()
    mm2C = df2['Kanal C'].max()
    mm3C = df3['Kanal C'].max()
    mm4C = df4['Kanal C'].max()
    mm5C = df5['Kanal C'].max()
    mm6C = df6['Kanal C'].max()



    mm1D = df['Kanal D'].max()
    mm2D = df2['Kanal D'].max()
    mm3D = df3['Kanal D'].max()
    mm4D = df4['Kanal D'].max()
    mm5D = df5['Kanal D'].max()
    mm6D = df6['Kanal D'].max()

    mmA = [mm1A,mm2A,mm3A,mm4A,mm5A,mm6A]
    mmB = [mm1B,mm2B,mm3B,mm4B,mm5B,mm6B]
    mmC = [mm1C,mm2C,mm3C,mm4C,mm5C,mm6C]
    mmD = [mm1D,mm2D,mm3D,mm4D,mm5D,mm6D]

    return mmA,mmB,mmC,mmD

def get_Mittelwert(df,df2,df3,df4,df5,df6):
    mwa = df['Kanal A'].mean()
    mw2a = df2['Kanal A'].mean()
    mw3a = df3['Kanal A'].mean()
    mw4a = df4['Kanal A'].mean()
    mw5a = df5['Kanal A'].mean()
    mw6a = df6['Kanal A'].mean()

    mwb = df['Kanal B'].mean()
    mw2b = df2['Kanal B'].mean()
    mw3b = df3['Kanal B'].mean()
    mw4b = df4['Kanal B'].mean()
    mw5b = df5['Kanal B'].mean()
    mw6b = df6['Kanal B'].mean()

    mwc = df['Kanal C'].mean()
    mw2c = df2['Kanal C'].mean()
    mw3c = df3['Kanal C'].mean()
    mw4c = df4['Kanal C'].mean()
    mw5c = df5['Kanal C'].mean()
    mw6c = df6['Kanal C'].mean()

    mwd = df['Kanal D'].mean()
    mw2d = df2['Kanal D'].mean()
    mw3d = df3['Kanal D'].mean()
    mw4d = df4['Kanal D'].mean()
    mw5d = df5['Kanal D'].mean()
    mw6d = df6['Kanal D'].mean()

    mwa_list = [mwa,mw2a,mw3a,mw4a,mw5a,mw6a]
    mwb_list = [mwb,mw2b,mw3b,mw4b,mw5b,mw6b]
    mwc_list = [mwc,mw2c,mw3c,mw4c,mw5c,mw6c]
    mwd_list = [mwd,mw2d,mw3d,mw4d,mw5d,mw6d]

    return mwa_list, mwb_list, mwc_list, mwd_list

def printmittelwertandmax(mmA, mmB, mmC , mmD,mwa_list, mwb_list, mwc_list, mwd_list):
    book = xlsxwriter.Workbook('test.xlsx')
    sheet = book.add_worksheet()

    # Überschriften hinzufügen
    x = ['Maximum W1', 'Maximum V2', 'Maximum U1', 'Maximum Piezzo']

    column = 1
    row = 0 
    for i in x:    
        sheet.write(row, column, i)
        column += 1
    
    x = ['Mittelwert W1', 'Mittelwert V2', 'Mittelwert U1', 'Mittelwert Piezzo']

    column = 5
    row = 0 
    for i in x:    
        sheet.write(row, column, i)
        column += 1

    
    y= ['kein Gewicht', '14 Gramm', '19 Gramm', '24 Gramm', '29 Gramm', '31 Gramm']

    column = 0
    row = 1 
    for i in y:    
        sheet.write(row, column, i)
        row += 1
    
    #### Maximum

    row = 1   
    column = 1

    for item in mmA :     

        sheet.write(row, column, item)          
        row += 1 

    column = 2
    row = 1 

    for item in mmB :     

        sheet.write(row, column, item)
        row += 1
    
    column = 3
    row = 1 
    
    for item in mmC :     

        sheet.write(row, column, item)
        row += 1
    
    column = 4
    row = 1 
    
    for item in mmD :     

        sheet.write(row, column, item)
        row += 1
    

    ## Mittelwerte 
    row = 1   
    column = 5

    for item in mwa_list :     

        sheet.write(row, column, item)          
        row += 1 

    column = 6
    row = 1 

    for item in mwb_list :     

        sheet.write(row, column, item)
        row += 1
    
    column = 7
    row = 1 
    
    for item in mwc_list :     

        sheet.write(row, column, item)
        row += 1
    
    column = 8
    row = 1 
    
    for item in mwd_list :     

        sheet.write(row, column, item)
        row += 1


    book.close()

def main(path):
    MU1,MU2,MU3,MU4,MU5,MU6 = list_to_df_name(path)
    df,df2,df3,df4,df5,df6 = get_df(MU1,MU2,MU3,MU4,MU5,MU6)
    mmA,mmB,mmC,mmD = get_maximum(df,df2,df3,df4,df5,df6)
    mwa_list, mwb_list, mwc_list, mwd_list = get_Mittelwert(df,df2,df3,df4,df5,df6)
    printmittelwertandmax(mmA,mmB,mmC,mmD,mwa_list, mwb_list, mwc_list, mwd_list)
    

if __name__ == "__main__":
    path = Path(r'C:\Users\danie\Google Drive\Bachelorarbeit\Messungen2\Messung neuer AUfbau alter Motor\sortiert\50Hz\csv')
    main(path)   