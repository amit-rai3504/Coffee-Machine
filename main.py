from config import MENU
from config import resources

end_program = False

def enough_resources(coffee_type):
    if resources["water"] < MENU[coffee_type]["ingredients"]["water"]:
        print("Not enough water, sorry can't make coffee")
        return False
    if resources["coffee"] < MENU[coffee_type]["ingredients"]["coffee"]:
        print("Not enough coffee, sorry can't make coffee")
        return False
    if coffee_type != "espresso" and resources["milk"] < MENU[coffee_type]["ingredients"]["milk"]:
        print("Not enough milk, sorry can't make coffee")
        return False
    return True


def make_coffee(coffee_type):
    resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
    resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
    if coffee_type != "espresso":
        resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
    print(f"Here is your {coffee_type}. Enjoy!.")


def calc_amount_entered(quarters, dimes, nickles, penny):
    return (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * penny)


def get_report():
    for resource in resources:
        print(f"{resource}: {resources[resource]}")


def check_transaction_successful():
    print("Please insert coins")
    quarters = int(input("How many quarters? :"))
    dimes = int(input("How many dimes? :"))
    nickles = int(input("How many nickles? :"))
    penny = int(input("How many pennies? :"))
    money_entered = calc_amount_entered(quarters, dimes, nickles, penny)
    if money_entered < MENU[request]["cost"]:
        print("Not Enough Money, Money Refunded")
        return False
    resources["money"] += MENU[request]["cost"]
    money_to_be_returned = money_entered - MENU[request]["cost"]
    print(f"here is your ${money_to_be_returned} change")
    return True


while not end_program:
    request = input("What would you like? (espresso/latte/cappuccino):")
    if request == "Off":
        end_program = True
    elif request == "report":
        get_report()
    elif request in MENU:
        coffee_type = request
        if not enough_resources(coffee_type):
            end_program = True
        elif not check_transaction_successful():
            end_program = True
        else:
            make_coffee(coffee_type)
            end_program = True
