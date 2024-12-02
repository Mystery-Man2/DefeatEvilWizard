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