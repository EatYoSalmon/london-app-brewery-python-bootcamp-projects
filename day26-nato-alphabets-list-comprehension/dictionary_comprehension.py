from random import randint
import pandas as pd


# Dictionany comprehension is another handy built-in feature of Python similar
# to list comprehension. It allows programmer to create a new dictionary based
# on values of a list or items of another dictionary with a single
# declaritive statement.

# Syntax:
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dict.items()}

# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# student_scores = {student: randint(0, 100) for student in names}

# print(student_scores.items())

# passes_students = {
#     student: score for (student, score)
#     in student_scores.items() if score >= 60
# }

# Pandas DataFrame objects also work with dictionary comprehension; we can
# treate them as dictionaries for the most part as their data structure are
# similar.

student_dict = {
    'student': ['A', 'B', 'C'],
    'score': [56, 74, 95]
}

student_df = pd.DataFrame(student_dict)
print(student_df)

# However, by default, if we try to loop through the values within a DataFrame,
# it will not go row by row. Instead, it will unintuitively loop through each
# value within each column before moving on the the next column. Therefore, in
# looping through DataFrame objects, we will be using the built-in method
# called .itterows() which loops through rows within a DataFrame object.

for (key, value) in student_df.items():
    print(key)
    print(value)

for (index, row) in student_df.iterrows():
    # Each row within a DataFrame object is considered a Series object.
    print(index)
    print(row)
    print(row.student, row.score)
