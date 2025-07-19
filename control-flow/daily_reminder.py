# This script will ask the user for a single task, its priority level, 
# and if it is time-sensitive. The program will then provide a customized 
# reminder for that task, demonstrating control flow and loops without 
# relying on data structures to store multiple tasks.

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        print(f"'{task}' is a high priority task",end="")
    case "medium":
        print(f"'{task}' is a medium priority task",end="")
    case "low":
        print(f"'{task}' is a low priority task",end="")

if time_bound == "yes":
    print(" that requires immediate attention today!")
else:
    print(". Consider completing it when you have free time.")
