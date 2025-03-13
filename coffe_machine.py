logo=['''     ( (
     ) )
  ........
  |      |]
  \      /  
   `----''']
print(logo[0])
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

def is_resources(choose):
    ingredients = MENU[choose]["ingredients"]
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"Sorry! Not enough {item}.")
            return False
    return True

def update_resources(choose):
    ingredients = MENU[choose]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]

while True:
    choose = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choose == "off":
        print("Turning off the coffee machine. Goodbye!")
        break
    elif choose == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
    elif choose in MENU:
        if not is_resources(choose):
            continue
        print("Please insert coins.")
        quarters = int(input("How many quarters? ")) * 0.25
        dimes = int(input("How many dimes? ")) * 0.10
        nickels = int(input("How many nickels? ")) * 0.05
        pennies = int(input("How many pennies? ")) * 0.01
        total_amount = quarters + dimes + nickels + pennies
    
        drink_cost = MENU[choose]['cost']
    
        if total_amount > drink_cost:
            change = total_amount - drink_cost
            print(f"Here is your {choose}, enjoy! Your change is: ${change:.2f}")
            update_resources(choose)
        elif total_amount == drink_cost:
            print(f"Here is your {choose}, enjoy!")
            update_resources(choose)
        else:
            print("Money is not enough")
