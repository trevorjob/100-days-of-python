#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        

with open("input/Letters/starting_letter.txt" , "r") as demo_letter:
    letter_list = demo_letter.read()

with open("input/Names/invited_names.txt", "r") as demo_letter:
    name_list = demo_letter.read()


for name in name_list.split("\n"):
    with open("output/ReadyToSend/letter_to_{}.txt".format(name), "w") as send:
        send.write(letter_list.replace("[name]", name))
        

# print(letter_list)
# print(name_list)
    