task = input("Enter your task: ").lower()
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task. that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task. that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task. that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
        
