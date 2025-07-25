import pandas

data = pandas.read_csv("Squirrel_Data.csv")

red_squirrel_count = len(data[data["Highlight Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Highlight Fur Color"] == "Black"])
gray_squirrel_count = len(data[data["Highlight Fur Color"] == "Gray"])
print(red_squirrel_count)
print(black_squirrel_count)
print(gray_squirrel_count)

squirrel_colour_count = {
    "color" : ["Red","Black","Gray"],
    "count" : [red_squirrel_count, black_squirrel_count, gray_squirrel_count]
}
data_frame = pandas.DataFrame(squirrel_colour_count)
data_frame.to_csv("Squirrel_Count.csv",index=False)