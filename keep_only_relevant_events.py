#!/usr/bin/python3

"""
Takes a list of event names from a text file and collects these events 
from all iCalendar files of a given directory into a new iCalendar file.
"""

from sys import argv
import getopt
import argparse
from os import listdir
from os.path import isfile, join
from icalendar import Calendar, Event

# Handle arguments
parser=argparse.ArgumentParser(
    description=''' Takes a list of event names from a text file and collects these events 
from all iCalendar files of a given directory into a new iCalendar file. ''')
requiredNamed = parser.add_argument_group('required named arguments')
requiredNamed.add_argument('-e','--eventlist', type=str, help='Text file with event names each separated by a newline',required=True)
requiredNamed.add_argument('-i','--inputdir', type=str, help='Directory containing the iCalendar files to be filtered',required=True)
requiredNamed.add_argument('-o','--outputfile', type=str, help='Filename of the resulting iCalendar file containing the relevant events',required=True)
args=parser.parse_args()

# Get a list of all iCalendar file names
ics_files = [f for f in listdir(args.inputdir) if isfile(join(args.inputdir, f)) and f.lower().endswith('.ics')]

# Read the relevant event names into a list 
with open(args.eventlist) as f:
  events = f.read().splitlines()

# Create a new calendar object
new_cal = Calendar()
new_cal.add('prodid', '-//KeepOnlyRelevantEvents//EN')
new_cal.add('version', '1.0')

# Iterate through each file and event and add the relevant ones to the new calendar object
for f in ics_files:
  cal_file_path = join(args.inputdir, f)
  cal_file = open(cal_file_path,'rb')
  cal = Calendar.from_ical(cal_file.read())

  for component in cal.walk():
    is_event_and_relevant = component.name == "VEVENT" and component.get('summary') in events
    if is_event_and_relevant:
      new_cal.add_component(component)

  cal_file.close()

# Write the new iCalendar file
f = open(args.outputfile, 'wb')
f.write(new_cal.to_ical())
f.close()