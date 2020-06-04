from bs4 import BeautifulSoup
import pandas as pd
#from urllib2 import urlopen
from urllib.request import Request,urlopen
import requests
import csv
url="https://www.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbolCode=238&symbol=SBIN&symbol=SBIN&instrument=-&date=-&segmentLink=17&symbolCount=2&segmentLink=17"
table = pd.read_html(requests.get(url).text, attrs={"class" : "opttbldata"})

print (table)
