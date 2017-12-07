from convert_data import time_data
import pandas as pd

# this gives me the no such table error
time_df = time_data(2812)
print(time_df)



print(time_df)
print(time_df['time'][0])

# time_df['time2'] = time_df['finishTime']-time_df['startTime']
print(time_df)

soucet = time_df['time2'][0]+time_df['time2'][1]
print(soucet)
# tato suma funguje...
suma = time_df['time2'].sum()
print(suma)



prumer = pd.to_datetime(time_df['time2'][0]/time_df['distance'][0])
print(prumer)



