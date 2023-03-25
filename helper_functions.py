# Python modules
from datetime import datetime

def extract_activity_titles(item):
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
            item_start_time = datetime.strftime(datetime.fromisoformat(item['startTime']), '%H:%M')
            item_end_time = datetime.strftime(datetime.fromisoformat(item['endTime']), '%H:%M')
            activity_times.append([item_start_time, item_end_time])
    else:
        activity_times.append('No activity times found')
    return activity_times

def format_activity_times(times):
    formatted_times = ""
    if 'No activity times found' in times:
        return 'No activity times found'
    else:
        for item in times:
            to_add = f"{item[0]}-{item[1]}/"
            formatted_times += to_add
        return formatted_times.rstrip("/")
