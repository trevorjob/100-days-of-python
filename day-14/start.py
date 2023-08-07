from data import resources, MENU, PRICES , COIN_NAMES

def check_for_resourses(order):
        for i in resources:
                if (i == "money") or (order == "esspresso" and i == "milk"): continue
                elif resources[i] < MENU[order]["ingridients"][i]:
                        print(f"sorry there is not enough {i}")
                        return False
        return True

def report():
        for i in resources:
                print(f"{i}: {'$' if i == 'money' else ''}{resources[i]}{'g' if i == 'coffee' else ''}{'ml' if i == 'milk' or i == 'water' else ''}")

def get_coins():
        coins = []
        print("please insert coins: ")
        for idx,i in enumerate(PRICES):
                coin_num = eval(input(f"how many {COIN_NAMES[idx].lower()}s: "))
                for _ in range(coin_num):
                        coins.append(i)
        return sum(coins)

def make_coffee(order):
        global resources
        for i in resources:
                if (i == "money") or (order == "esspresso" and i == "milk"): continue
                resources[i] -= MENU[order]["ingridients"][i]
        

while True:
        order = input("what woud you like ? (esspresso/latte/cappuccino): ").lower()
        if order == "report":
                report()
                continue
        
        if order == "off": break
        if not check_for_resourses(order):
                continue
        
        price = get_coins()
        og_cost = MENU[order]["cost"]
        if price < og_cost:
                print("you no get money")
                continue
        
        change = price - og_cost
        resources["money"] += og_cost
        if change > 0:
                print(f"here is your change ${change}")
                
        make_coffee(order)
        print(f"here is your {order} enjoy")
        
                        
                        
                        
                        
                        