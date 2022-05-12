from numpy import blackman
import pandas as pd
from pathlib import Path


dir_path = str(Path(__file__).parent.resolve())
dataset_path = "/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"

df = pd.read_csv(dir_path + dataset_path)

fur_colors = ["Gray", "Cinnamon", "Black"]

# gray_count = df[df["Primary Fur Color"] == "Gray"]
# black_count = df[df["Primary Fur Color"] == "Black"]
# cinnamon_count = df[df["Primary Fur Color"] == "Cinnamon"]

color_count_list = []

for color in fur_colors:
    squirrels = df[df["Primary Fur Color"] == color]
    color_count = len(squirrels)
    color_count_list.append(color_count)

squirrel_data = {
    "Color": fur_colors,
    "Count": color_count_list
}

squirrel_count = pd.DataFrame(squirrel_data)
squirrel_count.to_csv(dir_path + "/squirrel_count.csv")
