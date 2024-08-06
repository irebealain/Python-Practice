def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "unsupported unit"

def validate_and_execute(days_to_unit_dictionary):
    try:
        user_input_number = int(days_to_unit_dictionary["days"])
        
        # we want to do conversion only for positive integers
        if user_input_number > 0:
            calculated_values = days_to_units(user_input_number, days_to_unit_dictionary["units"])
            print(calculated_values)
        elif user_input_number == 0:
            print("You entered a 0, please enter a valid positive number")
    except ValueError:
        print("Your input is not a valid number. Don't ruin my program!")