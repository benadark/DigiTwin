#aqi library for PM to AQI algorthism
import aqi
import math
#Pandas used to read excel file
import pandas as pd


df = pd.read_csv (r'C:\Users\ben24\Downloads\purpleair-newer.csv') #reading the csv file containing pm values 
column=df['PM2.5_CF1_ug/m3'] #storing the PM 2.5 values into variable 'column'
#column2=df['PM10.0_CF1_ug/m3'] #storing the PM 10 values into variable 'column2'
#column3=df['created_at'] #store dates


myaqi=[]; myaqi2=[]; dates=[]
#loop through each PM value stored in column variable
for i in range(len(column)):
   if math.isnan(column[i]) or column[i]>1000:
       continue
   else:
      a=aqi.to_iaqi(aqi.POLLUTANT_PM25, column[i], algo=aqi.ALGO_EPA) #uses aqi module to calculate aqi and appends it to myaqi list
      myaqi.append(a)
      #b=aqi.to_iaqi(aqi.POLLUTANT_PM10, column2[i], algo=aqi.ALGO_EPA)
      #myaqi2.append(b)
     # dates.append(column3[i])

data = {
  #"Date": dates,
  "AQI_PM2.5":myaqi,
  #"AQI_PM10":myaqi2
}
df = pd.DataFrame(data) #converts list to data frame
df.to_csv('Chev_AQI_data_PM25_PM10.csv',index = False) #writes to csv file 
