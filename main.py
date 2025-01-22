from crew import event_management_crew
import json
from pprint import pprint

event_details = {
    'event_topic': "Tech Innovation Conference",
    'event_description': "A gathering of tech innovators "
                         "and industry leaders "
                         "to explore future technologies.",
    'event_city': "Chennai",
    'tentative_date': "2025-01-26",
    'expected_participants': 500,
    'budget': 20000,
    'venue_type': "Conference Hall"
}


result = event_management_crew.kickoff(inputs=event_details)


with open('venue_details.json') as f:
   data = json.load(f)

pprint(data)