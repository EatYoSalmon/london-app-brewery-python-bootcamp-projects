# List comprehension is a method of creating a new sequence type from an
# existing one without a loop, improving readibility. Not every programming
# language has this feature built-in like Python does.

# The original list
from numpy import double


number = [1, 2, 3, 4, 5, 6]

# Basic method of creating a new list with a for-loop statement:
new_list = []
for n in number:
    # n + 1 is the result expression:
    add_1 = n + 1
    new_list.append(add_1)

print(new_list)

# List comprehension method reduces the code to just 1 line; the syntax
# is [result_expression for item in list]:
new_list_comprehended = [n + 1 for n in number]

print(new_list_comprehended)

# List comprehension works on any sequence data type.
name = 'Grich'
billboard_name = [letter.upper() + '~' for letter in name]
print(billboard_name)

doubled_range = [n * 2 for n in range(1, 5)]
print(doubled_range)

# Create a conditional list comprehension by added an inline if statement
# at the end of the statement:
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name) < 5]
print(short_names)

cap_names = [name.upper() for name in names if len(name) > 5]
print(cap_names)
