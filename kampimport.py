import locale
import logging
import json
import os
import calendar
import requests
import time
import datetime

cwd = os.getcwd()
payload = {'cid': '356',
           'cwd': '0E977397-2AF0-479A-8A47-C6A7B090B47B', 'format': 'json'}
# 11er
r = requests.get(
    'http://api.fotballdata.no/v1/stadiums/6410/clubs/1138/matches', params=payload)
# print(r.headers)
# print(r.url)
# print(r.text)
r_dict = r.json()
# print(r_dict['StadiumName'])
# data = json.load(r_dict)
# print(r_dict)
for match in r_dict['Matches']:
    # print(match['MatchNumber'])
    MatchStartDate = match['MatchStartDate']
    matchdate = int(match['MatchStartDate'][6:16])
    matchdatetime_str = time.strftime(
        "%Y %m %d - %H:%M", time.localtime(matchdate))
    matchdatetime_str = time.strftime(
        "%Y %m %d - %H:%M", time.localtime(matchdate))
    # print(matchdatetime_str)
    matchdate_str = time.strftime(
        "%Y-%m-%d", time.localtime(matchdate))
    # print(matchdate_str)
    today = datetime.date.today()
    # print(today)
    kampdag = time.strptime(matchdate_str, "%Y-%m-%d")
    # print(kampdag)

    format_str = '%Y-%m-%d'  # The format
    datetime_obj = datetime.datetime.strptime(matchdate_str, format_str)
    # print(datetime_obj.date())

    if datetime_obj.date() >= today:
        print('Carsten')
        print(datetime_obj.date())
        print(['AwayTeamName'])

fotball_url = 'http://api.fotballdata.no/v1/teams/123166/matches?cid=356&cwd=0E977397-2AF0-479A-8A47-C6A7B090B47B&format=json'
# " 7er: https://calendar.google.com/calendar/b/2?cid=dHJvbmRmb3RiYWxsLm5vX3ZkazFsNmRkN284NnN0OXEyMjA5M29laHNjQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20" + "<br />"  +
# " 9er: https://calendar.google.com/calendar/b/2?cid=dHJvbmRmb3RiYWxsLm5vXzRnbTRxbjRhanYzdnFvNzA3cG9wYzlzajQwQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20" + "<br />"  +
# "11er: https://calendar.google.com/calendar/b/2?cid=dHJvbmRmb3RiYWxsLm5vXzE3a3NvcDUwZ2xtbXUwNHNxdjZybjZwbmlzQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20" + "<br />"  +

# open("./config/baner.json", "r", encoding="utf-8")
# data = json.load(json_file)
with open("./kampimport/config/baner.json") as json_file:
    data = json.load(json_file)

FORMAT = '%(asctime)-15s: %(levelname)s: %(message)s'
logging.basicConfig(
    format=FORMAT, filename='kampimport.log', level=logging.DEBUG)
locale.setlocale(locale.LC_ALL, 'norwegian')
logger = logging.getLogger()

logging.debug('-' * 80)
logging.debug('Kjorer kampimport')
logging.debug('-' * 80)


def kopierKamper(bane):
    # logging.debug('Behandler bane: ' + bane)
    # cal = Calendar(bane)
    msg = 'Kjorer kampimport til kalenderen ' + bane['cal_navn']
    bane_navn = bane['cal_navn']
    bane_url = bane['url']
    logging.debug(msg)
    print(msg)


for bane in data['baner']:
    print(calendar.weekheader(3))
    print()
    print(calendar.firstweekday())
    print(calendar.month(2019, 3))
    kopierKamper(bane)


# response = urllib.request.urlopen(fotball_url)
# content = response.read()
# fotball_data = json.loads(content.decode('utf-8'))
# print(fotball_data)
