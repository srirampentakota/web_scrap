#import urllib2
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup
url="https://www.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbolCode=238&symbol=SBIN&symbol=SBIN&instrument=-&date=-&segmentLink=17&symbolCount=2&segmentLink=17"
#page = urllib2.urlopen(url)
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(req).read()
soup = BeautifulSoup(page,'lxml')
data= soup.find('div', attrs={'class':'opttbldata'})
#print(data)
import csv
from datetime import datetime
with open('index.csv', 'a') as csv_file:
	writer = csv.writer(csv_file)
	writer.writerow([data])

