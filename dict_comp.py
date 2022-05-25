import random

# 24 May 2022

# DICT COMPREHENSION
#   Creates a new DICT from an existing list or dict using a shortened syntax
#   Unique to python
#   Cuts down on typing and makes code shorter and easier to read
# SYNTAX from list: new_dict = {new_key:new_value for item in list}
# SYNTAX from dict: new_dict = {new_key:new_value for (key,value) in dict.items()}
# SYNTAX from dict w cond: new_dict = {new_key:new_value for (key,value) in dict.items() if test}

# TODO 1: Create dict that contains a randomly generated score for each of the students in the list.
geo_students_list = ["Aether", "Albedo", "Gorou", "Itto", "Ninguang", "Noelle", "Yunjin", "Zhongli"]
geo_students_dict = {student: random.randint(1, 100) for student in geo_students_list}
print(f"dict comp from list {geo_students_dict}")

# TODO 1.1: Create new dict that contains ONLY the geo students with a grade 60 or higher.
passed_geo_students = {student: grade for (student, grade) in geo_students_dict.items() if grade >= 60}
print(passed_geo_students)