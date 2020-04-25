import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import csv

url = 'https://www.houzz.in/professionals/searchDirectory?topicId=26714&query=Bedding+%26+Bath&location=&distance=50&sort=4'

page = requests.get(url)

soup = bs(page.content,'html.parser')
#print(len(soup))

container = soup.find_all("ul",{"class","hz-pro-search-results mb0"})
#print(len(container[0]))

name = soup.find("span",{"itemprop":"name"})
#print(Name.get_text())

Detail = soup.find("p",{"class":"hz-pro-search-result__about-me mtm mbxs"})
#print(Detail.get_text())

Add = soup.find("span",{"class":"hz-pro-search-result__location-info__text text-bold"})
#print(Add.get_text())

for names in name: 
	print(names.text)


	#name_soup = items.find("span",{"itemprop":"name"})
	#rint(name_soup.get_text())

	#detail_soup = items.find("p",{"class":"hz-pro-search-result__about-me mtm mbxs"})
	#print(detail_soup.get_text())

	#add_soup = items.find("span",{"class":"hz-pro-search-result__location-info__text text-bold"})
	#print(add_soup.get_text())

'''
#	records.append((name_soup,phone_soup,add_soup))

#	df = pd.DataFrame(records, columns=['name_soup','phone_soup','add_soup'])
    
#	df.to_csv('file1.csv', index=False, encoding='utf-8')	 

'''