# enemies = 1

# def increase_enemies():
#         enemies = 2
#         print("Enemies inside function: {}".format(enemies))
        
# increase_enemies()
# print("Enemies inside function: {}".format(enemies))


# # local scope

# def drink_potion():
#         potion_strength = 2
#         print(f"{potion_strength}")
        
# drink_potion()
# # print(potion_strength)


# # there is no block scope block scope

# game_level = 3

# enemies = ["skeleton", "zombie","alien"]
# if game_level < 5:
#         new_enemy = enemies[0]
        
# print(new_enemy)


# modifying the global scope

# enemies = 1

# def increase_enemies():
#         global enemies
#         enemies += 1
#         print("Enemies inside function: {}".format(enemies))
        
# increase_enemies()
# print("Enemies inside function: {}".format(enemies))



# global constants

# PI = 3.14159
# H = 1.3




import random
# guess the number game
def get_difficulty():
        get_difficulty = input("choose difficulty: 'easr' or 'hard': ")

        if get_difficulty == 'easy':
                return 10
        elif get_difficulty == 'hard':
                return 5
        return 0

attempt_count = get_difficulty()
num = random.randint(0,100)

while attempt_count != 0:    
        print(f"you have {attempt_count} guesses left")    
        guess = eval(input("guess the number: "))
        if guess > num:
                print("too high")
        elif guess < num:
                print("too low")
        else:
                print(f"congratulations you guessed it your number was {num}")
                break
        attempt_count -= 1
        if attempt_count == 0:
                print(f"you ran out of attempts your number was {num}")
        






