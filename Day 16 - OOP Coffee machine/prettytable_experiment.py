from prettytable import PrettyTable


ma_table = PrettyTable()
print(ma_table)

ma_table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])
print(ma_table)

ma_table.add_column("Type", ["Electric", "Water", "Fire"])
print(ma_table)

print(ma_table.align)