calculation_to_units=24
name_of_units="hours"

def days_to_units(num_of_days):
        return f"{num_of_days} days are {num_of_days*calculation_to_units} {name_of_units}"

def vaidate_and_execute():
    try:
        user_input_number=int(user_input)
        if user_input_number > 0:
            calculated_value= days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            return "zero cannot be caculated"
        else:
            print("entered a negative number")

    except ValueError:
        print("input is not valid number")


user_input=input("Hey, enter the number of days, i will convert it to hours! \n")
vaidate_and_execute()