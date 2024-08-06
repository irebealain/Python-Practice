from helper import validate_and_execute

user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter a number of days and the conversion unit (hours/minutes) separated by ':'\n")
    days_and_unit = user_input.split(":")
    days_to_unit_dictionary = {"days": days_and_unit[0], "units": days_and_unit[1]}
    print(days_to_unit_dictionary)
    validate_and_execute(days_to_unit_dictionary)

