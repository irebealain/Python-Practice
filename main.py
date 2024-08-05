calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"


def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            calculated_values = days_to_units(user_input_number)
            print(calculated_values)
        elif user_input_number == 0:
            print("You entered a 0, please enter a valid positive")
    except ValueError:
        print("Your input is not a valid number. Don't ruin my program!")
user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter a number of days and I will convert it to hours!\n")
    for num_of_days_element in user_input.split(","):
        validate_and_execute()