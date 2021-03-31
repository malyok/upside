# upside wiki page updates
A script and lambda function to obtain information about the number of changes of a Wiki page. Lambda function finds a Wiki page using passed keyword.
As a result, the main script returns the latest update time in ISO 8601 format and the number of updates within the last month. Also, it can calculate the sum and average value of the number of updates.

## Usage of main.py script:
```
$ python main.py -h
usage: main.py [-h] [-k KEYWORD] [-s STATS]

Gather information about updates on Wiki by passed keyword.

optional arguments:
  -h, --help            show this help message and exit
  -k KEYWORD, --keyword KEYWORD
                        Keyword for searching.
  -s STATS, --stats STATS
                        Show history stats limited by number of updates.
```

# Possible improvements
Lambda handler uses regexp functionality to extract data. Probably, usage of HTML parsers like Beautiful Soup or lxml may improve the speed of processing.
The main flow is synchronized it would be great to switch to async functionality. Add S3 storage for storing history instead of local.

# Testing
Cover main.py script with unit tests that must check the following cases:
- run script with wrong arguments
- run script with -h argument to ensure that the help is present
- verify script work in case of network unavailability
- verify script work in case of empty result from lambda
- verify storing of the history file
- verify correct values of statistics with different input data

Cover handler.py script with unit tests that must check the following cases:
- verify script work in case of network unavailability
- verify script work in case of empty response
- verify script work in case of response decoding issues
- check status codes for different circumstances
- check that number of updates is calculated in accordance with the requirement in 30 days
