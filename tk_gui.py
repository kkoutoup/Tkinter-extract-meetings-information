# Python modules
from tkinter import *
from tkinter import ttk, font
import re

# identify the button that was pressed and return corresponding value
def return_pressed_button(event):
    global event_target
    event_target = str(event.widget)
    return event_target

# validate user input and return values for api request
def validate_date_inputs():
    if str(event_target) == '.!frame.!button':
        # target user input
        inputs_combined = f"{from_date.get()}-{to_date.get()}"
        # check for valid input
        date_regex = re.compile(r'\d{2}\/\d{2}\/\d{4}\-\d{2}\/\d{2}\/\d{4}')
        check = re.match(date_regex, inputs_combined)
        if check is None: # notify user if no match
            label_text.set("Please enter a valid date range")
        else:
            label_text.set(f"Fetching results for {check.group()}. You can now close this window.")
            return check.group()
    else:
        user_choice = str(user_radio_choice.get())
        if user_choice == '':
            second_label_text.set(f"Please select between today's and this week's meetings")
        else:
            second_label_text.set(f"Fetching {str(user_radio_choice.get())}'s meetings information. You can now close this window.")
        return user_choice

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

# style - fonts
widget_font = font.Font(family ='TkDefaultFont', size = 12)
message_font = font.Font(family ='TkDefaultFont', size = 12, weight ='bold')

# widget frame - parent of radiobuttons etc
widget_frame = ttk.Frame(root, padding = 10)
widget_frame.pack()

# widget frame labels
radio_button_label = ttk.Label(widget_frame, text ="Today's or this week's meetings", font = widget_font)
alternative_selection_label = ttk.Label(widget_frame, text ="Select a different timespan (dd/mm/yyyy)", font = widget_font)
date_from_label = ttk.Label(widget_frame, text ="Start date")
date_to_label = ttk.Label(widget_frame, text ="End date")

# radio buttons - choose between today's and week's meetings
user_radio_choice = StringVar()
user_radio_today = ttk.Radiobutton(widget_frame, text ="Today's meetings", variable = user_radio_choice, value = 'today')
user_radio_week = ttk.Radiobutton(widget_frame, text ="This week's meetings", variable = user_radio_choice, value = 'week')

# entry item - for typing input
from_date = StringVar()
start_date = ttk.Entry(widget_frame, textvariable = from_date)
to_date = StringVar()
end_date = ttk.Entry(widget_frame, textvariable = to_date)

# buttons for entry elements and radio buttons -  this runs multiple functions
entry_confirm_button = ttk.Button(widget_frame, text ="Fetch results", command = lambda:[validate_date_inputs()])
radio_confirm_button = ttk.Button(widget_frame, text = "Fetch results", command = lambda:[validate_date_inputs()])
root.bind('<Button>', return_pressed_button) # monitor which button is pressed globally

# user error labels - output warning message to user
label_text = StringVar() # setting as StringVar to use set() later
label_text.set("")
second_label_text = StringVar()
second_label_text.set("")
entry_user_message_label = ttk.Label(widget_frame, textvariable = label_text, font = message_font, wraplength = 450)
radio_user_message_label = ttk.Label(widget_frame, textvariable = second_label_text, font = message_font, wraplength = 450)

# POSITION ELEMENTS
# radio button widgets
widget_frame.grid(column = 0, row = 0)
radio_button_label.grid(column = 0, row = 1, sticky = W)
user_radio_today.grid(column = 0, row = 2, sticky = W, pady = 5)
user_radio_week.grid(column = 0, row = 3, sticky = W, pady = 2)
radio_confirm_button.grid(column = 0, row = 5, sticky = W, pady = 5)
radio_confirm_button.config(width = 20)

# input widgets
alternative_selection_label.grid(column = 0, row = 6, sticky = W, pady = 10)
widget_frame.grid(column = 0, row = 7, sticky = W, pady = 5)
date_from_label.grid(column = 0, row = 8, sticky = W, pady = 5)
start_date.grid(column = 0, row = 8, sticky = W, padx = 80)
date_to_label.grid(column = 0, row = 9, sticky = W, pady = 5)
end_date.grid(column = 0, row = 9, sticky = W, padx = 80)

# user message labels for radio buttons and entry elements
radio_user_message_label.grid(column = 0, row = 4, sticky = W, pady = 5)
entry_user_message_label.grid(column = 0, row = 10, sticky = W, pady = 5)

# confirm button
entry_confirm_button.grid(column = 0, row = 11, sticky = W, pady = 5)
entry_confirm_button.config(width = 20)

# run window loop
root.mainloop()
