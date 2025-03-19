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
    taskTracking = []
    completedTasks = []
    taskNumber = []

    CATEGORY = { 'Completed' , 'Incomplete' }

    while True: 
        print("================")
        print("- Task Manager -")
        print("================")

        print("1. Add a task.")
        print("2. Add a step for a task.")
        print("3. Mark task as completed.")
        print("4. View all tasks.")
        print("5. Remove a task.")
        print("6. Display total number of tasks.")
        print("7. Quit")
        option = int(input("Please place in the option you'd like to choose: "))

        # If statement for option one - All the choices will be if statements. 
        if option == 1: 
            print("\n")
            tasks = input("Please type the task you'd like to add: ") 
            taskNumber.append(tasks)
            taskTracking.append(tasks)
            print("Task successfully added into the list!")

        elif option == 2:
            print(taskTracking)
            stepsQuestion = input("Please select the task you would like to place steps for: ")
            if stepsQuestion in taskTracking: 
                steps = input("Please input the steps you'd like to add: ") 
                stepsForTask.append(steps)
                print("Steps added successfully! Good luck!")
            else: 
                print("I believe you have misunderstood! Please try again!")
                return

        elif option == 3: 
            choice = input("Would you like to add this task to completed? Please enter yes if yes, enter no if no: ")
            if choice == True:
                print(taskTracking)
                taskQuestion = input("What task would you like to add?: ")
                completedTasks.append(taskQuestion)
                print("Good luck with the rest!")
            else: 
                print("Good luck with your task!")
        elif option == 4: 
            print("These are your tasks: {}".format(taskTracking))
        elif option == 5: 
            print(taskTracking)
            delete = input("Please select the task you would like to delete: ") 
            delete = taskTracking.popitem()
                
        elif option == 6: 
            print("This is a test.")
        elif option == 7: 
            print("Thank you for using this program.")
            return
        else: 
            print("Please retry your entry!")
            return
        
        
            
 






if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit() # Control C 



