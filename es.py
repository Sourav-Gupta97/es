"""
Overview 
Consists of 1 function: 

1) Main:  
  Input: No input for the function but takes input from the user for a file location. Also asks if you would like a CSV output for the cleaned data. 
  Output: Returns a dictionary from the JSON file and an "example.csv" file if said Y in the second question. 

2) date_conversion:
  Input: ISO date formate
  Output: date time object


Libraries Imported
- Json 
- Date time
- Pandas

Steps to run: 
Just call Main() and let the program guide you. 

"""


import json
from datetime import datetime
import pandas as pd

def date_conversion(timestamps):

    
    dt_object = datetime.fromtimestamp(timestamps)
    return str(dt_object)
  

def Main():
  location = input("Please enter the location of the file: ")
  outDf = input ("Do you want a csv Output? (Y/N) ")

  with open(location) as f:
    data = json.load(f)

  ## Dictionary to store a list of all the races
  race_lists = []

  ##Individual dict
  race_dict = {}

  ## looping through all the sections for that particular date: 
  meetingDate = data["dates"][0]['meetingDate']
  for sections in data["dates"][0]['sections']:
    animalType = sections["displayName"]
    ## looping through each meeting: 
    for raceType in sections["meetings"]:
      ## looping through each of the events
      meeting_id = raceType["id"]
      meeting_name = raceType["name"]
      for event in raceType["events"]:
        try: 
          race_number = event["raceNumber"]
          race_link = event["httpLink"]
          event_id = event["id"]
          distance = event["distance"]
          start_time = date_conversion(event["startTime"])

          race_dict = {"meeting_id": meeting_id, "meeting_name": meeting_name, "race_number": race_number, "race_link": race_link, "event_id": event_id, "distance": distance, "start_time": start_time}

          ## appending the dict
          race_lists.append(race_dict)

        
        except KeyError:
          pass
  
  if outDf == "Y":
    df = pd.DataFrame(race_lists)
    df.to_csv("example.csv")

  print(race_lists)

Main()