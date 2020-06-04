#from bs4 import BeautifulSoup
#import urllib2
import csv
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup
"""
url="https://www.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbolCode=238&symbol=SBIN&symbol=SBIN&instrument=-&date=-&segmentLink=17&symbolCount=2&segmentLink=17"
#page = urllib2.urlopen(url)
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(req).read()
soup = BeautifulSoup(page,'lxml')
"""

url = 'http://www.data.jma.go.jp/obd/stats/etrn/view/monthly_s3_en.php?block_no=47401&view=1'
#html = urllib2.urlopen(url).read()
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read()
soup = BeautifulSoup(html,'lxml')
table = soup.select_one("table.data2_s")
# python3 just use th.text
headers = [th.text for th in table.select("tr th")]
print(headers)
print([[td.text for td in row.find_all("td")] for row in table.select("tr + tr")])
"""
with open("out.csv", "w") as f:
    wr = csv.writer(f)
    wr.writerow(headers)
    wr.writerows([[td.text for td in row.find_all("td")] for row in table.select("tr + tr")])
"""
