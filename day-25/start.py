import csv
import pandas

# with open("weather_data.csv", "r") as data:
#         data = csv.reader(data)
#         temprature = []
#         for row in data:
#                 if row[1] != "temp":
#                         temprature.append(int(row[1]))
#         print(temprature)



# data = pandas.read_csv("weather_data.csv")        

# print(type(data))
# print(type(data["temp"]))
# data_dict = data.to_dict()
# data_list = data["temp"].to_list()
# average =  sum(data_list) / len(data_list)
# print(data["temp"].mean())
# print(data["temp"].max())
# print(average)

# get column
# print(data.condition)

# get row

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday.temp = int(monday.temp) * 9/5 + 32
# print(monday.temp)

# data_dict = {
#         "student" : ["amy", "mary", "james"],
#         "scores": [76, 65, 69]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)


data = pandas.read_csv("squirrels.csv") 
black = data[data["Primary Fur Color"] == "Black"]['Primary Fur Color'].to_list()
cinamon = data[data["Primary Fur Color"] == "Cinnamon"]['Primary Fur Color'].to_list()
gray = data[data["Primary Fur Color"] == "Gray"]['Primary Fur Color'].to_list()

data_dict = {
        "Fur Color": ["gray","red", "black"],
        "Count": [len(gray), len(cinamon), len(black)]
}

data = pandas.DataFrame(data_dict)
data.to_csv("squirrel_count.csv")

