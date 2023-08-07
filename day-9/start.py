
# pythonDictionary = {"bug": "an error that occurrs occurred while programing",
#                     "function": "a reuseable piece of code",
                    
# }

# # print(pythonDictionary)
# pythonDictionary["loop"] = "a loop is being able to do somthing over and over again"

# # print(pythonDictionary)

# # empty_dic = {}

# # pythonDictionary = {}


# pythonDictionary["bug"] = "a new 1"
# print(pythonDictionary)

# for i in pythonDictionary:
#         print(pythonDictionary[i])

        

# def gading(student_scores):
#         obj = {}
#         for i in student_scores:
#                 check = student_scores[i]
#                 if check >= 91:
#                         obj[i] = "outstanding"
#                 elif check >= 81 and check <= 90:
#                          obj[i] = "exceeded expectations"
#                 elif check >= 71 and check <= 80:
#                         obj[i] = "acceptabe"
#                 else:
#                         obj[i] = "fail" 
#         return obj

# student_scores = {"harry" : 81,
#                   "ron": 78,
#                   "hermione" : 99,
#                   "draco": 74,
#                   "neville": 62,
# }
# student_grades = gading(student_scores)



# # print(student_grades)




# capitals = {
#         "france": "paris",
#         "germany": "berlin",
# }


# travel_log = {
#         "france": [
#                 {"paris": 2},
#                 {"jidon": 3},
#                 {"lille": 8}
#         ],
        
#         "germany": [
#                 {"berlin": 4},
#                 {"hamburg": 6}, 
#                 {"stuttgart": 10}
#         ]
# }

def add_new_country(stri,num, arr=[]):
        global travel_log
        new_obj = {}
        new_obj["country"] = stri
        new_obj["visits"] = num
        new_obj["cities"] = arr
        travel_log.append(new_obj) 
        
        

        
travel_log = [
        {
                "country" : "france",
                "visits": 12,
                "cities": ["paris", "lille", "dijon"],
        },
        
        {
                "country" : "germany",
                "visits": 5,
                "cities": ["berlin", "hamburg","stuttgart"],
        },
        
]
        
# add_new_country("russia", 2, ["moscow", "saint petersburg", "minsk"])
# print(travel_log)
bids = []

def init():
        global bids
        cont_name = input("enter name ")
        cont_bid = eval(input("enter cont_bid "))
        bids.append({"name" :cont_name, "bid": cont_bid})


winner_int  = 0
winner = {}
still_bid = "yes"
while still_bid != "no":
        init()
        still_bid = input("is there anyone who still wants to bid ")

for elm in bids:
        if elm["bid"] > winner_int:
                winner_int = elm["bid"]
                winner = elm
print("the winner is {} with a bid of ${}".format(winner["name"], winner["bid"]))                        
        
        