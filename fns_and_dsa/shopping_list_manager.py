# Python script named shopping_list_manager.py that implements a simple interface 
# for managing a shopping list. This task focuses on using lists to store and 
# manipulate data dynamically.



def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            shopping_list.append(input("Enter the items to add: "))
            print(shopping_list, "Item Added Succsefull")
            # Prompt for and add an item
            pass
        elif choice == '2':
            # Prompt for and remove an item
            for i in range(len(shopping_list)):
                print(i, shopping_list[i])
            remove = input("Enter Item name to be removed")
            if remove in shopping_list:
                shopping_list.remove(remove)
            pass
        elif choice == '3':
            for i in shopping_list:
                print(i)
            # Display the shopping list
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
