# # """
# # Create a simplified Python script that uses conditional statements,
# # Match Case, and loops to remind the user about a single,
# # priority task for the day based on time sensitivity.
# # ggghh
# # Algorithm
# # #step 1
# #  Ask the useer to input task description and save it as task
# #  Ask for priority task and save it as priority task
# #  Ask if the task have a time bounce and save it to time_bounce variable have two answer (yes/no)
# #  #step 2
# #  Use a Match Case statement to react differently based on the task’s priority.
# # Within the Match Case or after, use an if statement to modify the reminder if the task is time-bound.
# #
# # #step 3
# # Print a reminder about the task that includes its priority level and whether immediate action is required based on time sensitivity.
# # A message should be ‘that requires immediate attention today!’
# # PSEUDOCODE
# # task = input("Enter task description: ")
# #
# # priority = ("Priority (high/medium/low):").lower()
# # time_bounce = ("Is it time-bound? (yes/no):").lower()
# # match priority:
# #     case "high":
# #       print("Reminder: 'Finish project report' is a high priority task that requires immediate attention today!")
# #     case "medium":
# #       print("You can work on this later since it not highly prioritized.")
# #     case "low":
# #     print("You can do this on your free time since is low priority.")"
# #     if time_bounce == "no"
# #       print("Note: 'Read a book' is a low priority task. Consider completing it when you have free time.")
# #
# #
# #
# #
# # """
# # Step 1: Input collection
# task = input("Enter your task:")
# priority = input("Priority (high/medium/low):").lower()
# time_bounce = input("Is it time-bound? (yes/no):").lower()
#
# # Step 2: Match Case on priority
# match priority:
#
#     case "high":
#         if time_bounce == "yes":
#             print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
#
#         print(f" '{task}' is a high priority task!")
#
#     case "medium":
#         print(f"Reminder: '{task}' is a medium priority task. ")
#     case "low":
#         print(f"Reminder: '{task}' is a low priority task. You can do this in your free time.")
#
#
# # if time_bounce == "no":
# #     print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
#
# if time_bounce == "yes":
#     print(f"Reminder: {task} is a high priority task that requires immediate attention today!")

# Step 1: Prompt user for input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Step 2: Match case for priority
match priority:
    case "high":
        print(f"Reminder: '{task}' is a high priority task", end="")
        if time_bound == "yes":
            print(" that requires immediate attention today!")
        else:
            print(". Try to address it as soon as possible.")
    case "medium":
        print(f"Reminder: '{task}' is a medium priority task. You can work on it later.")
    case "low":
        print(f"Reminder: '{task}' is a low priority task.", end="")
        if time_bound == "yes":
            print(" It still needs to be done today.")
        else:
            print(" Consider completing it when you have free time.")
    case _:
        print("Invalid priority. Please enter high, medium, or low.")

