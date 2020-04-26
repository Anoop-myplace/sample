from bs4 import BeautifulSoup
import pandas as pd
import requests

page = requests.get('https://www.worldweatheronline.com/lang/en-in/varanasi-weather/uttar-pradesh/in.aspx')
soup = BeautifulSoup(page.content,'html.parser')
week = soup.find(class_ ="col-lg-12 col-md-12 col-sm-12 col-xs-12")
items = week.find_all(class_ = "carousel-cell well text-center")

day = []
date = []
temp = []

for item in items:
    atb = (item.text.split(' '))         #atb = attributes scrapped
    day.append(atb[0])
    date.append(atb[1])
    temp.append(atb[3])

desc = [item.find('img',class_ = "lazyload img-rounded")['title'] for item in items]

wether_rp = pd.DataFrame(
        {
                'Day':day,
                'Date':date,
                'Status':desc,
                'Temperature':temp,
        })
    
wether_rp.to_csv("wether_report scrapped.csv")
