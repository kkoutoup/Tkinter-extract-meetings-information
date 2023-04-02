from tkinter import *
from tkinter import ttk, font
import re

# disable radio buttons
def disable_radio_buttons():
    user_radio_today.config(state = "disabled")
    user_radio_week.config(state = "disabled")
    
# validate values entered in entry fields
def validate_date_inputs():
    # target user input
    inputs_combined = f"{from_date.get()}-{to_date.get()}"
    # check for valid input
    date_regex = re.compile(r'\d{2}\/\d{2}\/\d{4}\-\d{2}\/\d{2}\/\d{4}')
    check = re.match(date_regex, inputs_combined)
    if check is None: # notify user if no match
        label_text.set("Please enter a valid date range")
    else:
        label_text.set(f"Fetching results for {check.group()}. You can now close this window")
        return check.group()

# root window
root = Tk()
root.title("Committee meetings information")

# root window size
root.resizable(FALSE, FALSE) # prevent window from resizing
root.geometry("500x300")

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

# confirm button -  this runs multiple functions
confirm_button = ttk.Button(widget_frame, text ="Fetch results", command = lambda:[disable_radio_buttons(), validate_date_inputs()])

# user error label - output warning message to user
label_text = StringVar() # setting as StringVar to use set() later
label_text.set("")
user_message_label = ttk.Label(widget_frame, textvariable = label_text, font = message_font, wraplength = 450)

# POSITION ELEMENTS
# radio button widget
widget_frame.grid(column = 0, row = 0)
radio_button_label.grid(column = 0, row = 1, sticky = W)
user_radio_today.grid(column = 0, row = 2, sticky = W, pady = 5)
user_radio_week.grid(column = 0, row = 3, sticky = W, pady = 2)

# input widget
alternative_selection_label.grid(column = 0, row = 5, sticky = W, pady = 10)
widget_frame.grid(column = 0, row = 5, sticky = W, pady = 5)
date_from_label.grid(column = 0, row = 6, sticky = W, pady = 5)
start_date.grid(column = 0, row = 6, sticky = W, padx = 80)
date_to_label.grid(column = 0, row = 7, sticky = W, pady = 5)
end_date.grid(column = 0, row = 7, sticky = W, padx = 80)

# user message label
user_message_label.grid(column = 0, row = 8, sticky = W, pady = 5)

# confirm button
confirm_button.grid(column = 0, row = 9, sticky = W, pady = 5)
confirm_button.config(width = 20)

# run window loop
root.mainloop()
