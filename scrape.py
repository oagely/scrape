import requests
from bs4 import BeautifulSoup

base_url = 'https://www.yelp.com/search?find_desc=Restaurants&find_loc='
loc = 'Newport+Beach,+CA,+United+States'
current_page = 0

def look_up_loc(loc):

look_up_loc(new_loc)

while current_page < 200:
	print(current_page)
	url = base_url + loc + "&start=" str(page)
	yelp_r = requests.get(url)
	yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')
	businesses = yelp_soup.findAll('div', {'class': 'biz-listing-large'})

	file_path = 'yelp-{loc}-2.txt'.format(loc=loc)

	for biz in businesses:
		#print(biz)
		title = biz.findAll('a', {'class': 'biz-name'})[0].text
		print(title)
		try:
			address = biz.findAll('address')[0]
		except:
			address = None
		print(address)
		second_line = ""
		first_line = ""
		for item in address:
			if "br" in str(item):
				print(item.getText())
			else:
				print(item.strip(" \n\t\r"))
				first_line = item.strip(" \n\t\r")
		print('\n')
		phone = biz.findAll('span', {'class': 'biz-phone'})[0].text
		print(phone)
		page_line = "{title}\n{address}\n{phone}\n\n".format(
			title=title,
			address=address,
			phone=phone)
		textfile.write(page_line)
	current_page += 10






file_path = 'yelp-{loc}.txt'.format(loc=loc)

with open(file_path, "a") as textfile:
	businesses = yelp_soup.findAll('div', {'class': 'biz-listing-large'})

	for biz in businesses:
		#print(biz)
		title = biz.findAll('a', {'class': 'biz-name'})[0].text
		print(title)
		address = biz.findAll('address')[0]
		print(address)
		print('\n')
		phone = biz.findAll('span', {'class': 'biz-phone'})[0].text
		print(phone)
		page_line = "{title}\n{address}\n{phone}\n\n".format(
			title=title,
			address=address,
			phone=phone)
		textfile.write(page_line)



print(yelp_soup.findAll('li', {'class': 'biz-name'}))

for name in yelp_soup.findAll('li', {'class': 'biz-name'}):
	print(name.text)



#yelp_r -- <Response 200>


yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')
print(yelp_soup.findAll('li', {'class': 'regular-search-result'}))

print(yelp_soup.findAll('li', {'class': 'biz-name'}))

for name in yelp_soup.findAll('li', {'class': 'biz-name'}):
	print(name.text)








print(yelp_r.status_code)



print(yelp_soup.prettify())
print(yelp_soup.findAll('li', {}))

for link in yelp_soup.findAll('a'):
	print(link)




