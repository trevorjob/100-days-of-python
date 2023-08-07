import random

words = ["flamingo", "base", "cognitive", "human", "speakers"]
random_word = random.choice(words)
plane = []
check = True
count = 5



def print_arr(count):
        for i in count:
                print("{}".format(i),end=" ")
        print("\n")

for i in range(len(random_word)):
        plane.append("_")

        
        
while check:
        if ("_" not in plane) or (count == 0):
                check = False
                break
        guess = input("guess a letter: ")
        for idx , elm in enumerate(random_word):
                if elm == guess:
                        plane[idx] = guess
                        count += 1
        count -= 1
        print_arr(plane)
        print(count)

print("you {} your word was {}".format("win" if count > 0 else "lose" ,random_word))                        
                
        