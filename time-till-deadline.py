from datetime import datetime
# Let the user enter the goal and the deadline
user_input = input("Enter your goal with a deadline separated by a colon:\n")
input_list = user_input.split(":")
# Gets the two inputs
goal = input_list[0]
deadline = input_list[1]
# Convert the user input into a date from a string
deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
# The day today
date_today = datetime.today()
# Calculation of the gap between the deadline and today's date
date_till = deadline_date - date_today
# Then print the results in the console or the terminal.
# The remaining days are calculated into hours and made an integer
remaining_hours = int(date_till.total_seconds() / 60 / 60)
print(f"Dear user, your goal to {goal} remaining {remaining_hours} hours")