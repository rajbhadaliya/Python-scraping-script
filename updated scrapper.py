import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import csv

name =  []
review = []


def link_scrap(url1):
	page = requests.get(url1)
	soup = bs(page.content,'html.parser')
	container = []
	#container = soup.find_all("div",{"class","profile-about__content"})
	try:
		container.append(soup.find("div",{"class","profile-about__content"}).find("div").get_text())
	except AttributeError:
		container.append("No data")
	#print(container)

def pagination(url, page_number):
	temp = page_number
	if page_number != 0:
		url = url + str(temp)
	#print(url)
	page = requests.get(url)
	soup = bs(page.content,'html.parser')
	container = soup.find_all("li",{"class","hz-pro-search-results__item"})
	name.append([item.find("span",{"itemprop":"name"}).get_text() for item in container])
	
	for i in range(15):
		try:
			review.append(container[i].find("span",{"class","hz-star-rate__review-string"}).get_text())
		except AttributeError:
			review.append("No data")
	
	""" link = [item.find('a').get('href') for item in container]

	for i in range(15):
		link_scrap(link[i]) """

	#Generating the next page url
	if page_number < 46:
		page_number = page_number + 15
		pagination('https://www.houzz.in/professionals/searchDirectory?topicId=26714&query=Bedding+%26+Bath&location=&distance=50&sort=4&p=', page_number)
   
#calling the function with relevant parameters
pagination('https://www.houzz.in/professionals/searchDirectory?topicId=26714&query=Bedding+%26+Bath&location=&distance=50&sort=4', 0)

print(*name, sep="\n")
print(*review, sep="\n")

all_data = {
    'Name' : name_data,
    'Address' : addresses_data,
    'Details' : detail_data
}
df = pd.DataFrame(all_data)
print(df)

df.to_csv('file_name.csv', index=False)
	










""" 
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

'''  """