# This script will ask the user for a single task, its priority level, 
# and if it is time-sensitive. The program will then provide a customized 
# reminder for that task, demonstrating control flow and loops without 
# relying on data structures to store multiple tasks.

task = input("Enter your task: ")

priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"'{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"'{task}' is a high priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "no":
            print(f"'{task}' is a medium priority task. Consider completing it when you have free time.")
        else:
            print(f"'{task}' is a medium priority task that requires immediate attention today!")
    case "low":
        if time_bound == "no":
            print(f"'{task}' is a low priority task. Consider completing it when you have free time.")
        else:
            print(f"'{task}' is a low priority task that requires immediate attention today!")
