import urllib
import urllib.request
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from datetime import datetime, date, timedelta
import logging, json, csv

def main():
    # set up logging
    logging.basicConfig(filename='meetings_report.log', format='%(asctime)s-%(levelname)s\n%(message)s', datefmt='%d/%m/%Y @ %H:%M:%S', filemode='w', level=logging.INFO)

    def build_request_url():
        print("=> Getting this week's dates")
        # api endpoint example: 'https://committees-api.parliament.uk/api/Broadcast/Meetings?FromDate=2023-03-13&ToDate=2023-03-19' \
        # calculate date range => start of week - today's date
        today = date.today()
        today_as_weekday = today.weekday()
        # start of week
        start_of_week = today - timedelta(days=today_as_weekday)
        # end of week = start of week + 6 days
        end_of_week = start_of_week + timedelta(days=6)
        # store to log file
        # api_endpoint = f"https://committees-api.parliament.uk/api/Broadcast/Meetings?FromDate={start_of_week}&ToDate={end_of_week}"
        api_endpoint = f"https://committees-api.parliament.uk/api/Broadcast/Meetings?FromDate=2023-03-22&ToDate=2023-03-22"
        logging.info(f"API endpoint: {api_endpoint}\nfor date range: {datetime.strftime(start_of_week, '%d/%m/%Y')} - {datetime.strftime(end_of_week, '%d/%m/%Y')}\n")
        return api_endpoint
    
    def make_request():
        url = build_request_url()
        print("=> Getting this week's meetings information")
        try:
            with urllib.request.urlopen(url) as response:
                logging.info(f"Response code: {response.getcode()}")
                return response.read().decode('cp1252') # resolve encoding issues => 'charmap' codec can't encode character '\u0175'
        except urllib.error.HTTPError as http_error:
            logging.info(f"Something went wrong when fetching the data: {http_error} - {http_error.code}")
        except urllib.error.URLError as url_error:
            logging.info(f"There was something wrong with the request: {url_error} - {url_error.reason}")
        except Exception as e:
            logging.info(print(f"Oops! {e}"))

    def write_to_file():
        api_response = make_request()
        print("=> Writing to file")
        try:
            with open('meetings_data.json', 'w', encoding='utf-8') as output_file:
                json.dump(json.loads(api_response), output_file, indent=4) # json loads to get rid of "\" in response
        except Exception as e:
            logging.info("Problems writing to file: {e}")

    def extract_event_activities(item):
        activity_titles = []
        if len(item['activities']) == 0: 
            return 'No activities found'
        if len(item['activities']) == 1 and item['activities'][0]['type'] == 'Private discussion': # private discussion activities don't have titles
            return 'No activity title for private discussion'
        if len(item['activities']) > 0:
            activity_titles = [activity['subjects'][0] for activity in item['activities'] if activity['subjects']]
            return '/'.join(list(dict.fromkeys(activity_titles))) # if more than one activities have the same name then only keep the activity name once

    def extract_activity_types(item):
        item_activities = item['activities']
        item_activities_list = [item['type'] for item in item_activities if item_activities]
        return '/'.join(item_activities_list)
        
    # container - collecting all data here
    collected_data = []

    # read file and construct dataset
    def read_file():
        with open('meetings_data.json', 'r') as input_file:
            data = input_file.read()
            data_to_json = json.loads(data)
            for item in data_to_json:
                if item['isCommons']: # only select House of Commons events
                    collected_data.append({
                            # committe name
                            'Committee name': item['committees'][0]['name'],
                            # committee ID
                            'Committee ID': item['committees'][0]['id'],
                            # event ID
                            'Event ID': item['id'],
                            # date - from start time
                            'Date': datetime.strftime(datetime.fromisoformat(item['startTime']), '%A %d %B %Y'),
                            # start time
                            'Event start time': datetime.strftime(datetime.fromisoformat(item['startTime']), '%H:%M:%S'),
                            # end time
                            'Event end time': datetime.strftime(datetime.fromisoformat(item['endTime']), '%H:%M:%S'),
                            # location
                            'Location': item['location']['description'],
                            # No of activities
                            'Number of activities': len(item['activities']),
                            # activities
                            'Activities': extract_event_activities(item),
                            # activity types
                            'Activity types': extract_activity_types(item),
                            # notes
                            'Notes': item['notes'],
                            # Event in CIS
                            'Event in CIS': f"https://admin.committees.parliament.uk/Committee/{item['committees'][0]['id']}/Event/Edit/{item['id']}#!/details"
                        })
                            
    # write to csv
    def write_to_csv():
        print("=> Writing to csv")
        with open('week_meetings.csv', 'w', newline='') as output_file:
            fieldnames = ['Committee name', 'Committee ID', 'Event ID', 'Date', 'Event start time', 'Event end time', 'Location', 'Number of activities', 'Activities', 'Activity types', 'Notes', 'Event in CIS']
            writer = csv.DictWriter(output_file, fieldnames)
            writer.writeheader()
            writer.writerows(collected_data)

    # run sequence
    write_to_file()
    read_file()
    write_to_csv()

if __name__ == "__main__":
    main()
