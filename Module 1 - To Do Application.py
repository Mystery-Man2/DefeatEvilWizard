# Thad Howell's 'To-Do' Application ... Module 1 assignment 

print("\nWelcome to 'Thad's To-Do list' ✅")
print("Let's get productive!")

tasks = []

def menu ():
    print("-"*60)
    print("                   M A I N  M E N U")
    print("\n[1] Add Task")
    print("\n[2] View Task")
    print("\n[3] Delete Task")
    print("\n[0] Exit the program")
    print("-"*60)

def display_tasks():
    for index,item in enumerate(tasks, start=1):
        print(f"{index} - {item}")

option = True
while option != 0:
    try:
        menu()
        option = int(input("\nPlease make your selection: "))
    except:
        print("\nThis is an invalid choice, please enter a valid selection.")
    else:
        if option == 1:
            add_task = str(input("\nWhat task would you like to add to your To-Do list? : "))
            tasks.append(add_task)
            print(f"\n'{add_task}' has been added to your To-Do list!")
        elif option == 2:
            if not tasks:
                print("\nThere are no tasks to display, please add a task. ")
            else:
                print("-"*60)
                print("\n                   Here are your tasks: ")
                print()
                display_tasks()
        elif option == 3:
            if not tasks:
                print("\nThere are no tasks to delete, please add a task.")
            else:
                print()
                if_clear = str(input("\nWould you like to delete EVERY task and clear the list? (y/n): "))
            if if_clear == "y":
                tasks.clear()
                print("\nAll tasks have been deleted!")
            elif if_clear == "n":
                print("\nHere are your tasks: ")
                print()
                display_tasks()
                try:
                    delete_task = int(input("\nPlease enter the number of the task you would like to delete. : "))
                except ValueError:
                    print("\nPlease enter the number of the task you would like to delete (1, 2, 3, etc.)") 
                else:
                    try:
                        del tasks[delete_task -1]
                        print(f"\nTask '{delete_task}' has been removed.")
                    except IndexError:
                        print("\nThe number you entered was not attached to a task.")
        elif option == 0:
            pass 
        else:
            print("\nThat is not a recognized input... please close the application and try again.")
            print("\nPlease only enter the number of the selection you would like to choose (1, 2, 3, or 0) ")
    finally:
        pass  
else:    
    print("\nThank you for using 'Thad's To-Do list' ✅")
    print("\nHave a productive day!")
    print()
    exit()


# ToDoApplication

Module-1-To-Do-Assignment: This is my submission for the assignment at the end of Module 1.

This is a fairly simple application to use.

Upon opening the application, you will be met with a menu and the option to enter a selection.

The menu only has 4 options: "1" to add a task. "2" to view all tasks. "3" to delete a task(s). "0" to end the program.

** If you enter a word, sentence, or number that is not listed as an option on the main menu, the program will tell you to only enter the number for the selection you would like to execute.

After selecting "1" from the main menu, it will prompt you to enter a task, which you will need to type out.

The program will give you a confirmation that your task has been added to your to-do list and then it will bring you back to the menu and ask you for another selection. After selecting "2" from the main menu, it will show you all your tasks, listed in order starting with "1".

After selecting "3" from the main menu, you will be presented with a choice to either clear the list entirely by entering "y" or to just delete 1 task by entering "n".

If there are no tasks in your list, the application will not display the choice and will tell you that the list is empty and will instruct you to add a task before trying to delete one. If you select "y", the application will clear the list and delete ALL tasks, tell you it has done so, and then bring you back to the main menu. If you select "n", the application will ask you to enter the number of the task you wish to delete. Once you input the number of the task you wish to delete, the application will delete the task, tell you it has done so, and then return you to the main menu. If you attempt to type out the task while trying to delete it instead of using the number, or type in a number that is not attached to a task, the application will tell you that you must enter the number attached to the task to delete it and bring you back to the main menu. After selecting "0", the application will display the exit message and close.