from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


end_program = False
money = MoneyMachine()
coffee = CoffeeMaker()
menu = Menu()
while not end_program:
    request = input(f"What would you like? {menu.get_items()}:")
    if request == "Off":
        end_program = True
    elif request == "report":
        coffee.report()
        print(f"money : ${money.report()}")
    else:
        drink = menu.find_drink(request)
        coffee_type = request
        if not coffee.is_resource_sufficient(drink):
            end_program = True
        elif not money.make_payment(drink.cost):
            end_program = True
        else:
            coffee.make_coffee(drink)
            end_program = True
