# Python Sequences
# list
# range
# string 
# tuple

names= ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
long_names = [name.upper() for name in names if len(name)>5]
print(long_names)

# with open("file1.txt") as file1:
#     file1_num = [int(line.strip()) for line in file1]

# with open("file2.txt") as file2:
#     file2_num = [int(line.strip()) for line in file2]
    
# result = [num for num in file1_num if num in file2_num] 

# print(result)

# Dictionary Comprehension
# syntax : new_dict = {new_key: new_value for (key, value) in dict.items() if text}

import random 

student_scores = {student:random.randint(1,100) for student in names}
print(student_scores)
qualified_students = {student:score for (student,score) in student_scores.items() if score >60 }
print(qualified_students)