import calendar
import locale 
import random
import string

from requests_html import HTMLSession

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

def start_request(url):
    headers = {'user-agent':random.choice(USER_AGENT_LIST) }
    session = HTMLSession()
    print(url)
    response = session.get(url,headers=headers)
    return response  


def clean_date_string_from_punctution(date_string):
    translator=str.maketrans('','',string.punctuation)
    date_string=date_string.translate(translator)
    return date_string

def replace_month_name_to_number(date_string):
    lower_string = date_string.lower()
    for month_id in range(1, 13):
        if(lower_string.find(calendar.month_name[month_id])!=-1):
            return (lower_string.replace(calendar.month_name[month_id],"0"+str(month_id)))
        if(lower_string.find(calendar.month_abbr[month_id])!=-1):
            return (lower_string.replace(calendar.month_abbr[month_id],"0"+str(month_id)))


def get_numbers_from_date_string(date_string):
    splitted_date = [string for string in date_string.split() if string.isdigit()]
    return splitted_date

def print_format_date_structure():
    print('''
    def format_date(date_string):
        ...
        return real_date_format
    ''')
def print_date_structure():
    print('''
    año-mes-dia
    2018-04-28
    '''
    )

def print_scrap_structure():
    print('''
    query_extract_title = '//tag[@class="???"]'
    query_extract_text = "//tag[@class='???']//p"
    query_extract_date = "//tag[@class='???']"
    ''')

def print_crawl_structure():
    print('''
    query_extract_all_href = "//tag[@class='???']//h1/a/@href"
    ''')
