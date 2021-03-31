import argparse
import json
import os
import urllib.request
import urllib.error

import pandas


API_URL = 'https://4gr9e0dl11.execute-api.us-east-1.amazonaws.com/dev?keyword={}'
HISTORY_FILE = 'history.json'


def get_wikipage_stats(keyword):
    url = API_URL.format(keyword)
    try:
        with urllib.request.urlopen(url) as response:
            return json.loads(response.read())
    except urllib.error.URLError as err:
        return {}

def save_history(data):
    data_to_save = []
    if os.path.exists('history.json'):
        with open(HISTORY_FILE, 'r') as fin:
            data_to_save = json.load(fin)

    data_to_save.append(data)
    with open(HISTORY_FILE, 'w') as fout:
        json.dump(data_to_save, fout, indent=4)
        

def get_history_stats():
    df = pandas.read_json(HISTORY_FILE)
    filtered = df[df['number_updates_last_month'] > 0]
    return (filtered['number_updates_last_month'].sum(),
            filtered['number_updates_last_month'].mean())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Gather information about updates on Wiki by passed keyword.')
    parser.add_argument('-k', '--keyword', dest='keyword',
                        help='Keyword for searching.')
    parser.add_argument('-s', '--stats', dest='stats', type=int,
                        help='Show history stats limited by number of updates.')
    args = parser.parse_args()

    if args.keyword:
        result = get_wikipage_stats(args.keyword)
        print(result)
        save_history(result)

    if args.stats:
        print(get_history_stats())
    
# EOF
