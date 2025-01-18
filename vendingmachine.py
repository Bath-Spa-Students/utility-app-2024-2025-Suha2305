def welcome_message(): # stores a welcome message 
    print("Hello! Welcome to Suha's vending machine") # welcome message 

def display_menu(): 
    print("\nCATEGORIES:\n--------------------") # prints category header
    for category, items in vending_machine.items(): # its a for loop that iterates over categories
        print(f"Category: {category} |") 
        print("-----------------------------")
        for code, details in items.items():
            print(f"{code}: {details['name']} - {details['price']} DHS | Stock: {details['stock']}")
        print("...") # prints the details of each item

def suggest_item(category): # this function creates a suggestion for each category 
    suggestions = {
        'Drinks': 'Would you like to have some snacks with your drink?',
        'Snacks': 'How about a nice cold drink with your snacks?',
        'Chocolates': 'Need something to wash down that chocolate?',
        'First Aid': 'Stay safe! Need any chocolates or snacks?'
    }
    print(suggestions.get(category, "")) # prints a suggestion based on what the user bought 

def get_change(amount, cost): # this function calculates the return change 
    return amount - cost

def make_purchase(category, code, amount): #This function checks if the item is in stock and if the user has inserted enough money.
    items = vending_machine.get(category, {})
    if code in items: # checks if the given code exists
        item = items[code]
        if item['stock'] == 0: # checks if the item is in stock 
            print("Sorry, this item is out of stock. Would you like to buy something else?")
            return amount # returns reamaining amount 
        while amount < item['price']: # this while loop continues until the user has inserted enough money 
            print("Insufficient funds. Please add more money.")
            added_money = float(input("Insert additional money (DHS): ")) # prompts the user to add more money 
            amount += added_money # adds the amount of money being inserted 
            print(f"Total money available: {amount:.2f} DHS") # prints the total amount money available 
        item['stock'] -= 1 # reduces stock value by 1
        change = get_change(amount, item['price']) # calculates the change to be given 
        print(f"Dispensing {item['name']}")
        print(f"Your change: {change:.2f} DHS")
        suggest_item(category) # suggests a category based on previous purchase 
        return change
    print("Invalid code entered.")
    return amount # returns the change

# Vending Machine Inventory
vending_machine = {
    'Drinks': {
        'A1': {'name': 'Water', 'price': 2.00, 'stock': 12},
        'A2': {'name': 'Vimto Juice', 'price': 4.00, 'stock': 8},
        'A3': {'name': 'Coke', 'price': 4.00, 'stock': 10},
        'A4': {'name': 'Coffee', 'price': 5.00, 'stock': 7},
        'A5': {'name': 'Espresso Shot', 'price': 5.00, 'stock': 5}
    },
    'Snacks': {
        'B1': {'name': 'Cheetos Spicy', 'price': 4.00, 'stock': 6},
        'B2': {'name': 'Corn Puffs', 'price': 3.00, 'stock': 9},
        'B3': {'name': 'Lays', 'price': 2.50, 'stock': 3},
        'B4': {'name': 'Astor', 'price': 3.00, 'stock': 8},
        'B5': {'name': 'Hello Panda', 'price': 5.00, 'stock': 11},
        'B6': {'name': 'Wafers', 'price': 6.00, 'stock': 3}
    },
    'Chocolates': {
        'C1': {'name': 'Dairy Milk', 'price': 4.00, 'stock': 6},
        'C2': {'name': 'KitKat', 'price': 4.00, 'stock': 4},
        'C3': {'name': 'Kinder Bueno', 'price': 6.00, 'stock': 9}
    },
    'First Aid': {
        'D1': {'name': 'Bandaids', 'price': 15.00, 'stock': 8},
        'D2': {'name': 'Panadol', 'price': 30.00, 'stock': 12},
        'D3': {'name': 'Antiseptic Spray', 'price': 20.00, 'stock': 4}
    }
}

# Main Program
welcome_message() # prints a welcome message 
display_menu() # displays the menu 
user_money = float(input("Insert money (DHS): "))
while True: # starts an infinite loop 
    category = input("Enter the category you want to buy from (Drinks, Snacks, Chocolates, First Aid): ").capitalize()
    if category.lower() not in [cat.lower() for cat in vending_machine]: # checks if the entered category is valid 
        print("Invalid category entered. Please try again.")
        continue # if the entered category is invalid the loop starts from the beginning 
    category_key = next(cat for cat in vending_machine if cat.lower() == category.lower()) # finds the category key 
    code = input("Enter the code of the item you want to purchase: ").upper()
    user_money = make_purchase(category_key, code, user_money) # calls the make_purchase function
    print(f"Total money remaining: {user_money:.2f} DHS") # prints the remaining money 
    if user_money <= 0:
        print("You have no more money left.")
        choice = input("Do you want to buy another item? (yes/no): ").lower() # prompts the user whether to buy another item
        if choice == 'yes':
            user_money = float(input("Insert additional money (DHS): ")) # prompts user to add additional money if fund is insufficient
        else:
            break
    else:
        choice = input("Do you want to buy another item? (yes/no): ").lower()
        if choice != 'yes':
            break
print(f"Thank you for using Suha's vending machine! Your remaining change: {user_money:.2f} DHS") # thanks the user for purchase and dispenses remaining money 
