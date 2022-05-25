import pandas
# 25 May 2022

# LOOPING THROUGH DICTIONARIES FOR LOOP
student_dict = {
    "student": ["Albedo", "Ningguang", "Noelle", "Zhongli"],
    "score": [99, 98, 90, 96]
}
# Retrieve keys from each item in dict
for (key, value) in student_dict.items():
    print(key)

# Retrieve values from each key in dict
for (key, value) in student_dict.items():
    print(value)


# LOOPING W PANDAS DF & HOW TO ITERATE OVER PANDAS DF
student_df = pandas.DataFrame(student_dict)
print(student_df)

# TODO 1: Loop through a DF.
for (key, value) in student_df.items():
    print(value)

# TODO 2: Loop through rows of a DF, rather than columns using method "iterrows".
# index == the number in the first column of the df
for (index, row) in student_df.iterrows():
    # print(index)
    # print(row)
    # print(row.student)
    if row.student == "Ningguang":
        print(f"Ningguang's score is: {row.score}")