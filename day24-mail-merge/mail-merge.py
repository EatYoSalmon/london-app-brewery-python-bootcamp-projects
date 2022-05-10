from pathlib import Path


parent_path = str(Path(__file__).parent.resolve())
names_path = "/Input/Names/invited_names.txt"
template_path = "/Input/Letters/starting_letter.txt"
output_path = "/Output/ReadyToSend"

with open(parent_path + names_path, "r") as file:
    names = file.readlines()

with open(parent_path + template_path, "r") as file:
    template = file.read()

for name in names:
    name = name.strip("\n")
    letter = template.replace("[name]", name)
    file_name = f"/Letter to {name}.txt"
    
    with open(parent_path + output_path + file_name, "w") as file:
        file.write(letter)

    