# a_dictionary = {"key": "value"}
# val = a_dictionary["non"]


# # Index error
# fruit_list = ["apple", "orange", "pear"]
# print(fruit_list[10])


# # FileNotFound
# try:
#         file = open("a_file.txt")
#         a_dictionary = {"key": "value"}
#         val = a_dictionary["key"]
# except FileNotFoundError:
#         file = open("a_file.txt", "w")
#         file.write("somthing")
# except KeyError as error_message:
#         print(f"the key {error_message} does not exist")
# else:
#         content = file.read()
#         print(content)
# finally:
#         raise TabError("i made it up")
        
        
height = float(input("height: "))
weight = int(input("weight: "))
        
if height > 3:
        raise ValueError("human height must be below 3 meters")

bmi = weight / height **2 
print(bmi)