import pandas
#
# data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data['temp'].to_list()
# print(data['temp'].max())
#
#
# print(data.condition)

# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print((monday.temp * 9/5) + 32)

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# x= pandas.DataFrame(data_dict)
# x.to_csv("new_data.csv")

data = pandas.read_csv("Squirrel_Data.csv")
grey = data[data["Primary Fur Color"] == 'Gray']
grey_count = grey["Primary Fur Color"].count()
red = data[data["Primary Fur Color"] == 'Cinnamon']
red_count = red["Primary Fur Color"].count()
black = data[data["Primary Fur Color"] == 'Black']
black_count = black["Primary Fur Color"].count()

squirrel_dict = {
    "Fur Color": ["grey", "red", "black"],
    'Count': [grey_count, red_count, black_count]
}
data.to_excel("squirrel_count.xlsx")

