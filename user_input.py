# Python modules
import re
from datetime import datetime, date, timedelta

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

def translate_user_input():
    # possible scenarios: 'today', 'week', date range
    user_input = get_user_input()
    # today
    if user_input == 'today':
        todays_date = date.today()
        return f"{todays_date}/{todays_date}" # api endpoint needs two values (from/to) - in this case they match
    elif user_input == 'week':
        # calculate date range => start of week - today's date
        today = date.today()
        today_as_weekday = today.weekday()
        # start of week
        start_of_week = today - timedelta(days=today_as_weekday)
        # end of week = start of week + 6 days
        end_of_week = start_of_week + timedelta(days=6)
        return f"{start_of_week}/{end_of_week}" # corresponding to from/to values in api endpoint
    else:
        date_range = user_input.split('-')
        date_range_array = [datetime.strptime(item,'%d/%m/%Y').strftime('%Y-%m-%d') for item in date_range] # string to datetime object and formatted with strftime
        return'/'.join(date_range_array)
