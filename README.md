# Tkinter extract committee meetings information from Parliament's API
Python script that extracts committee meetings information from UK Parliament's API based on user choice with a Tkinter user interface.
- Today's meetings
- Week's meetings
- Meetings within a date range
Gathered data are exported in csv and json format.

This is an alternative to [this Python script](https://github.com/kkoutoup/API-extract-meetings-information) that gets user input through the terminal.

## Category
API/data collection

## Purpose
Help with checking committee meetings information appearing in Parliament's publications are correct.

## Instructions
- Download repo
- Run ```extract_meetings_information.pyw```
- In the new window select between
    - ```date range``` using the date picker to extract meetings information in a desired date range
    - or between ```today```, ```week``` from the radio buttons to exact the day's or week's meetings respectively
- Click the "Fetch results" button and close the window. A .log, .json and .csv file should appear in the project's folder.

## Data collected
The following data is collected for each meeting:
- Committee name
- Committee ID
- Event ID
- Date
- Event start time
- Event end time
- Event location
- Number of activities within the event
- Activity titles
- Activity types (i.e. Private discussion, oral evidence session etc.)
- Activities times (start and end times for activities within the event)
- Notes (any notes added for the event)
- Event in CIS (link for event details in Committee Information System)

## Dependencies
Built in Python 3.11.2 with the following modules
- tkinter
- urllib
- json
- csv
- datetime
- re
- logging

## Developed by
Kostas Koutoupis ([@kkoutoup](https://github.com/kkoutoup))
