while True:
	import csv
	from urllib.request import Request,urlopen
	from bs4 import BeautifulSoup
	import re
	import time 
	from openpyxl import Workbook
	#import datetime
	#currentDT = datetime.datetime.now()
	#page = urllib2.urlopen(url)
	url="https://www.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbolCode=238&symbol=SBIN&symbol=SBIN&instrument=-&date=-&segmentLink=17&symbolCount=2&segmentLink=17"
	req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	page = urlopen(req).read()
	soup = BeautifulSoup(page,'lxml')
	table = soup.select_one("div.opttbldata")
	# python3 just use th.text
	#headers = [th.text.encode("utf-8") for th in table.select("tr")]
	#headers = [th.text for th in table.select("th")]
	#head=headers[:3]
	#headers=headers[3:]
	#d={"\n":"","\r":"","\t":""}
	#print([[td.text.replace('\t',"").replace("\n","").replace("\r","") for td in row.find_all("td")] for row in table.select("tr")])
	"""
	with open("out2.csv", "w") as f:
    	wr = csv.writer(f)
    	wr.writerow(headers)
    	#wr.writerows([[td.text.encode("utf-8") for td in row.find_all("td")] for row in table.select("tr + tr")])
    	wr.writerows([[td.text.replace('\t',"").replace("\n","").replace("\r","") for td in row.find_all("td")] for row in table.select("tr")])
	"""
	#wb = Workbook()
	#sheet1 = wb.add_sheet('Sheet 1')
	wb = Workbook()
	ws = wb.active
	#rows=[[td.text.replace('\t',"").replace("\n","").replace("\r","") for td in row.find_all("td")] for row in table.select("tr")]
	#ws.append(head)
	#ws.append(headers)
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
	#with open('out2.csv', 'r') as f:
	#    for row in csv.reader(f):
	#        ws.append(row)
	#wb.save('out8.xlsx')
	wb.save('out5.xlsx')
	#wb.save('out9.xlsx')
	print("done")
	time.sleep(100)
