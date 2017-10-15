import requests
from SakaiPy import SakaiPy
from SakaiPy.SakaiTools import Assignment
#import googleapiclient
from pprint import pprint
import json

info = {'username': '', # your username here, see TODO in README.md
        'password': '', # your password here
        'baseurl': 'https://sakai.luc.edu'} # or the url of your institution

sak = SakaiPy.SakaiPy(info)
cal = sak.get_calendar()
calDict = cal.getAllMyEvents()
calStrJson = json.dumps(calDict, ensure_ascii=False)
calPartJson = json.loads(calStrJson)
calJson = calPartJson["calendar_collection"]
assDict = {}
for a, b in enumerate(calJson):
    assDict[b['assignmentId']] = b
with open('sakCal.json', 'w') as f:
    json.dump(assDict, f)
    f.close()

