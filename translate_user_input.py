# Python modules
from datetime import datetime, date
import time

# local modules
from helper_functions import calculate_days_of_the_week
from tk_gui import *
from config import selected_dates

def translate_user_input():
    # possible scenarios: 'today', 'week', date range
    user_input = validate_date_inputs()
    # today
    if user_input == 'today':
        todays_date = date.today()
        time.sleep(1) # in some cases 'today' was returning 'None'. Pausing script to avoid that.
        return f"{todays_date}/{todays_date}" # api endpoint needs two values (from/to) - in this case they match
    elif user_input == 'week':
       result = calculate_days_of_the_week()
       return result
    else:
        date_range = user_input.split('-')
        date_range_array = [datetime.strptime(item,'%d/%m/%Y').strftime('%Y-%m-%d') for item in date_range] # string to datetime object and formatted with strftime
        return'/'.join(date_range_array)
