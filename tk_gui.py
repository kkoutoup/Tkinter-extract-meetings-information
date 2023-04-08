# Python modules
from tkinter import *
from tkinter import ttk, font
from tkcalendar import Calendar, DateEntry
import re

# local modules
import config

# identify which button was pressed
def return_pressed_button(event):
    global event_target
    event_target = str(event.widget)
    return event_target

# check if dates are in the right order
def check_dates_order():
    if config.button_pressed == '.!frame5.!button':
        if config.calendar_from_date > config.calendar_to_date:
            config.dates_in_right_order = False
            button_label_text.set("Dates are in the wrong order")
        else:
            button_label_text.set(f"Fetching results for {config.calendar_from_date} to {config.calendar_to_date}. You may now close this window.")
            config.dates_in_right_order = True

# set calendar_from_date, calendar_to_date and button_pressed in config.py
def return_user_input():
    config.calendar_from_date = cal_from_date.get_date()
    config.calendar_to_date = cal_to_date.get_date()
    config.button_pressed = str(event_target)

# validate user input and return values for api request
# def validate_date_inputs():
#     if str(event_target) == '.!frame.!button':
#         # target user input
#         inputs_combined = f"{from_date.get()}-{to_date.get()}"
#         # check for valid input
#         date_regex = re.compile(r'\d{2}\/\d{2}\/\d{4}\-\d{2}\/\d{2}\/\d{4}')
#         check = re.match(date_regex, inputs_combined)
#         if check is None: # notify user if no match
#             label_text.set("Please enter a valid date range")
#         else:
#             label_text.set(f"Fetching results for {check.group()}. You can now close this window.")
#             return check.group()
#     else:
#         user_choice = str(user_radio_choice.get())
#         if user_choice == '':
#             label_text.set(f"Please select between today's and this week's meetings")
#         else:
#             label_text.set(f"Fetching {str(user_radio_choice.get())}'s meetings information. You can now close this window.")
#         return user_choice

# ROOT WINDOW
# root window
root = Tk()
root.title("Committee meetings information")

# root window size
root.resizable(FALSE, FALSE) # prevent window from resizing
root_width = 500
root_height = 350
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{root_width}x{root_height}+{int(((screen_width)-root_width)/2)}+{int(((screen_height)-root_height)/2)}") # center window on screen

# STYLES
# style - fonts
instructions_font = font.Font(family ='TkDefaultFont', size = 12)
widget_font = font.Font(family ='TkDefaultFont', size = 11)
message_font = font.Font(family ='TkDefaultFont', size = 12, weight ='bold')

# date picker instructions frame
date_picker_instructions_frame = ttk.Frame(root, padding = "5 10 0 0")
date_picker_instructions_frame.pack(anchor = N, side = TOP, fill = X)
# instruction label one
instuctions_label_one = ttk.Label(date_picker_instructions_frame, text = "Select a date range", font = instructions_font)
instuctions_label_one.pack(side = LEFT)

# parent frame for 'from date' label and 'calendar for' frame
parent_frame = ttk.Frame(root, padding = 10)
parent_frame.pack(anchor = N, side = TOP, fill = X)
# 'from date' label
from_date_label = ttk.Label(parent_frame, text = "From:", font = widget_font, padding = "0 0 5 0")
from_date_label.pack(side = LEFT)
# calendar 'from date' frame
calendar_from_frame = ttk.Frame(parent_frame)
calendar_from_frame.pack(side = LEFT)
# calendar 'from date' picker
cal_from_date = DateEntry(calendar_from_frame, selectmode = "day", font = widget_font)
cal_from_date.pack()
# cal_from_date.bind("<<DateEntrySelected>>", get_from_date) - test which start date was selected

# parent for 'to date' label and 'calendar to' frame
parent_two_frame = ttk.Frame(root, padding = 10)
parent_two_frame.pack(anchor = N, side = TOP, fill = X)
# 'to date' label
to_date_label = ttk.Label(parent_two_frame, text = "To:", font = widget_font, padding = "0 0 22 0")
to_date_label.pack(side = LEFT)
# calendar 'to date' frame
calendar_to_frame = ttk.Frame(parent_two_frame)
calendar_to_frame.pack(side = LEFT)
# caledar 'to date' picker
cal_to_date = DateEntry(calendar_to_frame, selectmode = "day", font = widget_font)
cal_to_date.pack()
# cal_to_date.bind("<<DateEntrySelected>>", get_to_date) - test which end date was selected

# button label frame and label
button_label_frame = ttk.Frame(root)
button_label_frame.pack(anchor = N, side = TOP, fill = X)
button_label_text = StringVar()
button_label = ttk.Label(button_label_frame, textvariable = button_label_text, font = widget_font, wraplength = root_width)
button_label.pack(side = LEFT)

# calendar button frame
calendar_button_frame = ttk.Frame(root, height = 10)
calendar_button_frame.pack(anchor = N, side = LEFT)
# button
calendar_fetch_button = ttk.Button(calendar_button_frame, text = "Fetch results", command = lambda: [return_user_input(), check_dates_order()])
calendar_fetch_button.config(width = 20, padding = "2 2 2 2")
calendar_fetch_button.pack(anchor = N, side = LEFT)

# run window loop
root.bind("<Button>", return_pressed_button) # monitor which button is getting clicked
root.mainloop()