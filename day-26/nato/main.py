student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    # print(row)
    #Access row.student or row.score
    pass

data  = pandas.read_csv('./nato_phonetic_alphabet.csv')
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# print(data)
code = {value.letter:value.code for idx,value in data.iterrows()}
print(code)
while True:
    user = input("enter code: ")
    user = [n.upper() for n in user]
    try:
        new_code = [code[val] for val in user if code[val]]
    except KeyError:
        print("sorry only letters in the aphabets please")
    else:
        break

print(new_code)