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
def is_resources_sufficient(order_ingredients):
    """check if resources are enough for drink user ask"""
    sufficient = True
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] > resources.get(ingredient, 0):
            print(f"Not enough {item} (needed: {order_ingredients[item]}, available: {resources.get(item, 0)}")
            sufficient = False
    return sufficient


def process_coins():
    print("please insert coins.")
    quarters = int(input("how many quarters"))
    dimes = int(input("how many dimes"))
    nickels = int(input("how many nickles"))
    pennies = int(input("how many pennies"))

    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.5) + (pennies * 0.01)
    return round(total , 2)

profit = 0
def is_transaction_successful(money_received, drink_cost):
    global profit
    if money_received < drink_cost:
        print("sorry that is not enough money money refunded")
        return False
    else:
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"here is the ${change} in change.")
        profit +=drink_cost
        return True


def make_coffee(drink_name, ingredients):
    for ingredient in ingredients:
        resources[ingredient] =-ingredients[ingredient]
    print(f"here is your {drink_name} enjoy")


def print_report():
    print(f"Water: {resources.get('water', 0)}ml")
    print(f"Milk: {resources.get('milk', 0)}ml")
    print(f"Coffee: {resources.get('coffee', 0)}g")
    print(f"Money: ${profit}")





valid_choices =["espresso", "latte", "cappuccino"]
while True:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        break
    elif user_choice == "report":
        print_report()
    elif user_choice in MENU:
        drink = MENU[user_choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(user_choice, drink["ingredients"])

    else:
        print("Invalid choice. Please try again.")







