# Tkinter extract committee meetings information from Parliament's API
A Python script that extracts committee meetings information from UK Parliament's API based on user choice.
- Today's meetings
- Week's meetings
- Meetings within a date range
Gathered data are exported in csv and json format.

## Category
API/data collection

## Purpose
Help with checking committee meetings information appearing in Parliament's publications are correct.

## Instructions
- Download repo
- Run ```extract_meetings_information.py```
- Select between ```today```, ```week``` or ```date range```
to extract meetings information for the day, week or date range respectively.

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
- urllib
- json
- csv
- datetime
- re
- logging

## Developed by
Kostas Koutoupis ([@kkoutoup](https://github.com/kkoutoup))
