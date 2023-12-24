import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) AppleWeKit/537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
webpage=requests.get('https://www.ambitionbox.com/list-of-companies?page=1',headers=headers).text

soup=BeautifulSoup(webpage,'html.parser')
soup.find_all('h1')[0].text

company=soup.find_all('div',class_='company-content-wrapper')
len(company) 

name=[]
rating=[]
reviews=[]
ctype=[]
hq=[]
how_old=[]
no_of_employee=[]

for i in company:

  name.append(i.find('h2').text.strip())
  rating.append(i.find('p',class_='rating').text.strip())
  reviews.append(i.find('a' , class_='review-count').text.strip())
  ctype.append(i.find_all('p',class_='infoEntity')[0].text.strip())
  hq.append(i.find_all('p',class_='infoEntity')[1].text.strip())
  how_old.append(i.find_all('p',class_='infoEntity')[2].text.strip())
  no_of_employee.append(i.find_all('p',class_='infoEntity')[3].text.strip())

d={'name' : name,'rating' : rating,'reviews':reviews,'Type':ctype,'HQ':hq,'how_old':how_old,'no_of_employee':no_of_employee}

df=pd.DataFrame(d)

df
