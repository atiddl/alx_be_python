# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Check if the task is time-bound
if time_bound == "yes":
    print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
else:
    # Use Match Case to determine suggestion based on priority for non-time-bound tasks
    match priority:
        case "high":
            suggestion = "It's important to complete it as soon as possible."
        case "medium":
            suggestion = "Try to complete it soon."
        case "low":
            suggestion = "Consider completing it when you have free time."
        case _:
            suggestion = "Please check the priority level."
    print(f"Note: '{task}' is a {priority} priority task. {suggestion}")