# Python modules
from datetime import datetime, date, timedelta

def extract_event_activities(item):
    activity_titles = []
    if not item['activities']: 
        return 'No activities found'
    if len(item['activities']) == 1 and item['activities'][0]['type'] == 'Private discussion': # private discussion activities don't have titles
        return 'No activity title for private discussion'
    if len(item['activities']) > 0:
        activity_titles = [activity['subjects'][0] for activity in item['activities'] if activity['subjects']]
        return '/'.join(list(dict.fromkeys(activity_titles))) # if more than one activities have the same name then only keep the activity name once

def extract_activity_types(item):
    item_activities = item['activities']
    if item['activities']:
        item_activities_list = [item['type'] for item in item_activities]
        return '/'.join(item_activities_list)
    else:
        return 'No activity types found'
    
def extract_activities_times(item):
    event_activities = item['activities']
    activity_times = []
    if event_activities:
        for item in event_activities:
            itemStartTime = datetime.strftime(datetime.fromisoformat(item['startTime']), '%H:%M:%S')
            itemEndTime = datetime.strftime(datetime.fromisoformat(item['endTime']), '%H:%M:%S')
            activity_times.append([itemStartTime, itemEndTime])
    else:
        activity_times.append('No activity times found')
    return activity_times
