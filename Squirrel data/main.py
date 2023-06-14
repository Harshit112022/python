import pandas
data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
count_gray=0
count_Cinnamon=0
count_Black=0
count_gray=len(data[data["Primary Fur Color"]=="Gray"])
count_Cinnamon=len(data[data["Primary Fur Color"]=="Cinnamon"])
count_Black=len(data[data["Primary Fur Color"]=="Black"])
colour={
    "Squirrel":["Gray","Cinnamon","Black"],
    "Number of Squirrel":[count_gray,count_Cinnamon,count_Black]
}
# print(colour)
data2 = pandas.DataFrame(colour)
print(data2)
data2.to_csv("colour_data")