# Python modules
import urllib
import urllib.request
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from datetime import datetime, date, timedelta
import logging, json, csv

# local modules
from helper_functions import extract_activity_types, extract_event_activities, extract_activities_times, format_activity_times
from user_input import get_user_input, translate_user_input

def main():
    # set up logging
    logging.basicConfig(filename='meetings_report.log', format='%(asctime)s-%(levelname)s\n%(message)s', datefmt='%d/%m/%Y @ %H:%M:%S', filemode='w', level=logging.INFO)

    def build_request_url():
        user_input = translate_user_input()
        print(user_input)
        # api endpoint example: 'https://committees-api.parliament.uk/api/Broadcast/Meetings?FromDate=2023-03-13&ToDate=2023-03-19' \
        # store to log file
        api_endpoint = f"https://committees-api.parliament.uk/api/Broadcast/Meetings?FromDate={user_input.split('/')[0]}&ToDate={user_input.split('/')[1]}"
        logging.info(f"API endpoint: {api_endpoint}\nfor date range: {user_input}\n")
        return api_endpoint
    
    def make_request():
        url = build_request_url()
        print("=> Getting meetings information")
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

    def write_to_json_file():
        api_response = make_request()
        print("=> Writing to file")
        try:
            with open('meetings_data.json', 'w', encoding='utf-8') as output_file:
                json.dump(json.loads(api_response), output_file, indent=4) # json loads to get rid of "\" in response
        except Exception as e:
            logging.info("Problems writing to file: {e}")
        
    # container - collecting all data here
    collected_data = []

    # read file and construct dataset
    def read_json_file():
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
                            'Activity titles': extract_event_activities(item),
                            # activity types
                            'Activity types': extract_activity_types(item),
                            # activities times
                            'Activities times': format_activity_times(extract_activities_times(item)),
                            # notes
                            'Notes': item['notes'],
                            # Event in CIS
                            'Event in CIS': f"https://admin.committees.parliament.uk/Committee/{item['committees'][0]['id']}/Event/Edit/{item['id']}#!/details"
                        })
                            
    # write to csv
    def write_to_csv():
        print("=> Writing to csv")
        with open('week_meetings.csv', 'w', newline='') as output_file:
            fieldnames = ['Committee name', 'Committee ID', 'Event ID', 'Date', 'Event start time', 'Event end time', 'Location', 'Number of activities', 'Activity titles', 'Activity types', 'Activities times', 'Notes', 'Event in CIS']
            writer = csv.DictWriter(output_file, fieldnames)
            writer.writeheader()
            writer.writerows(collected_data)

    # run sequence
    write_to_json_file()
    read_json_file()
    write_to_csv()

if __name__ == "__main__":
    main()
