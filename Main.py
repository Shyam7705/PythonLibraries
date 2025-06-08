# with open("Weather-data.csv") as dataFile:
#     data = dataFile.readlines()
#     print(data)

# import csv
# with open("Weather-data.csv") as dataFile:

#     data = csv.reader(dataFile)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

## Using pandas to read a CSV file
# import pandas as pd
# data = pd.read_csv("Weather-data.csv")   #reading the csv file by using the read_csv function
# print(data)

###   Date - 08-06-2025
# import pandas as pd
# data = pd.read_csv("Weather-data.csv")
# print(data)     # we are printing the data in CSV file by using the pandas

# here we are going to print the all the temperature by using pandas
# print(data["temp"])

# here we hava mainly two type of data structure 
# 1. series
# 2. DataFrame

# we can use some function to to convert the dataFrame and series into python basic data structure 

# converting the data into dict
# data_dict = data.to_dict()
# print(data_dict)
# there is many more function to convert the DataFrame to python basic data Structure


# converting the series of data into list
# temp_list = data["temp"].to_list()
# print(temp_list)
# there is many more function to convert the Series to python basic data Structure


# finding the average of all the temperature

# temp = data["temp"].to_list()
# size = len(temp)
# sum = 0
# for i in temp:
#     sum += i
# print(sum/size)

# temp1 = sum(temp) / len(temp)
# print(temp1)

#finding the average with the function of pandas
# print(data["temp"].mean())

# print(data["temp"].max())

# print(sorted((data["condition"].to_list()), reverse=True))

# getting data row-wise
# print(data[data["condition"] == "Sunny"])
# print(data[data.condition == "Sunny"])

# printing the row in which the temperature is maximum 
# maxi = (data[data["temp"] == data["temp"].max()])
# print(maxi)

# ptinting the temperatures of the sunny day
# Sunny = data[data["condition"] == "Sunny"]
# print(Sunny.temp) 

# monday = data[data.day == "Monday"]
# in_f = ((monday.temp * (9/5)) + 32)
# print(in_f)

# Creating the DataFrame from Scratch
# data_dict = {
#     "student" : ["Shyam", "Radhe", "Bade"],
#     "marks" : [5, 9, 8]
# }
# data = pd.DataFrame(data_dict)
# print(data)

# converting the DataFrame to CSV file
# data.to_csv("data_csv.csv")

