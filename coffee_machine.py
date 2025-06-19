#TODO: create a dictrioary to hold stock of coffee and water
machine_stock = {"water" : 300 , "coffee" : 100 , "milk" : 200}

#TODO: create a disctonary to keep coffee flavours and their measures
coffee_flavour = {
                    "expresso"   : { "water" :50 , "coffee" : 18 , "milk" : 0 } ,
                    "latte"      : { "water" :200 , "coffee" : 24 , "milk" : 150 } ,
                    "cappuccino" : { "water" :250 , "coffee" : 24 , "milk" : 200 }
                }
#TODO: user input for flavour
user_input = input("What would you like? (expresso/latte/cappuccino)")
print (user_input)
#TODO: ask for coins based no flavour

#TODO: Validation - if not enough stock then return coins
