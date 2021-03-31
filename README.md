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

# Testing
