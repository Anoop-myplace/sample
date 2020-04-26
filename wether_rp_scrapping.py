from bs4 import BeautifulSoup
import csv
import requests

page = requests.get('https://www.worldweatheronline.com/lang/en-in/varanasi-weather/uttar-pradesh/in.aspx')
soup = BeautifulSoup(page.content,'html.parser')

csv_file = open('Wether_rp scrapped.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Date','Day','Temprature','Climate Status'])

week = soup.find(class_ ="col-lg-12 col-md-12 col-sm-12 col-xs-12")
items = week.find_all(class_ = "carousel-cell well text-center")
 
for item in items:
    atb = (item.text.split(' '))
    day=atb[0]
    date=atb[1]
    temp=atb[3]
    desc = item.find('img',class_ = "lazyload img-rounded")['title']
    csv_writer.writerow([date,day,temp,desc])
    
csv_file.close()
