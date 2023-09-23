from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()


is_on = True


while is_on:

    choice = input(f"What would you like? ({my_menu.get_items()}): ")
    # my_menu_item = MenuItem(name=my_menu.find_drink(choice).name,
    #                         water=my_menu.find_drink(choice).ingredients["water"],
    #                         milk=my_menu.find_drink(choice).ingredients["milk"],
    #                         coffee=my_menu.find_drink(choice).ingredients["coffee"],
    #                         cost=my_menu.find_drink(choice).cost)

    if choice == "off":

        is_on = False

    elif choice == "report":

        print(my_coffee_maker.report())

        print(my_money_machine.report())

    else:

        drink = my_menu.find_drink(choice)

        if my_coffee_maker.is_resource_sufficient(drink):

            payment = my_money_machine.make_payment(drink.cost)

            if payment:

                my_coffee_maker.make_coffee(drink)