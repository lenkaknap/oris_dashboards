

from convert_data import map_data
import numpy as np
import matplotlib as plt

# df = all_info_combined(person_id = 2812)
# print(df)

# data for latitude and longitude
df = map_data(2812)
print(df["latitude"])
rows = len(df.index)

latitude = []
longitude = []

for i in range (rows):
    latitude.append(df["latitude"][i])
print(latitude)

for i in range (rows):
    longitude.append(df["longitude"][i])
print(longitude)

latitude_ls = df["latitude"].tolist()
print(latitude_ls, type(latitude_ls))


# udelat sum a jednotlivych rows, pripad all_info_combined()
# distanceSum = 0
# for row in rows:
#     distanceSum += row[29]
# print("Nabehal jsi: {} km vzdusnou carou.".format(distanceSum))

# print(dataFrame["distance"][0])
# print(dataFrame)
# print(dataFrame.dtypes)
# print(dataFrame.describe())

# print("You have run: {} kilometers!".format(dataFrame["distance"].sum()))
# print("You have climbed: {} meters (at least when the organizers provided meters of climbing)!".format(dataFrame["climbing"].sum()))
# print("You have found: {} controls!".format(dataFrame["controls"].sum()))
#
# distanceSum = dataFrame["distance"].sum()
# print(distanceSum)
#
# df2 = pd.DataFrame(dataFrame[["date","distance"]])
# print(df2)
# df2.plot(kind="bar", x = "date", y = "distance")
# df3 = pd.DataFrame(dataFrame[["discipline","distance"]])
# print(df3)
# df3.plot.bar(stacked=True)
# plt.pyplot.show()
#
# kmKlas = 0
# kmMid = 0
# kmSpri = 0
# i=0
#
# while i < 10:
#     if dataFrame["discipline"][i] == 1:
#         kmKlas += dataFrame["distance"][i]
#     elif dataFrame["discipline"][i] == 2:
#         kmMid += dataFrame["distance"][i]
#     elif dataFrame["discipline"][i] == 3:
#         kmSpri += dataFrame["distance"][i]
#     i += 1
# print(kmKlas)
# print(kmMid)
#print(kmSpri)
