from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cafe_menu = Menu()
machine = CoffeeMaker()
cashier = MoneyMachine()

is_running = True

while is_running:
    choice = input(f"    What would you like? ({cafe_menu.get_items()}): ").lower()

    if choice == "report":
        machine.report()
        cashier.report()

    elif choice == "off":
        is_running = False

    else:
        drink = cafe_menu.find_drink(choice)
        if machine.is_resource_sufficient(drink):

            print(f"Order: {drink.name.title()}")
            print(f"Total: ${'{:.2f}'.format(drink.cost)}")

            if cashier.make_payment(drink.cost):
                machine.make_coffee(drink)