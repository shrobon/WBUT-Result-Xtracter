__author__ = 'Shrobon'
from re import search as find
import requests
from bs4 import BeautifulSoup
def range(lower,upper,sem):
    while(lower<=upper):
        with requests.Session() as req:
            dom=BeautifulSoup(req.post("http://www.wbutech.net/show-result.php",data={"semno":sem,"rollno":lower,"rectype":1},headers={"Referer":"http://www.wbutech.net/result_odd.php"}).text)
            if len(dom.find_all("th"))==14:
            	name=find("Name : (.+)",dom.find_all("th")[1].text.strip()).group(1)
            	reg=find("Registration No. : (.+) OF",dom.find_all("th")[3].text.strip()).group(1)
            	sgpa=find("SEMESTER : ([0-9.]+)",dom.find_all("td")[54].text.strip()).group(1)
            	print (name+", "+str(lower)+", "+reg+", "+sgpa)
            else:
            	print (str(lower)+" MISSING")
            req.close()
            lower+=1
range(30000112001,30000112030,5)