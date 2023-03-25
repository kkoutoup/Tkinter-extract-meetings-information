# Python modules
import re

def get_user_input():
    print("Please choose a valid timespan\n 'today' for the day's meetings\n 'week' for this week's meetings \n any other timespan in the following format: dd/mm/yyyy-dd/mm/yyyy")
    user_input = input()
    # check for 'today' or 'week'
    accepted_values = ['today', 'week']
    # check for other formats
    date_regex = re.compile(r'\d{2}\/\d{2}\/\d{4}\-\d{2}\/\d{2}\/\d{4}')
    date_match = re.match(date_regex, user_input)
    if user_input not in accepted_values and date_match is None:
        get_user_input() # ask for input again
    else:
        if user_input in accepted_values:
            return user_input
        else:
            return date_match.group()

