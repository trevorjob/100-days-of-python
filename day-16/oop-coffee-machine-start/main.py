from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
coffe_maker = CoffeeMaker()
cash_machine = MoneyMachine()
# my_menu_item = MenuItem()

while True:
        order = input(f"what would you like {my_menu.get_items()}: ")
        if order == "report":
                coffe_maker.report()
                cash_machine.report()
                continue
        elif order == "off":
                break
        drink = my_menu.find_drink(order)
        if not drink:
                continue
        if not coffe_maker.is_resource_sufficient(drink):
                continue
        if not cash_machine.make_payment(drink.cost):
                continue
        coffe_maker.make_coffee(drink)   
            


