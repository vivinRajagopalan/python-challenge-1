# Initialize the menu items
menu_items = [
    {"Item name": "Dosa", "Price": 2.5},
    {"Item name": "Idly", "Price": 1.3},
    {"Item name": "Vada", "Price": 1.7},
    {"Item name": "Sambhar", "Price": 1.0},
]

itemName = "Item name"
itemPrice = "Price"
qty = "Quantity"

# An empty list to store the customer's order
customer_order = []

# Function to print menu
def print_menu():
    print("Menu:")
    for index, item in enumerate(menu_items):
        print(f"{index + 1}. {item['Item name']} - ${item['Price']}")

# Function to take an order
def take_order():
    print_menu()
    menu_selection = input("Please enter the number of the item you'd like to order: ")

    # Validate the menu_selection input
    if menu_selection.isdigit():
        menu_selection = int(menu_selection)
        if 1 <= menu_selection <= len(menu_items):
            selected_item = menu_items[menu_selection - 1] 
            item_name = selected_item[itemName]
            item_price = selected_item[itemPrice]

            # Ask the customer for the quantity input
            quantity_input = input(f"How many {item_name}s would you like to order? (Default is 1 if input is invalid): ")

            # Validate the quantity input
            if quantity_input.isdigit():
                quantity = int(quantity_input)
            else:
                quantity = 1

            # Add the order to the customer_order list
            customer_order.append({
                "Item name": item_name,
                "Price": item_price,
                "Quantity": quantity
            })

            print("Current order:")
            for order in customer_order:
                print(order)
        else:
            print("Error: Invalid selection. Please enter a number corresponding to the menu items.")
    else:
        print("Error: Invalid input. Please enter a number.")

# Continuous loop to ask if the customer wants to continue ordering
place_order = True

while place_order:
    take_order()
    while True:
        keep_ordering = input("Would you like to keep ordering? (y/n): ").lower()
        match keep_ordering:
            case 'y':
                place_order = True
                break
            case 'n':
                place_order = False
                print("Thank you for your order.")
                break
            case _:
                print("Invalid input. Please type 'y' for yes or 'n' for no.")

# Determine the maximum length of the item names
max_length = max(len(order[itemName]) for order in customer_order)

# Create the header and dash separator with string multiplication
six = 6
eight = 8
header = f"{'Item name'.ljust(max_length)} | Price  | Quantity"
dash_separator = f"{'-' * max_length} | {'-' * six} | {'-' * eight}"

# Print the formatted bill
print("\nReceipt:")
print(header)
print(dash_separator)
for order in customer_order:
    item_name = order[itemName]
    price = order[itemPrice]
    quantity = order[qty]
    space_padded_item_name = item_name.ljust(max_length)
    print(f"{space_padded_item_name} | ${price:.2f} | {quantity}")

# Find the total price of the order using list comprehension
total_price = sum(order[itemPrice] * order[qty] for order in customer_order)

# Display the total price
print(f"\nTotal Price: ${total_price:.2f}")