MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 15,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 25,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 30
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def sufficient(order_ingredients):
    for item in order_ingredients:
        if resources[item] < order_ingredients[item]:
            print(f"Sorry not enough {item}")
            return False
    return True

def coin():
    print("Please insert coins")
    total = int(input("How many ₹1 coin: ")) * 1
    total += int(input("How many ₹2 coin: ")) * 2
    total += int(input("How many ₹5 coin: ")) * 5
    total += int(input("How many ₹10 coin: ")) * 10
    return total

def successfull(payment, drink_cost):
    if payment >= drink_cost:
        change = payment - drink_cost
        print(f"Here is {change} in change.")
        global profit
        profit += payment
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(choice, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {choice} ☕️. Enjoy!")

on = True

while on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ₹{profit}")
    else:
        drink = MENU[choice]
        if sufficient(drink['ingredients']):
            payment = coin()
            if successfull(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])