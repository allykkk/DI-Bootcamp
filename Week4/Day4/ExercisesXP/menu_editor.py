from menu_item import MenuManager, MenuItem

'''
Create a file called menu_editor.py , which will have the following functions:
    1. show_user_menu() - this function should display the program menu (not the restaurant menu!), and ask the user to :
            View an Item (V)
            Add an Item (A)
            Delete an Item (D)
            Update an Item (U)
            Show the Menu (S)
            Call the appropriate function that matches the user’s input.

    2. add_item_to_menu() - this function should ask the user to input the item’s name and price. This function will not interact with the menu itself, but simply create a MenuItem object and call the appropriate function from the MenuItem object.
        If the item was added successfully print a message which states: item was added successfully.

    3. remove_item_from_menu()- this function should ask the user to input the name of the item they want to remove from the restaurant’s menu. This function will not interact with the menu itself, but simply create a MenuItem object and call the appropriate function from the MenuItem object.
        If the item was deleted successfully – print a message to let the user know this was completed.
        If not – print a message which states that there was an error.

    4. update_item_from_menu()- this function should ask the user to input the name and price of the item they want to update from the restaurant’s menu, as well as to input the name and price they want to change them with. This function will not interact with the menu itself, but simply create a MenuItem object and call the appropriate function from the MenuItem object.
        If the item was updated successfully – print a message to let the user know this was completed.
        If not – print a message which states that there was an error.

    5. show_restaurant_menu() - print the restaurant’s menu.

When the user chooses to exit the program, display the restaurant menu and exit the program.
'''


def show_user_menu():
    while True:
        print("Program Menu:")
        print("V - View an Item")
        print("A - Add an Item")
        print("D - Delete an Item")
        print("U - Update an Item")
        print("S - Show the Menu")
        print("E - Exit")

        choice = input("Enter your choice: ").upper()

        if choice == "V":
            view_item()
        elif choice == "A":
            add_item_to_menu()
        elif choice == "D":
            remove_item_from_menu()
        elif choice == "U":
            update_item_from_menu()
        elif choice == "S":
            show_restaurant_menu()
        elif choice == "E":
            show_restaurant_menu()
            break
        else:
            print("Invalid choice. Please try again.")


def view_item():
    name = input("Enter the item's name: ")
    item = MenuManager.get_by_name(name)

    if item:
        print("Item Details:")
        print(f"Name: {item.name}")
        print(f"Price: ${item.price}")
    else:
        print("Item not found.")


def add_item_to_menu():
    name = input("Enter the item's name: ")
    price = int(input("Enter the item's price: "))

    item = MenuItem(name, price)
    item.save()

    print("Item was added successfully.")


def remove_item_from_menu():
    name = input("Enter the name of the item to remove: ")

    item = MenuManager.get_by_name(name)

    if item:
        item.delete()
        print("Item was deleted successfully.")
    else:
        print("Item not found.")


def update_item_from_menu():
    name = input("Enter the name of the item to update: ")
    new_name = input("Enter the new name: ")
    new_price = int(input("Enter the new price: "))

    item = MenuManager.get_by_name(name)

    if item:
        item.update(new_name, new_price)
        print("Item was updated successfully.")
    else:
        print("Item not found.")


def show_restaurant_menu():
    items = MenuManager.all_items()
    if items:
        print("Restaurant Menu:")
        for item in items:
            print(item)
    else:
        print("No items found in the menu.")


if __name__ == "__main__":
    show_user_menu()
