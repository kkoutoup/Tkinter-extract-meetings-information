# Python modules
from datetime import datetime, date
import time
import sys

# local modules
from helper_functions import calculate_days_of_the_week
from tk_gui import *
import config

def translate_user_input():
    if config.dates_in_right_order:
        if config.button_pressed == '.!frame5.!button': # if user pressed the calendar fetch button
            return [config.calendar_from_date, config.calendar_to_date]
    # possible scenarios: 'today', 'week', date range
    # user_input = return_user_input()
    # today
    # if user_input == 'today':
    #     todays_date = date.today()
    #     time.sleep(1) # in some cases 'today' was returning 'None'. Pausing script to avoid that.
    #     return f"{todays_date}/{todays_date}" # api endpoint needs two values (from/to) - in this case they match
    # elif user_input == 'week':
    #    result = calculate_days_of_the_week()
    #    return result
    # else:
    #     return user_input
