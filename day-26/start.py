# list comprehension

# numbers = [1,2,3]

# new_num = [n + 1 for n in numbers]


# name = "nandom"
# new_name = [letter for letter in name]
# print(new_name)
# mr = [num*2 for num in range(1,5)]
# print(mr)

# names = ['alex', 'beth', 'caroline', 'dave', 'freddy']
# shortss = [name for name in names if len(name) < 4]
# print(shortss)

# long = [name.upper() for name in names if len(name) >= 5]

# print(long)


# dictionary comprehensions
import random

# names = ['alex', 'beth', 'caroline', 'dave', 'freddy']


# new_dict = {student:random.randint(1,100) for student in names}

# next_dict = {key:value for key,value in new_dict.items() if value >= 60}

# print(next_dict)


# sentence = "What is the airspeed velocity of an unladen swallow?"
# result = {key:len(key) for key in sentence.split(' ')}
# print(result)

# weather_c = {
#         "monday": 12,
#         "tuesday": 14,
#         "wednesday": 15,
#         "thursday": 14,
#         "friday": 21,
#         "saturday": 22,
#         "sunday": 24,
# }

# weather_f = {key:value * 9/5 + 32 for key,value in weather_c.items()}
# print(weather_f)




student_dict = {
        "student": ["angela", "michael", "lillian"],
        "score": [56,76,98]
}

import pandas
student_data = pandas.DataFrame(student_dict)
# print(student_data)

for (index, row) in student_data.iterrows():
        print(row.score)




