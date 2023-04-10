# Python modules
from datetime import datetime, date

# local modules
from helper_functions import calculate_days_of_the_week
from tk_gui import *
import config
from logging_setup import *

def translate_user_input():
    if config.user_radiobutton_choice == 'calendar':
        if config.dates_in_right_order:
            logging.info((f"Fetched results from {dt.strftime(dt.fromisoformat(str(config.calendar_from_date)), '%d/%m/%Y')} to {dt.strftime(dt.fromisoformat(str(config.calendar_to_date)), '%d/%m/%Y')}\n"))
            return [config.calendar_from_date, config.calendar_to_date]
    if config.user_radiobutton_choice == 'radio':
        if config.today_week_choice == 'today':
            todays_date = date.today()
            logging.info(f"Fetched meetings information for {todays_date}\n")
            return [todays_date, todays_date]
        else:
            result = calculate_days_of_the_week()
            logging.info(f"Fetched this week's meetings information\n")
            return result.split("/")
