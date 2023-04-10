# Python modules
import tkinter as tk
from tkinter import ttk, font
from tkcalendar import Calendar, DateEntry
from datetime import datetime as dt

# local modules
import config
from logging_setup import *

# GUI CHECKS
# on 'fetch' button click update button_pressed in config.py
def return_pressed_button(event):
    config.button_pressed = str(event.widget)

# on radiobutton click update user_radiobutton_choice in config.py
def set_radio_button_choice():
    config.user_radiobutton_choice = str(user_choice.get())

# check user choice and update user
def check_day_week_choice():
    if not config.today_week_choice is None and config.user_radiobutton_choice == 'radio':
        button_label_text.set(f"Fetching {config.today_week_choice}'s meetings information. You may now close this window.")

# set day/week user choice
def set_day_week_choice():
    config.today_week_choice = str(day_week_choice.get())

# if user clicks on 'fetch' button but hasn't made a choice
def update_user():
    if config.button_pressed == '.!frame7.!button' and config.user_radiobutton_choice == None:
        button_label_text.set("Please select one of the two options")

# on 'fetch' button click check if calendar widget dates are in the right order
def check_dates_order():
    if config.user_radiobutton_choice == 'calendar':
        if config.calendar_from_date > config.calendar_to_date:
            config.dates_in_right_order = False
            button_label_text.set("Dates are in the wrong order")
        else:
            config.dates_in_right_order = True
            button_label_text.set(f"Fetching results from {dt.strftime(dt.fromisoformat(str(config.calendar_from_date)), '%d/%m/%Y')} to {dt.strftime(dt.fromisoformat(str(config.calendar_to_date)), '%d/%m/%Y')}. You may now close this window.")

# on 'fetch' button click set calendar_from_date, calendar_to_date in config.py
def return_user_input():
    config.calendar_from_date = cal_from_date.get_date()
    config.calendar_to_date = cal_to_date.get_date()

# GUI SETUP
# ROOT WINDOW
root =  tk.Tk()
root.title("Committee meetings information")

# root window size
root.resizable(False, False) # prevent window from resizing
root_width = 500
root_height = 350
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{root_width}x{root_height}+{int(((screen_width)-root_width)/2)}+{int(((screen_height)-root_height)/2)}") # center window on screen

# STYLES
# style - fonts
instructions_font = font.Font(family ='TkDefaultFont', size = 12)
widget_font = font.Font(family ='TkDefaultFont', size = 11)
message_font = font.Font(family ='TkDefaultFont', size = 11, weight ='bold')

# CALENDAR - DATE PICKER
# date picker instructions frame
date_picker_instructions_frame = ttk.Frame(root, padding = "5 10 0 0")
date_picker_instructions_frame.pack(anchor = "w")
# instructions label
user_choice = tk.StringVar() # set up as StringVar to update later
date_check = ttk.Radiobutton(date_picker_instructions_frame, value = "calendar", variable = user_choice, command = set_radio_button_choice)
date_check.pack(side = "left")
date_picker_instuctions_label = ttk.Label(date_picker_instructions_frame, text = "Select a date range", font = instructions_font)
date_picker_instuctions_label.pack(side = "left")

# parent frame for 'from date' label and 'calendar for' frame
parent_frame = ttk.Frame(root, padding = 10)
parent_frame.pack(anchor = "n", side = "top", fill = "x")
# 'from date' label
from_date_label = ttk.Label(parent_frame, text = "From:", font = widget_font, padding = "0 0 5 0")
from_date_label.pack(side = "left")
# calendar 'from date' picker
cal_from_date = DateEntry(parent_frame, selectmode = "day", font = widget_font, date_pattern='dd/MM/yyyy')
cal_from_date.pack(side  = "left")

# parent for 'to date' label and 'calendar to' frame
parent_two_frame = ttk.Frame(root, padding = 10)
parent_two_frame.pack(anchor = "n", side = "top", fill = "x")
# 'to date' label
to_date_label = ttk.Label(parent_two_frame, text = "To:", font = widget_font, padding = "0 0 22 0")
to_date_label.pack(side = "left")
# caledar 'to date' picker
cal_to_date = DateEntry(parent_two_frame, selectmode = "day", font = widget_font, date_pattern='dd/MM/yyyy')
cal_to_date.pack(side = "left")

# RADIO BUTTONS
# text style for radio buttons
radio_button_instructions_frame = ttk.Frame(root, padding = "5 10 0 0")
radio_button_instructions_frame.pack(anchor = "n", side = "top", fill = "x")
radio_check = ttk.Radiobutton(radio_button_instructions_frame, value = "radio", variable = user_choice, command = set_radio_button_choice)
radio_check.pack(side = "left")
# instructions label
radio_button_label = ttk.Label(radio_button_instructions_frame, text = "Select today's or this week's meetings", font = instructions_font)
radio_button_label.pack(side = "left")

# today/week
today_week_frame = tk.Frame(root)
today_week_frame.pack(anchor = "w", side = "top", padx = 11, pady = 5)
day_week_choice = tk.StringVar(value = " ")
today_radio = tk.Radiobutton(today_week_frame, value = "today", text = "Today's meetings", variable = day_week_choice, font = widget_font, command = set_day_week_choice)
today_radio.pack(anchor = "w")
week_radio = tk.Radiobutton(today_week_frame, value = "week", text = "This week's meetings", variable = day_week_choice, font = widget_font, command = set_day_week_choice)
week_radio.pack(anchor = "w")

# button label frame and label
button_label_frame = ttk.Frame(root, padding = "12 10 0 5")
button_label_frame.pack(anchor = "n", side = "top", fill = "x")
button_label_text = tk.StringVar()
button_label = ttk.Label(button_label_frame, textvariable = button_label_text, font = message_font, wraplength = root_width - 20)
button_label.pack(side = "left")

# calendar button frame
button_frame = ttk.Frame(root)
button_frame.pack(anchor = "n", side = "top", fill = "x")
# button style
button_style = ttk.Style()
button_style.configure('big.TButton', font = widget_font)
# button
fetch_button = ttk.Button(button_frame, text = "Fetch results", style = 'big.TButton', command = lambda: [return_user_input(), check_dates_order(), update_user(), check_day_week_choice()])
fetch_button.config(width = 20, padding = "2 2 2 2")
fetch_button.pack(anchor = "n", side = "left", padx = 10, pady = 5)

# run window loop
root.bind("<Button>", return_pressed_button) # monitor which button is getting clicked
root.mainloop()