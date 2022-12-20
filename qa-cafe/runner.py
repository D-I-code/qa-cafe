from CafeConnector import *

def cafe_menu():
    print("""
    -------- Welcome to QA Cafe --------
    What can we help you with?
    1) Add Order
    2) Read Order By ID
    3) Read All Orders
    4) Update Order by ID
    5) Delete Order by ID
    6) Delete All Orders
    """)


cafe_menu()
usr_choice = input("Please select from the menu: ")

if usr_choice == "1":
    print("You chose 'Add Order.' ")
    drink = input("Enter drink of choice: ")
    name = input("Enter your name: ")
    size = input("Enter size of drink (small, medium,large): ")
    extras = input("Enter drink extras (milk, cream, choc etc.): ")
    add_order(name, drink, size, extras, 5.0)
    print(f"Order successful: {drink}, {name}, {size}, {extras}, price: £5")

elif usr_choice == "2":
    print("You chose 'Read Order By ID' ")
    read_order = input("Please input an order ID: ")
    print("You chose order: " + read_order)

elif usr_choice == "3":
    print("You chose 'Read All Orders' ")
    orders = get_all_orders()
    print(f"Here are all orders: {str(orders)}")

elif usr_choice == "4":
    print("You chose 'Update Order by ID' ")


elif usr_choice == "5":
    print("You chose 'Delete Order by ID' ")
    del_order = input("Please enter the order ID you would like to delete: ")
    print("Order " + del_order + " deleted!")

elif usr_choice == "6":
    print("You chose 'Delete All Orders' ")
    del_all = input("Are you sure you want to delete all orders? ")
    if del_all == "Yes":
        print("You have successfully deleted all orders!")

    elif del_all == "No":
        print("Would you like to continue")

    else:
        print("Please enter Yes or No.")

else:
    print("Please enter a valid input!")



# while True:
#     usr_input = input("Would you like any extras? ")
#
#     if usr_input == "Yes":
#         print("You have added: " + usr_input)
#         break
#     elif usr_input == "No":
#         print("No added extras.")
#         break
#     else:
#         print("Please enter Yes or No.")
#         break
