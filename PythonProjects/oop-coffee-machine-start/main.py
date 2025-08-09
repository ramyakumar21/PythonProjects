from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

choice = Menu()
order = CoffeeMaker()
money = MoneyMachine()

machine = "on"

while machine == "on":
    user_choice = input(f"What would you like to order? {(choice.get_items())}")
    item = choice.find_drink(user_choice)
    if user_choice == "off":
        machine = "off"
    elif user_choice == "report":
        order.report()
        money.report()
    else:
        if item is not None:
            resource_sufficient =  order.is_resource_sufficient(item)
            if resource_sufficient:
                is_transaction_successful = money.make_payment(item.cost)
                if is_transaction_successful:
                    order.make_coffee(item)



# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino/):”
# 2. Turn off the Coffee Machine by entering “off” to the prompt.
# 3. Print report.
# 4. Check resources sufficient?
# 5. Process coins.
# 6. Check transaction successful?
# 7. Make Coffee.