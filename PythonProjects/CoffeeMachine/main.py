MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def take_payment():
    """Takes user input and adds to return payment"""
    print("Please insert coins: \n")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))
    payment = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return round(payment, 2)

def make_coffee(choice):
    """Checks for ingredients"""
    for x in MENU[choice]["ingredients"]:
        resources[x] -= MENU[choice]["ingredients"][x]
    print("☕")
    print(f"Here is your {user_choice}. Enjoy!")

def check_resources(order_ingredients):
    """Checks for resource availability"""
    for x in order_ingredients:
        if order_ingredients[x] >= resources[x]:
            print(f"Sorry there is not enough {x}.")
            return False
    return True


machine = "on"
money = 0

while machine != "off":
    #  1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”

    user_choice = input(f"What would you like? {list(MENU)}:").lower()

    #  2. Turn off the Coffee Machine by entering “off” to the prompt.

    if user_choice == "off":
        machine = "off"

    #  3. Print report.

    elif user_choice == "report":
        print(f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g \nMoney: ${money}")

    #  4. Check resources sufficient?

    #  5. Process coins.

    #  6. Check transaction successful?

    #  7. Make Coffee.

    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        resources_sufficient = check_resources(MENU[user_choice]["ingredients"])
        if resources_sufficient:
            user_payment = take_payment()
            if user_payment < MENU[f"{user_choice}"]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                make_coffee(user_choice)
                money += MENU[f"{user_choice}"]["cost"]
                if user_payment > MENU[f"{user_choice}"]["cost"]:
                    print(f"Here is ${round((user_payment - MENU[f"{user_choice}"]["cost"]), 2)} in change. \n")

        # if user_choice == "espresso":
        #     if resources["water"] < MENU[f"{user_choice}"]["ingredients"]["water"]:
        #         print(f"Sorry there is not enough water.")
        #     elif resources["coffee"] < MENU[f"{user_choice}"]["ingredients"]["coffee"]:
        #         print(f"Sorry there is not enough coffee.")
        #     else:
        #         user_payment = take_payment()
        #         if user_payment < MENU[f"{user_choice}"]["cost"]:
        #             print("Sorry that's not enough money. Money refunded.")
        #         else:
        #             make_coffee(user_choice)
        #             money += MENU[f"{user_choice}"]["cost"]
        #             if user_payment > MENU[f"{user_choice}"]["cost"]:
        #                 print(f"Here is ${round((user_payment - MENU[f"{user_choice}"]["cost"]), 2)} in change. \n")
        # elif user_choice == "latte":
        #     if resources["water"] < 200:
        #         print(f"Sorry there is not enough water.")
        #     elif resources["coffee"] < 24:
        #         print(f"Sorry there is not enough coffee.")
        #     elif resources["milk"] < 150:
        #         print(f"Sorry there is not enough milk.")
        #     else:
        #         user_payment = take_payment()
        #         if user_payment < MENU[f"{user_choice}"]["cost"]:
        #             print("Sorry that's not enough money. Money refunded.")
        #         else:
        #             make_coffee(user_choice)
        #             money += user_payment
        #             if user_payment > MENU[f"{user_choice}"]["cost"]:
        #                 print(f"Here is ${round((user_payment - MENU[f"{user_choice}"]["cost"]), 2)} in change. \n")
        # elif user_choice == "cappuccino":
        #     if resources["water"] < 250:
        #         print(f"Sorry there is not enough water.")
        #     elif resources["coffee"] < 24:
        #         print(f"Sorry there is not enough coffee.")
        #     elif resources["milk"] < 100:
        #         print(f"Sorry there is not enough milk.")
        #     else:
        #         user_payment = take_payment()
        #         if user_payment < MENU[f"{user_choice}"]["cost"]:
        #             print("Sorry that's not enough money. Money refunded.")
        #         else:
        #             make_coffee(user_choice)
        #             money += user_payment
        #             if user_payment > MENU[f"{user_choice}"]["cost"]:
        #                 print(f"Here is ${round((user_payment - MENU[f"{user_choice}"]["cost"]), 2)} in change. \n")

    else:
            print("You selected invalid options.")





