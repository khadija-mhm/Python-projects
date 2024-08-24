from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
#TODO 1. Print report
#TODO 2. Check resources sufficient?
#TODO 3. Process coins
#TODO 4. Check transaction successful?
#TODO 5. Make/give coffee

#create objects from classes 'MoneyMachine'
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
options = menu.get_items()

is_on = True
while is_on:
    order = input(f"What would you like: ({options})?").lower()
    if order == "off":
        is_on = False
    elif order == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink):
         if money_machine.make_payment(drink.cost):
             coffee_maker.make_coffee(drink)



