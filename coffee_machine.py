# Dictionary to Hold Stock of Machine
machine_stock = {"water" : 300 , "coffee" : 100 , "milk" : 200}

# Dictionary to hold coffee flavour and recipe
coffee_flavour = {
                    "expresso"   : { "water" :50 , "coffee" : 18 , "milk" : 0 , "cost": 1.50} ,
                    "latte"      : { "water" :200 , "coffee" : 24 , "milk" : 150, "cost" : 2.50} ,
                    "cappuccino" : { "water" :250 , "coffee" : 24 , "milk" : 200 , "cost" : 3.00}
                }
# Exit coffee machine and stop serving coffee
still_serving_coffee = True

# Functionality to get the flavour and recipie
def get_quantity(in_flavour,in_dict_coffee):
    return (in_dict_coffee.get(in_flavour))

# Functionality to check if the stock is enough
def is_enough_stock(in_dict_selection,in_dict_stock):
    if (in_dict_stock["water"] >= in_dict_selection["water"]) \
        and (in_dict_stock["coffee"] >= in_dict_selection["coffee"]) \
        and (in_dict_stock["milk"] >= in_dict_selection["milk"]):

        return True

    else:
        return False
# Key Functionality - Now Make the final coffee
def make_coffee(selected_flavour_dict,machine_stock_dict):
    machine_stock_dict["water"] =  machine_stock_dict.get("water") - selected_flavour_dict.get("water")
    machine_stock_dict["coffee"] =  machine_stock_dict.get("coffee") - selected_flavour_dict.get("coffee")
    machine_stock_dict["milk"] =  machine_stock_dict.get("milk") - selected_flavour_dict.get("milk")

    # Return stock in the coffee machine
    return machine_stock_dict





def coffee_machine(user_coffee_flavour,in_dict_coffee_flav,in_dict_machine_stock):
    # Declare a new dictionary; and
    # get the quantity required for preparing a coffee using function get_quantity()
    coffee_selection = {}
    coffee_selection = get_quantity(user_coffee_flavour,in_dict_coffee_flav)
    print(coffee_selection)

    if is_enough_stock(coffee_selection,in_dict_machine_stock) == True:

        # Ask for money
        in_penny   = int(input("Insert Pennies  : "))
        in_dime    = int(input("Insert Dimes    : "))
        in_nickle  = int(input("Insert Nickles  : "))
        in_quarter = int(input("Insert Quarters : "))

        in_total = 0.0
        in_total = (in_penny*0.01) + (in_dime*0.1) + (in_nickle*0.05) + (in_quarter*0.25)

        # Calculate change to return
        tender_change = 0.0
        tender_change = round((in_total - coffee_selection["cost"]),00)
        print(f"Change = {tender_change}")

        # Amount is greater than or equal to the price of coffee flavour
        if tender_change >= 0.0:
            # Prepare coffee
            machine_stock = make_coffee(coffee_selection,in_dict_machine_stock)

            if tender_change == 0.0:
                print(f"Here's your {user_coffee_flavour}!Enjoy")

            else:
                print(f"Here's your change of {tender_change}. Enjoy your {user_coffee_flavour}")

        # Amount is less, ask customer to insert more coins
        else:
            print("Insufficient coins to prepare coffee")

    # Stock is insufficient to prepare coffee
    else:
        print ("There is no enough stock for a coffee, reselect")

# Enclose the program in while loop
# Exit program when Still Serving Coffee = False
while still_serving_coffee:
    # Ask user for coffee selection
    user_selection = input("What would you like? (expresso/latte/cappuccino): ")
    print (user_selection)

    # Exit program when machine is switched off
    if user_selection == "off":
        print("I'll see you again")
        still_serving_coffee = False
        exit()

    # Check coffee machine stock
    elif user_selection == "report":
        print(f'Water= {machine_stock["water"]} Milk= {machine_stock["milk"]} Coffee= {machine_stock["coffee"]}')

    # Make coffee
    else:
        coffee_machine(user_selection,coffee_flavour,machine_stock)