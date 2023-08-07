#!/usr/bin/python3
#name = input('what is your name ')

#print('hello', name)
# num1, op , num2 = input('calculate ').split()


# num1 = int(num1)
# num2 = int(num2)

# if op == "+":
#         print("{} + {} = {}".format(num1, num2, num2 + num1))
# elif op == "-":
#         print("{} - {} = {}".format(num1, num2, num1 - num2))
# elif op == "*":
#         print("{} * {} = {}".format(num1, num2, num1 * num2))
# elif op == "/":
#         print("{} / {} = {}".format(num1, num2, num1 // num2))
# elif op == "%":
#         print("{} % {} = {}".format(num1, num2, num1 % num2))
# else:
#         print("put an operator")
# sum = num2 + num1
# mod = num1 % num2
# mul = num1 * num2
# div = num1 // num2


# print('sum = ', sum)
# print('mod = ', mod)
# print('mul = ', mul)
# print('div = ', div)
# # print('sum = ', sum)

# inv = eval(input("how much "))
# interest = eval(input("how much interest ")) * .01
# sum = 0

# for i in range(1, 11):
#         sum += inv + inv * interest

# print("year {} you made {:.2f}".format(i, sum))

                
'''
size = eval(input('make tree '))
i = 0
strin = ''
str2  = ''
sgn = '#'
base = size
while i in range(size):
        for c in range(base):
                strin += ' '
        for j in range(i):
                sgn += '##'
        print(strin, sgn)
        base -= 1
        i += 1
        strin = ''
        sgn = '#'
for c in range(size):
        strin += ' '
print(strin ,"#")
'''

# random_str = "    this is an imp  "
# print(random_str)
# random_str = random_str.lstrip()
# random_str = random_str.rstrip()
# print(random_str)
# print(random_str.capitalize())
# print(random_str.upper())
# print(random_str.lower())

# a_list = ["bunch", "of", "strings", "lists"]
# print(" ".join(a_list))

# a_list_2 = random_str.split()
# for i in a_list_2:
#         print(i)
# print("how many string :", random_str.count("is"))
# print("where is string :", random_str.find("is"))

# print(random_str.replace("an", "a kind of"))

# s = ''
# inp = input("enter string ")
# inp = inp.split()
# for i in inp:
#         s += i[0]
# print(s.upper())

# letter = "s"
# num = "4.64"
# spc = " "

# def isFloat(str_val):
#         try:
#                 float(str_val)
#                 return True
#         except ValueError:
#                 return False

# print("is s a letter or number : ", letter.isalnum())
# print("is s a letter : ", letter.isalpha())
# print("is 2 a number : ", num.isdigit())
# print("is num a float : ", isFloat(num))
# print("is s a lowercase : ", letter.islower())
# print("is s a uppercase : ", letter.isupper())
# print("is spc a space : ", spc.isspace())


# msg = input("type messega: ")
# encryption = ''
# num = 0
# msg.split()
# for i in msg:
#         num = ord(i)
#         if (num >= 97 and num <= 122) or (num >= 65 and num <= 90):
#                 num += 3
#                 encryption += chr(num)
#         else:
#                 encryption += i        

# print(encryption)
                
# def add_numbers(num1, num2):
#         return num1 + num2

# print("5 + 4 = {}".format(add_numbers(5,4)))
# name = "job"
# def assign_name():
#         global name 
#         name = "nandom"
# assign_name()
# print(name)

# str = "x + 3 = 6"
# def solve(str):
#         num1 = 0
#         num2 = 0
#         str.split()
#         for i in str:
#                 i = ord(i)
#                 if (i <= 57 and i >= 48):
                        
#                         if num1 == 0:
#                                 num1 += i - 47
#                         else:
#                                 num2 += i - 47
#                 # print(i)
        
#         print(num2 - num1)
        
# solve(str)

# num = eval(input("how many u want "))

# def rt_(num):
#         for i in range(2, num):
#                 if (num % i) == 0:
#                         return False
                        
#         return True

# my_arr = []
# for i in range(num):
#         if (rt_(i) == True):
#                 my_arr.append(i)
        
# print(my_arr)


print(__name__)