# 24 May 2022

# LIST COMPREHENSION
#   Creates a new list from an existing list (i.e. sequences)
#   Unique to python
#   Cuts down on typing and makes code shorter and easier to read
# SYNTAX: new_list = [new_item for item in list]

# PYTHON SEQUENCES
#   Have a specific order
#   e.g. list, range, string, tuple
#   List comprehensions will follow the specific order of the sequence


# TODO 1: Create a new list from the "numbers" list, where you added 1 to each item.
numbers = [1, 2, 3]

# TODO 1.1: Using for loop.
new_numbers_1 = []
for num in numbers:
    new_num = num + 1
    new_numbers_1.append(new_num)
print(f"for loop: {new_numbers_1}")

# TODO 1.2: Using list comprehension.
new_numbers_2 = [old_num + 1 for old_num in numbers]
print(f"list comp: {new_numbers_2}")

# TODO 2: List comprehension for strings.
name = "Stone"
letter_list = [letter for letter in name]
print(f"list comp for strings: {letter_list}")

# TODO 3: Create a new list from a range, where the list items are double the values in the range.
range_list = [num * 2 for num in range(1, 5)]
print(f"list comp in range: {range_list}")

# CONDITIONAL LIST COMPREHENSION
#   Adds a condition at the end
#   This means the list comp will ONLY add a new item if the condition is met
# SYNTAX: new_list = [new_item for item in list if test]

# TODO 3: Conditional list comprehension.
names = ["Aether", "Albedo","Gorou", "Itto", "Ninguang", "Noelle", "Yunjin", "Zhongli"]
short_names = [name for name in names if len(name) < 5]
print(f"conditional list comp: {short_names}")

# TODO 3.1: Create a new list that contains the names longer than 5 character in ALL CAPS.
long_names_cap = [name.upper() for name in names if len(name) > 4]
print(f"conditional list comp ALL CAPS: {long_names_cap}")

# CODING ROOMS EXERCISE
# TODO 4.1: Create a new list that squares the numbers from the old list.
base_numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num ** 2 for num in base_numbers]
print(f"squared list comp: {squared_numbers}")

# TODO 4.1: Create a new list containing ONLY the even numbers from the old list.
result = [num for num in base_numbers if num % 2 == 0]
print(f"even number list comp: {result}")

# TODO 5: Read the two text files. Make a list comp for numbers (as an int, NOT str) that are in BOTH text files.

f1 = open("file1.txt", "r")
f1_list = f1.readlines()
print(f"number in file1: {f1_list}")

f2 = open("file2.txt", "r")
f2_list = f2.readlines()
print(f"number in file2: {f2_list}")

in_both = [int(num) for num in f1_list if num in f2_list]
print(f"numbers in both files list comp:{in_both}")
