from art import logo, vs
from data import data
import random

def get_data():
        return random.choice(data)

def picker(pick):
        if pick == 'A':
                return first, second
        if pick == 'B':
                return second, first

def printers(first, second, score):
        if score > 0:
                print(f"your current score is : {score}")
                
        print(f"compare A: {first['name']}, a {first['description']}, from {first['country']}")
        print(vs)
        print(f"compare B: {second['name']}, a {second['description']}, from {second['country']}")

score = 0
n = True
first = get_data()
while n:
        second = get_data()
        if first == second:
                second = get_data()
                
        printers(first, second,score)
        pick = input("who has the most followers 'A' or 'B': " ).upper()
        selected, other = picker(pick)
        if (selected["follower_count"] > other["follower_count"]):
                score += 1
        else:
                print(f"sorry thats wrong your score is {score}")
                n = False
        
        first = second
        




