import pandas
import csv

# Reading a CSV wihtout pandas
# with open(".\weather.csv") as report:
#     data = csv.reader(report)
#     print(data)                            # Gives a CSV reader Object
#     temp = []
#     for row in data:
#         if row[1] != "Temp":
#             temp.append(int(row[1]))  # Assuming the temperature is in the second column
#         # print(row)
#     print(temp)



data = pandas.read_csv(".\weather.csv")  # This reads the CSV file into a DataFrame
# print(data)  # Display the DataFrame  (Pandas DataFrame Object)
# print(data["Temp"]) # Access the 'Temp' column (Pandas Series Object)

# Pandas has 2 types of data structures: Series and DataFrame
#  dataFrame is a 2D structure, while Series is a 1D structure

# Convert DataFrame to a dictionary
# to_dict = data.to_dict()  # Convert DataFrame to a dictionary
# print(to_dict)  # Display the dictionary

# temp_list = data["Temp"].to_list()  # Convert the 'Temp' column to a list
# print(temp_list)  # Display the list of temperatures

# avg_temp = sum(temp_list) / len(temp_list)  # Calculate the average temperature
# print(f"Average Temperature: {avg_temp}")  # Display the average temperature
# print(data["Temp"].mean())  # Calculate the mean using pandas
# print(data["Temp"].max())  # Calculate the maximum temperature using pandas
# print(data["Temp"].min())  # Calculate the minimum temperature using pandas

# # Accessing the 'Temp' column directly
# print(data.Temp)

# # Get data in row
# print(data[data.Day == "Monday"])  # Display the 'Day' column
# print(data[data.Temp == data["Temp"].max()])  # Display the row with the maximum temperature

monday = data[data.Day == "Monday"]
print(monday.Temp[0])

# Creating a DataFrame from scratch
# data_dict = {
#     "students": ["Alice", "Bob", "Charlie"],
#     "scores": [85, 90, 95]
# }
# data_frame = pandas.DataFrame(data_dict)  # Create a DataFrame from the dictionary
# print(data_frame)  # Display the DataFrame
# data_frame.to_csv("students_scores.csv", index=False)  # Save the DataFrame to a CSV file