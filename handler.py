import json
import re
import urllib.request
import urllib.error
from datetime import datetime, timedelta


SEARCH_URL = 'https://en.wikipedia.org/w/index.php?title={}&action=history'
RE_DATE_CHANGE = re.compile(r'<a href=.+class="mw-changeslist-date".+(\d{2}:\d{2},\s\d{2}\s\w+\s\d{4})</a>')
RESULT = {'latest_update_time': '', 'number_updates_last_month': 0}


def get_page_source(keyword):
     url = SEARCH_URL.format(keyword)
     try:
         with urllib.request.urlopen(url) as response:
             html = response.read()
             return html.decode()
     except urllib.error.URLError as err:
         return ''


def wiki_handler(event, context):
    keyword = event.get('queryStringParameters', {}).get('keyword', '')

    html = get_page_source(keyword)

    message = 'Found by keyword: {}'.format(keyword)
    extracted_dates = re.findall(RE_DATE_CHANGE, html)
    if not extracted_dates:
        RESULT['message'] = 'Seems to be there are no changes on the page.'
        return {'statusCode': 404,
                'body': json.dumps(RESULT)}
    dates = \
        [datetime.strptime(item, '%H:%M, %d %B %Y') for item in extracted_dates]
    dates.sort(reverse=True)
    latest_date = dates[0]

    month_ago = datetime.now() - timedelta(days=30)
    monthly_dates = [date for date in dates if date >= month_ago]

    RESULT.update({
        'message': 'Result for `{}` keyword.'.format(keyword),
        'latest_update_time': latest_date.isoformat(),
        'number_updates_last_month': len(monthly_dates)
    })
    return {'statusCode': 200, 'body': json.dumps(RESULT)}

# EOF
