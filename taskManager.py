"""
You will create a multi-function Python Task Manager program. This program will allow the user to:
Add a Task
Add a Step to a Task
Mark Step as Completed
View All Tasks
Remove a Task
Display Total Number of Tasks
Quit
Each menu option will be created in it's own function which is called when that menu option is selected. Once again, Python dictionaries are your friend when it comes to storing data.

Taken from the Google Classroom
"""

import sys



def main():

    print("################################") 
    print("################################")
    print("##  Welcome to Task Manager:  ##")
    print("## The place to manage tasks! ##")
    print("################################") 
    print("################################")


    stepsForTask = [] 
    completedTasks = []
    taskNumber = []

    CATEGORY = { 'Completed' , 'Incomplete' }
    # TASKS = ''

    while True: 
        print("\n")
        print("================")
        print("- Task Manager -")
        print("================")

        print("1. Add a task.")
        print("2. Add a step for a task.")
        print("3. Mark step as completed.")
        print("4. View all tasks.")
        print("5. Remove a task.")
        print("6. Display total number of tasks.")
        print("7. Quit")
        option = int(input("Please place in the option you'd like to choose: "))

        if option == 1: 
            tasks = input("Please type the task you'd like to add: ") 
        elif option == 2:
            steps = input("Please add the steps for the task: ")
        elif option == 3: 
            choice = input("Would you like to add this task to completed? Please enter yes if yes, enter no if no: ")
            if choice == y:
                taskQuestion = input("What task would you like to add?: ")
                completedTasks.append(taskQuestion)
            else:
                break

        
            
 






if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit() # Control C 



