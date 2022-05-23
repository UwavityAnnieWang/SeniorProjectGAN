#!/usr/bin/env python3
#don't forget the shebang lmfao 
import shutil 
import requests
import urllib.request
import re
#import urllib3
import json
#import ast
from bs4 import BeautifulSoup
r = []
thing = open('hope.json')
#print(type(thing))
#this is a lost cause (for now) so going to work on getting taiwan dataset 
for obj in thing:
	bruh = obj.strip()
	#print(bruh)
	#print("hehehehehe")
	#might have to parse links and obtain authentication key from each of them? 
	if("Url:" in bruh):
		
		#bruh = bruh.strip(",")
		
		bruh = bruh[bruh.index("https"):bruh.index(",")]
		bruh = bruh.strip('"')
		print(bruh)
		
		
		porbe = requests.get(bruh)

		open(str(bruh), "wb").write(porbe.content)


		
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
