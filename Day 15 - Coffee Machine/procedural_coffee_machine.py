"""
Coffee Machine
by Grich
v1.0

Objectives:
1. Print report
2. CHeck resources sufficient?
3. Process coins; ask how many of each type of coin (penny, nickle, dime, quarter)
4. Check transaction successful?; if not return coins, else, proceed to make coffee.
5. Make Coffee; deduct resources
"""

from data import MENU, resources, profit


def print_res(res, balance):
    """Print the current available resources in the machine"""
    print(f""" 
Resources: 
Water:     {res["water"]}ml
Milk:      {res["milk"]}ml
Coffee:    {res["coffee"]}g
Money:     ${'{:.2f}'.format(balance)}
    """)


def is_suf(menu, res):
    """Check if there's enough ingredients to make the menu;
    Return True if so, False if not."""
    for ing in menu["ingredients"]:
        if res[ing] < menu["ingredients"][ing]:
            print(f"\nSorry there is not enough {ing}.\n")
            return False  # Return False
    return True  # Return True


def coin():
    """Process inserted coins into payment balance;
    Return payment balance."""
    print("    Please insert coins:")
    payment = 0
    payment += 0.25 * int(input("    How many quarters? "))
    payment += 0.10 * int(input("    How many dimes? "))
    payment += 0.05 * int(input("    How many nickles? "))
    payment += 0.01 * int(input("    How many pennies? "))

    return payment


def is_paid(total):
    """Returns a dictionary of payment and change if payment is successful; Returns False if payment is insufficient."""
    payment = coin()  # Process inserted coins into payment balance

    if payment < total:
        print("\nSorry that's not enough money. Payment refunded.\n")
        return False

    # Finished Algo#2, not focus on Algo#3.1-3.2
    change = (payment - total)
    payment -= change
    print(f"\nHere is ${'{:.2f}'.format(change)} in change.")

    return {"payment": payment, "change": change}


def make_coffee(menu, name, res):
    """Deduct ingredients from resources and print serving phrase."""
    for ing in menu["ingredients"]:  # 3.1.2 Deduct ingredients from resources in machine;
        res[ing] -= menu["ingredients"][ing]
    print(f"Here is your {name}. Enjoy!\n")


def main_prompt(res, balance):  # Beginning of main prompting loop
    """
    Ask for user's order;
    Function will always loop back to call itself until 'off' is entered;
    If 'report' is entered, current available resources will be printed.

    :param res: available resources in the machine
    :param balance: accumulated balance in the machine
    :return: None (terminate program)
    """
    choice = input("    What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "report":
        print_res(res, balance)
        main_prompt(res, balance)
        return
    elif choice == "off":
        print("\n!!------------MACHINE SHUTTING DOWN-------------!!")
        return

    try:
        drink = MENU[choice]  # This get the dictionary of drink menu
        if is_suf(drink, res) is False:
            main_prompt(res, balance)
            return

        print(f"""------------------
Order: {choice.title()}
Total: $ {'{:.2f}'.format(drink['cost'])}
------------------""")

        end_total = is_paid(drink["cost"])  # 3. Check if transaction is successful

        if end_total is False:  # 3.2 If transaction is unsuccessful, refund payment and recall the prompt
            main_prompt(res, balance)
            return

        balance += end_total["payment"]  # 3.1 If transaction is successful: 3.1.1 Add payment to balance;
        make_coffee(drink, choice, res) # 3.1.2 Deduct ingredients from resources and serve the coffee.

        main_prompt(res, balance)
        return

    except KeyError:
        print("""
!!------------ERROR INVALID ORDER---------------!!
Please enter a valid drink from the provided menu.
        """)
        main_prompt(res, balance)
        return


main_prompt(resources, profit)
