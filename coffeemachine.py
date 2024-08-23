MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0
machine_on = True
while machine_on == True:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        print("Turning off the coffee machine. Goodbye!")
        machine_on = False
    elif order == "report":
        print(f"Water: " + str(resources["water"]) + "ml\n" + "Milk: " + str(resources["milk"]) + "ml\n" + "Coffee: " + str(resources["coffee"]) + "g\n" + "Money: " + "$" + str(money) + "\n")
    else:
        drink = MENU[order]
        for item in drink["ingredients"]:
            if drink["ingredients"][item] >= resources[item]:
             print(f"Sorry there is not enough {item}.")
             machine_on = False
            else:
                quarters = int(input("Please pay for your drink. How many quarters?"))
                dimes = int(input("How many dimes?"))
                nickles = int(input("How many nickles?"))
                pennies = int(input("How many pennies?"))
                inserted_money = float((quarters*0.25) + (dimes*0.10) + (nickles*0.05) + (pennies*0.01))
                if inserted_money == drink["cost"]:
                     money += inserted_money
                     for item in drink["ingredients"]:
                         resources[item] -= drink["ingredients"][item]
                     print(f"Here is your {order}. Enjoy! ")
                elif inserted_money > drink["cost"]:
                    change = inserted_money - drink["cost"]
                    money += inserted_money
                    money -= change
                    change = round(change, 2)
                    print(f"Here is ${change} dollars in change.")
                    for item in drink["ingredients"]:
                     resources[item] -= drink["ingredients"][item]
                    print(f"Here is your {order}. Enjoy! ")
                else:
                    print(f"Sorry there is not enough money. Money refunded")







