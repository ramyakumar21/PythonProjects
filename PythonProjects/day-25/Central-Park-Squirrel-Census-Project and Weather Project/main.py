from cmath import nan

#
# with open("weather_data.csv", mode = "r") as weather_data:
#     data = weather_data.readlines()
#
# print(data)

# Print temp data from weather_data.csv
# import csv
#
# with open("weather_data.csv", mode = "r") as weather_data:
#     data = csv.reader(weather_data)
#
#     temperature = []
#     for row in data:
#         if row[1] == "temp":
#             pass
#         else:
#             temperature.append(int(row[1]))
#
#     print(temperature)


import pandas as pd

# data = pd.read_csv("weather_data.csv")
#print(data)

# data_dict = data.to_dict()
# #print(data_dict)
# temp_list = data["temp"]
#
# average = temp_list.sum() / len(temp_list)
# print(average)
#
# mean = data["temp"].mean()
# print(mean)
#
# print(data["temp"].max())

#print(data[data.temp == data.temp.max()])

#Celsius to Fahrenheit: (F=(C * 9/5)+32)

# temp_in_C = data.temp[data.day == "Monday"]
# print(temp_in_C)
#
# monday = data[data.day == "Monday"]
# print(monday.temp)
#
# temp_in_F = (temp_in_C * 9 / 5) + 32
# print(temp_in_F)



# colour, total count for squirrels into a CSV file

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colour = data["Primary Fur Color"]
colour_unique = colour.unique()


black = colour[data["Primary Fur Color"] == "Black"].count()
cinnamon = colour[data["Primary Fur Color"] == "Cinnamon"].count()
gray = colour[data["Primary Fur Color"] == "Gray"].count()

to_learn = {
    "Primary Fur Color": ["Black", "Cinnamon", "Gray"],
    "Count" : [black, cinnamon, gray],
}

data_frame = pd.DataFrame(to_learn)
data_frame.to_csv("squirrel_data.csv")
