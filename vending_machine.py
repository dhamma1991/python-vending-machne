# Ordered Dict is needed here
# We want the coin denominations to run from highest to lowest
# In order for the program to try and give out higher coin denominations as change first
from collections import OrderedDict

products = { # Key represents product, value is price
    1: {"Coca-Cola (Can)": 70},
    2: {"Coca-Cola (Bottle)": 120},
    3: {"Diet Coca-Cola (Can)": 70},
    4: {"Diet Coca-Cola (Bottle)": 120},
    5: {"Fanta": 70},
    6: {"Sprite": 70},
    7: {"Bottled Water": 50},
    8: {"Ginger Beer (Can)": 90}
}

# Sort ordered dictionaries in reverse order so that the larger denominations are used first to make up the change
usd = {1:20, 2:20, 5:20, 10:20, 25:20, 50:20, 100:20, 200:20}
ordered_usd = OrderedDict(sorted(usd.items(), reverse=True))
eur = {1:20, 2:20, 5:20, 10:20, 20:20, 50:20, 100:20, 200:20}
ordered_eur = OrderedDict(sorted(eur.items(), reverse=True))

# Error Strings
error_string = "Error: unable to make up amount with available coins"
error_input_string = "Error: please enter a number corresponding to the product you want"


# Get Change Function
def get_change(amount, denomination=ordered_eur):  # Default is eur
    change = []  # Initialize empty list
    for coin, quantity in denomination.items():  # Loop through the available coins
        if denomination[coin] == 0:  # If the machine has ran out of a particular coin
            continue  # Go to the next largest available denomination
        while coin <= amount:  # While the coin being looped over is less than the amount outstanding...
            amount -= coin  # Deduct the value of that coin from the amount
            change.append(coin)  # Add the coin to the set to be given out
            denomination[coin] -= 1  # One less coin available of that denomination
    
    if sum(change) < amount:  # If the program has been unable to make up the amount, raise an error
        return error_string

    print("Your change is:", change)  # Print the user's change


# Begin User Interaction
print("Welcome to the Python Vending Machine. Available products:")
for x, y in products.items():  # Display available products to user
    print(x, y)
    
choosing = True
while choosing:
    print("Select a product (enter number): ")
    name = input()
    if name.isdigit():  # If user input is a number
        name = int(name)  # Make sure the number is an actual int
        if name in products.keys():  # If that int corresponds to a product key
            choosing = False  # Come out of the loop, the user has successfully chosen a product
        else:
            # Else the user has picked a number that doesn't correspond to a product
            # The user will be prompted to enter another number
            print(error_input_string)
    else:  # Else the user hasn't entered a number
        print(error_input_string)
      
amount_outstanding = list(products[name].values())[0]  # This gets the value (price) as an int
product_string = list(products[name].keys())[0]

print("You have chosen:", product_string)  # Tell the user what they have just chosen

while amount_outstanding > 0:
    print("The amount outstanding is", amount_outstanding)    
    print("Please insert change (You can enter 200, 100, 50, 20, 10, 5, 2, or 1 representing coin denominations): ")
    inserted = int(input())
    if inserted in eur:
        amount_outstanding -= inserted  # Deduct the amount the user has entered from the amount outstanding
    else:
        print("Sorry, the coin you just tried to insert doesn't exist. Please enter an actual coin...")
         
    print("You have just inserted a", inserted, "cents coin")

if amount_outstanding < 0:
    get_change(-amount_outstanding)
else:
    print("No change! Enjoy your beverage!")