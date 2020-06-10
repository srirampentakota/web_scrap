name=1
while True:
	from fake_useragent import UserAgent
	import csv
	from urllib.request import Request,urlopen
	from bs4 import BeautifulSoup
	import re
	import time 
	from openpyxl import Workbook
	url="https://www.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbolCode=238&symbol=SBIN&symbol=SBIN&instrument=-&date=-&segmentLink=17&symbolCount=2&segmentLink=17"
	req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	page = urlopen(req).read()
	soup = BeautifulSoup(page,'lxml')
	table = soup.select_one("div.opttbldata")
	wb = Workbook()
	ws = wb.active
	rows=[]
	for row in table.select("tr"):
		headers=[]
		for th in row.find_all("th"):
			if th.has_attr("colspan"):
				span = int(th["colspan"])
				th=th.text.replace('\t',"").replace("\n","").replace("\r","")
				if(len(th)==0):
					for j in range(0,span):
						headers.append(th)
				else:
					headers.append(th)
					for i in range(1,span):
						headers.append("")
			else:
				th=th.text.replace('\t',"").replace("\n","").replace("\r","")
				headers.append(th)
		if(len(headers)!=0):
			rows.append(headers)
	for row in table.select("tr"):
		temp=[]
		for td in row.find_all("td"):
			if td.has_attr("colspan"):
				span = int(td["colspan"])
				td=td.text.replace('\t',"").replace("\n","").replace("\r","")
				if(len(td)==0):
					for j in range(0,span):
						temp.append(td)
				else:
					temp.append(td)
					for i in range(1,span):
						headers.append("")
			else:
				td=td.text.replace('\t',"").replace("\n","").replace("\r","")
				temp.append(td)
		if(len(temp)!=0):
			rows.append(temp)

	for i in rows:
    		ws.append(i)
	wb.save(str(name)+'.xlsx')
	name+=1
	time.sleep(20)
