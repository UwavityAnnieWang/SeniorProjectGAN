#!/usr/bin/env python3
#don't forget the shebang lmfao 
import shutil 
import requests
import urllib.request
import re
import httplib2
 

#import httplib.client

#import urllib3
#import json
#import ast
from bs4 import BeautifulSoup, SoupStrainer
#this one will be the scraper fr
#so what it'll do is...it will go through each page, go to the link and scrape the image from there 
#make a while loop 
#while loop variable 
#we love r 
#r = []
http = httplib2.Http()
#while loop variable 
page = 0 
another_variable = 0 
#first testing without while loop 
og_url = "https://theme.npm.edu.tw/opendata/DigitImageSets.aspx?lang=2&Key=^^11"
status, response = http.request(og_url)
#print(response)
for link in BeautifulSoup(response, 'html.parser', parse_only = SoupStrainer('a')):
	if link.has_key('href') and "DigitImageSets" in link['href'] and "/opendata/" not in link['href'] and "Key" in link['href']:
		#print(link)

		#here we will parse the links themselves and download them lmfao (this script will take such a long time :/)
		# i just use r for reference to see if everything is going well, now I will have to get the DigitImage thing 
		#idk if i can do the https thing with this kind of url...oh well 
		thing = "https://theme.npm.edu.tw/opendata/" + link['href']
		statusOne, responseOne = http.request(thing)
		#ok so this does get all the images 
		#because of this for loop everything is going wack so I have to make it so it doesn't do that 

		for funni in  BeautifulSoup(response, 'html.parser', parse_only=SoupStrainer(['img', 'src'])):
			if "pic.ashx" in funni['src']:
				another_variable = another_variable + 1
				print(another_variable)

				placeholder = funni['src']
				
				#print(placeholder)
				#so this does the right thing...time to see if it pulls the images lol lol lol 
				placeholder = "https://theme.npm.edu.tw/opendata/att/" + placeholder[(placeholder.index("=")+1):placeholder.index("&")]
				#print(placeholder)
				#print(placeholder)
				'''again = requests.get(placeholder)
				file = open("bruh" + str(another_variable) + ".jpg", "wb")
				file.write(again.content)
				#print("finished lmao")
				file.close()'''



				#print(placeholder)
				#wget.download(placeholder)



				#print(placeholder)
				#another = "https://theme.npm.edu.tw/opendata/att/" + placeholder[placeholder.index("ftp"):placeholder.index("jpg")]
				#print(another)
				#print(link['src'])


			#<img alt="" src="pic.ashx?qp=ftp/20211227/K2A000979N000000000PAC.jpg&amp;sizetype=2"/>

			#print(link)

#https://theme.npm.edu.tw/opendata/att/collectionPic/04014176/17020821.jpg
		

		#print(thing)

		#r.append(link['href'])
		#it is a string so I should be able to 
		#print(type(link['href']))
#print(r)


#page = requests.get(og_url)
#soup = BeautifulSoup(page.text, 'html.parser')
#for link in BeautifulSoup(page.text, )

#print(soup)
#this is a start..let's try to get a href 
#thing = soup.find_all('a', {'class' : "fancybo_xxxx fancybox.iframe"})
#print(thing)
#remember to get rid of amp! 
#thing = soup.find_all()
#print(thing)

#here is where i attempt to filter the links
#thing = soup.find_all('a')
#thing = soup.find_all('li')
#thing = soup.find_all('a', href = re.compile("DigitImageSets"))
#thing = soup.find_all(href=re.compile("DigitImageSets"))
#print(thing)


		
	#another = bruh[bruh.index("Url:"):bruh.index("Height:")]
	#print(bruh.find())
	#print(bruh.find("Height"))

	#print(bruh.find("Url:"))
	#print(bruh.split("Url"))
	#r.append(bruh)
	#print(bruh)

	#print(bruh)
	
	#r.append(obj[obj.index("http"):obj.index("/")])
#print(r)
#data = json.load(thing)
#this is pissing me off 
#print(r)

#for obj in thing:
	#json.loads(obj)
	#ast.literal_eval(obj)
	#r.append(ast.literal_eval(obj))
	#print(r)
	#object is a string yea? so we somehow have to parse the string Scroll-TIF-images/dzi-folder-2017-04-26-16_55_47 

	#print(obj)
	#ok so the obj part is indeed working 
	#i just need to parse out the Url 
	#print(obj)

#already an object :/ so let's do this 


#lets do this again..i love life 
#longest freakin url to exist ever I'm sorry lmfao 
#bonkers = []
#r = []
#og_url = 'https://scrolls.uchicago.edu/search?title=&field_artist_target_id=All&field_museum_target_id=All&field_culture_target_id=All&field_dynasty_target_id=All&field_theme_subject_target_id=63&field_image_source_target_id=All&field_scroll_id_value=&items_per_page=100'
#so what is happening here is that I have to parse out links from the thing and then try to find the image? i don't think the scroll is an image though 

'''page = requests.get(og_url)
soup = BeautifulSoup(page.text, 'html.parser')
print(soup)'''
#warning = soup.find_all('a', attrs={'href': re.compile("^http://")})
#print(warning)
'''for i in warning:
	r.append(i.attrs['src'])
print(r)'''




	

      		
		
	

	 #Get request on full_url

	
	#bonkers.append(thing)

'''book_container = warning.nextSibling.nextSibling
images = book_container.findAll('img')
print(images[0])'''
