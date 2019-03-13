# Keep Only Relevant Events

The Python script `keep_only_relevant_events.py` takes a list of event names from a text file and collects these events from all iCalendar files of a given directory into a new iCalendar file.

# Setup

Install the environment in the project directory using _pipenv_: `pipenv install --ignore-pipfile`

Now you can run the script via: `pipenv run python keep_only_relevant_events.py`

## Usage

```
usage: keep_only_relevant_events.py [-h] -e EVENTLIST -i INPUTDIR -o OUTPUTFILE

Takes a list of event names from a text file and filters all iCalendar files
of a given directory for these events.

optional arguments:
  -h, --help            show this help message and exit

required named arguments:
  -e EVENTLIST, --eventlist EVENTLIST
                        Text file with event names each separated by a newline
  -i INPUTDIR, --inputdir INPUTDIR
                        Directory containing the iCalendar files to be filtered
  -o OUTPUTFILE, --outputfile OUTPUTFILE
                        Filename of the resulting iCalendar file containing the relevant events
```