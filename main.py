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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry not enough {item}")
            return False
    return True


def process_coins():
    print(f"please insert coins")
    total = int(input("How many quarters?")) * 0.25
    total += int(input("How many dimes?")) * 0.1
    total += int(input("How many nickels?")) * 0.05
    total += int(input("How many pennies?")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry not enough money. Money Returned")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


is_on = True

# Prompt User what would you like
while is_on:
    answer = input(f"What would you like? (espresso/latte/cappuccino/)").lower()
    # Turn off when user types off
    if answer == 'off':
        print('Bye')
        is_on = False
    # Print report of all coffee machine resources
    elif answer == "report":
        print(f"{resources['water']}ml")
        print(f"{resources['milk']}ml")
        print(f"{resources['coffee']}g")
        print(f"${profit}")
    # check resources sufficient
    else:
        drink = MENU[answer]
        if is_resource_sufficient(drink["ingredients"]):
            #  Process coins
            payment = process_coins()
            # Check transaction if successful
            if is_transaction_successful(payment, drink["cost"]):
                # Make Coffee
                make_coffee(answer, drink["ingredients"])
