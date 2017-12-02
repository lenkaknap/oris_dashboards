from convert_data import time_data, kilometers_data
from pandas import to_datetime

df3 = kilometers_data(2812)
print(df3)

time_df = time_data(2812)
print(time_df)

# print(type(time_df['time']))
#
# suma = time_df['time'].sum()
# print(suma)

time_df['startTime'] = to_datetime(time_df['startTime'])
time_df['finishTime'] = to_datetime(time_df['finishTime'])

print(time_df)
print(time_df['time'][0])

time_df['time2'] = time_df['finishTime']-time_df['startTime']
print(time_df)

# tato suma funguje...
suma = time_df['time2'].sum()
print(suma)



