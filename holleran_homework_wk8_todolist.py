"""
Python 1 - DAT-119 - Spring 2019
Joe Holleran
03/27/2019
In-Class Assignment - Week 8 - To-Do List
"""
# Lists for to-do and finished or completed items
to_do_list = []
finish_list = []

# Welcome user to the to-do list application
print("--------------------------------------")
print("Welcome to the to-do list application!", "\n")

# Main function to be called upon when user wants to modify the to-do list
def main():
    
    # Start while loop
    while True:
        
        # Give the user the choices to modify the to-do list
        print("   Main Menu   ")
        print()
        print("1. View the items on your to-do list")
        print("2. View the items you have finished")
        print("3. Add an item to the to-do list")
        print("4. Mark a to-do list item as completed")
        print("5. Exit the to-to list application")
        
        # Take in input from user to modify the list
        user_select = int(input("Please choose one of the options above: "))
        
        # If statements to call functions to modify the list
        if user_select < 1 or user_select > 5:
            user_select = int(input("Please choose one of the options above: "))
        elif user_select == 1:
            todo_list()
        elif user_select == 2:
            finished_list()
        elif user_select == 3:
            add_list()
        elif user_select == 4:
            completed_list()
        elif user_select == 5:
            break
        
        go_to_main = input("Press enter to continue to the 'Main Menu'... ")
        print()
        if go_to_main == " ":
            main()
              
    # The loop is broken if user enters 5 and then is thanked for using program           
    print()
    print("Thanks for using the to-do list application!")

# To-do list function to print the to-do list
def todo_list():
    
    print("----------------")       
    print("Your to-do list:", "\n")
    
    # Print to-do list if there are items in the to-do list
    if len(to_do_list) != 0:
    
        for item in range(len(to_do_list)):
            print(item + 1, to_do_list[item], sep=". ")
    
        print()
        
    # Tell the user the to-do list is empty
    else:
        print("Your to-do list is empty.", "\n")

# Finished list function to print the finished list  
def finished_list():
    
    print("--------------------------------------")
    print("These are the items you have finished:", "\n")
    
    # Print finished list if there are items in the finished list
    if len(finish_list) != 0:
        
        # Print the finished list
        for item in range(len(finish_list)):
            print(item + 1, finish_list[item], sep=". ")
    
        print()
    # Tell the user the finished list is empty
    else:
        print("Your finished list is empty.", "\n")

# Function to add to-do list tasks to the to-do list
def add_list():
    
    print("--------------------------------------")
    print("Please add an item to your to-do list:", "\n")
    
    # Take in to-do list item from user
    add_item = input(" ")
    
    # Add the item to the to-do list
    to_do_list.append(add_item)
    print()
    

# Function to remove completed items from the to-do list
def completed_list():
    
    print("--------------------------------------------")
    print("Your to-do list:", "\n")
    
    # Print to-do list and ask the user to mark an item as finished
    if len(to_do_list) != 0:

        for item in range(len(to_do_list)):
            print(item + 1, to_do_list[item], sep=". ")
        # Ask user what items they want to remove
        item_complete = int(input("Enter finished to-do list item number: ")) - 1
    
        # Add item to the finished list
        finish_list.append(to_do_list[item_complete])
    
        # Remove item from the to-do list
        to_do_list.remove(to_do_list[item_complete])
    
        print()
    # Tell the user the to-do list is empty if there are no items in the to-do list
    else:
        print("Your to-do list is empty.", "\n")
    
        
# Call main function to start the program
main()