calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"

user_input = input("Hey user, enter a number of days and I will convert it to hours!\n")
def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        calculated_values = days_to_units(user_input_number)
        print(calculated_values)
    
    else:
        print("Your input is not a valid number. Don't ruin my program!")
validate_and_execute()