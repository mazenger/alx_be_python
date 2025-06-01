#!/usr/bin/env python3
"""
Daily Reminder
This script provides customized task reminders based on priority and time sensitivity.
"""

# Get user input for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Process the task based on priority and time sensitivity
match priority.lower():
    case "high":
        if time_bound.lower() == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Please complete it as soon as possible.")
    case "medium":
        if time_bound.lower() == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires attention today.")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Plan to complete it soon.")
    case "low":
        if time_bound.lower() == "yes":
            print(f"Reminder: '{task}' is a low priority task that needs to be done today.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level. Please use high, medium, or low.") 