import random


logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user = []
computer = []
for i in range(2):
        user.append(random.choice(cards))
        computer.append(random.choice(cards))   

print("your cards are {} and the dealer {}".format(user, computer))    
def calc_score(user=[],computer=[]):
        
        user_sum = 0 if (sum(user) == 21) or (sum(computer)) > 21 else sum(user)
        computer_sum = 0 if (sum(computer) == 21) or (sum(user) > 21) else sum(computer)
        return user_sum, computer_sum

again = True
def calc_who(who):
        global cards, computer_sum, user_sum, user, computer
        who.append(random.choice(cards))
        user_sum ,computer_sum = calc_score(user, computer)


def end_game(user, computer):
        global again
        if computer == 0 and user == 0:
                print("DRAW")
        elif user == 0:
                print("BLACKJACK: user {} wins!".format(user))
        elif computer == 0:
                print("BLACKJACK: computer {} wins!".format(computer))
                
        again = False
                
user_sum ,computer_sum = calc_score(user, computer)   


while again:
        deal = input("press 'y' to deal again press 'n' to place game ")
        if deal == "y":
                calc_who(user)
        elif deal == "n":
                while computer_sum < 17:
                        calc_who(computer)
                print(user_sum, computer_sum)
        end_game(user_sum, computer_sum)
                
        
               

print(user_sum, computer_sum)

# while True:
#         again = input("press n if you want add")
        


# winner = user_sum if user_sum > computer_sum else computer_sum
# print("{} wins: {}".format("user" if winner == user_sum else "computer", winner))
        
# print(logo)