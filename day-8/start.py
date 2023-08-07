name = "job"


# def greet(name):
#         name = "jeffry"
#         print(name)

# greet(name)
# print(name)

# def greet_with(name, location):
#         print("hello {}".format(name))
#         print("what is it like in {}".format(location))

# greet_with(name, "london")


# def paint_calc(height, width, cover):
#         print(math.ceil((height * width) / cover))


# test_h = int(input("what is the height "))
# test_w = int(input("what is the widthh "))
# coverage = 5

# paint_calc(height = test_h, width = test_w, cover = coverage)


alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
            "J", "K", "L", "M","N", "O", "P", "Q", "R", 
            "S", "T", "U", "V", "W", "X", "Y", "Z"]

question = "yes"
def encrypt(text, shift, type, direction):
        global alphabet
        shifted = ''

        for i in text:
                if not i.isalpha():
                        shifted += i
                        continue
                sete = alphabet.index(i)
                if (sete + shift) > len(alphabet) and (direction == "encode"):
                        sete = len(alphabet) - sete
                 
                shifted += alphabet[(sete + shift)] if type == True else alphabet[(sete - shift)]
        print("the {}d message is {}".format( direction, shifted.lower()))
        
        
while question == "yes":
        direction = input("type 'encode' or 'decode': ").lower()
        text = input("type your message: ").upper()
        shift = int(input("enter shift number: "))

        if (direction == "encode"):
                type = True
        else:
                type = False
      
        encrypt(text, shift, type, direction)
        question = input("would you like to go again\nyes or no ")



