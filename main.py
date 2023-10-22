from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
coffee_machine = CoffeeMaker()
coin_processor = MoneyMachine()


is_on = True
while is_on:
    usr = input(f"What would you like? ({coffee_menu.get_items()}): ").lower()
    if usr == "off":
        is_on = False
    elif usr == "report":
        coffee_machine.report()
        coin_processor.report()
    else:
        drink = coffee_menu.find_drink(usr)
        if coffee_machine.is_resource_sufficient(drink) and coin_processor.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)


