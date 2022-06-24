# FileNotFoundError
# with open('a_file.txt') as file:
#     file.read()

# KeyError
# a_dictionary = {'key': 'value'}
# value = a_dictionary['non_existent_key']

# IndexError
# fruit_list = ['Apple', 'Banana', 'Pear']
# fruit = fruit_list[3]

# TypeError
# text = 'abc'
# print(text + 5)

# Exception Handling Keywords in Python:
#     try - Something that might cause an exception;
#     except - Do this if there was an exception;
#     else - Do this if there were no exceptions;
#     finally - Do this no matter what happens;
#     raise - Raise your own exception (error always thrown);

try:
    file = open('a_file.txt')
    a_dictionary = {'key': 'value'}
    print(a_dictionary['notKey'])

except FileNotFoundError:
    file = open('a_file.txt', 'w')
    file.write('Something')
    print("'a_file.txt' is created.")

except KeyError as error_message:
    print(f"That key {error_message} does not exist!")

else:
    content = file.read()
    print("Everthing went great!")
    print(f"Page content:\n{content}")

finally:
    file.close()
    raise TypeError("This is an error that I made up!")
