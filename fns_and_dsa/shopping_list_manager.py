"""
program to add , remove and display list items
display option to user to choos what the want to do
they can add  items in the list
they can  remove items from the list
they can print the list content
to care with the invalid choice, we use if statement
"""



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
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue


        if choice == 1:
            # Prompt for and add an item
            item = input("Enter item name: ")
            shopping_list.append(item)
            print(f"{item} added to shopping list.")
            pass
        elif choice == 2:
            # Prompt for and remove an item
            item = input("Enter item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed successfully.4")


            pass
        elif choice == 3:
            # Display the shopping list
            print("This is your shopping list:")
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")
            # print("This is your shopping list:")
            # for item in shopping_list:
            #     print(item)

            pass

        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()