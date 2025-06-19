# Dictionary to Hold Stock of Machine
machine_stock = {"water" : 300 , "coffee" : 100 , "milk" : 200}

# Dictionary to hold coffee flavour and recipe
coffee_flavour = {
                    "expresso"   : { "water" :50 , "coffee" : 18 , "milk" : 0 } ,
                    "latte"      : { "water" :200 , "coffee" : 24 , "milk" : 150 } ,
                    "cappuccino" : { "water" :250 , "coffee" : 24 , "milk" : 200 }
                }

# Dictionary to get the flavour and recipie
def get_quantity(in_flavour,in_dict_coffee):
    return (in_dict_coffee.get(in_flavour))

def is_enough_stock(in_dict_selection,in_dict_stock):
    if (in_dict_stock.get("water") >= in_dict_selection.get("water")) and (in_dict_stock.get("coffee") >= in_dict_selection.get("coffee")) and (in_dict_stock.get("milk") >= in_dict_selection.get("milk")):
        return "yes"
    else:
        return "no"

# Ask user for coffee selection
user_coffee_flavour = input("What would you like? (expresso/latte/cappuccino)")
print (user_coffee_flavour)

# Declare a new dictionary; and
# get the quantity required for preparing a coffee using function get_quantity()
coffee_selection = {}
coffee_selection = get_quantity(user_coffee_flavour,coffee_flavour)

if is_enough_stock(coffee_selection,machine_stock) == "yes":
    print ("Enough Stock")
else:
    print("Not enough")
#print (coffee_selection)
# check stock availability