# Web scraper script for mining stock exchange data

This repo consists of python scripts extract the required economic data from one of the Stock Exchange websites (NSE) 
and store it in the local machine in the form of Excel sheet for every 30 min (A specific time interval based on the requirement).

Inorder to setup the code follow below steps:
---------------------------------------------

 1. Clone the repository in your local machine.
 2. Open the folder and open termianl in current working directory.
 3. Install all the packages mentioned in requirements.txt.
 4. Use the below command to install all packages.

     command:  pip3 install -r requirements.txt

 5. Now the setup is ready, you can Extract the data and store it in your machine. 

Extract and update same excel file:
-----------------------------------

 1. Go to the directory web_scrap.
 2. Open the terminal in the current directory.
 3. Enter the command in the below format:
	
	python3 scrap.py 

 A new excel file is created in the current working directory with the required data and the same file will get updated from the next time.

Extract and update same excel file:
-----------------------------------

 1. Go to the directory web_scrap.
 2. Open the terminal in the current directory.
 3. Enter the command in the below format:
	
	python3 scrap_new_file.py 

 A new excel file is created everytime in the current working directory with the required data updated in it.
