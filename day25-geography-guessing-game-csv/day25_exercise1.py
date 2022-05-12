from pathlib import Path
import pandas as pd


path = str(Path(__file__).parent.resolve())

df = pd.read_csv(path + "/weather_data.csv")

temperatures = df["temp"]

# Returns DataFrame or Series as a list.
temp_list = temperatures.to_list()

# Built-in sum() and len() to find the average of numerical elements in a list
average = sum(temp_list) / len(temp_list)

# Pandas methods allows for a more simplistic function call.
temp_average = temperatures.mean()
temp_maximum = temperatures.max()

# Refer columns in a DataFrame object in a square bracket like a dict key;
df["condition"]
# Or refer to them directly as attribute.
df.condition

# Get all rows that pass the specified condition.
df[df["day"] == "Monday"]
df[df.condition == "Sunny"]

df[df["temp"] == df.temp.max()]

# Get specific value from a row by specifying its column attribute/key
monday = df[df.day == "Monday"]
monday_condition = monday.condition
monday_condition = monday["condition"]

monday_in_farenheit = (int(monday.temp) * 1.8) + 32
print(monday_in_farenheit)

# Creating DataFrame from scratch with a dicitonary.
data_dict = {
    "students": ["Tom", "Dick", "Harry"],
    "scores": [76, 56, 65]
}

student_data = pd.DataFrame(data_dict)
student_data.to_csv("day25-geography-guessing-game-csv/student_scores.csv")