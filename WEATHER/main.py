# with open("DATABASE.csv") as file:
#     data=file.readlines()
#     print(data)
#
# import csv
# with open("DATABASE.csv") as file:
#     data=csv.reader(file)
#     temp=[]
#     for line in data:
#         if line[1] != "TEMP":
#             temp.append(int(line[1]))
#
# print(temp)



import pandas
data=pandas.read_csv("DATABASE.csv")
print(type(data))
# s=sum(data["TEMP"])
# l=len(data["TEMP"])
# # print(s/l)
# print(data["TEMP"].mean())
# print(data["TEMP"].max())
# print(data["CONDITION"])
# print(data.CONDITION)
#GET THE DATA IN  ROW
# print(data[data.DAY=="MONDAY"])
#print max temp row
# print(data[data.TEMP==data.TEMP.max()])
monday=data[data.DAY=="MONDAY"]
# print(monday.CONDITION)
#conversion to cel to far
print(((monday.TEMP)*(9/5))+32)
#create a data frame from scratch
new_data={
    "student":["harshit","ajay","vijay"],
    "marks":[100,43,99]
}
data2=pandas.DataFrame(new_data)
# print(data2)
data2.to_csv("new_data")
