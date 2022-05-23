#!/usr/bin/env python3
#don't forget the shebang lmfao 
import requests
import httplib2
import os.path
from bs4 import BeautifulSoup, SoupStrainer
#this one will be the scraper fr
#so what it'll do is...it will go through each page, go to the link and scrape the image from there 
#make a while loop 
#while loop variable 

http = httplib2.Http()
#while loop variable currently commented out for my own sanity  
#how much data should i download? 
page = 1
another_variable = 0 
while page != 31:
#first testing without while loop 
	og_url = "https://theme.npm.edu.tw/opendata/DigitImageSets.aspx?lang=2&Key=^^11&pageNo=" + str(page)
	status, response = http.request(og_url)
	#print(response)
	for link in BeautifulSoup(response, 'html.parser', parse_only = SoupStrainer('a')):
		if link.has_key('href') and "DigitImageSets" in link['href'] and "/opendata/" not in link['href'] and "Key" in link['href']:
			another_variable=another_variable+1
			file_name = "bruh" + str(another_variable) + ".jpg"
			#print(link)

			#here we will parse the links themselves and download them lmfao (this script will take such a long time :/)
			# i just use r for reference to see if everything is going well, now I will have to get the DigitImage thing 
			#idk if i can do the https thing with this kind of url...oh well 
			thing = "https://theme.npm.edu.tw/opendata/" + link['href']
			
			statusOne, responseOne = http.request(thing)
			#basically it has found a valid link and now is parsing it 
			for funni in BeautifulSoup(responseOne, 'html.parser', parse_only=SoupStrainer(['img', 'src'])):
				#IT WORKS MUAHAHAHAHAHAHAHAHAHA 
				if "https" in funni['src'] and not os.path.isfile(file_name):
					again = requests.get(funni['src'])
					file = open(file_name, "wb")
					file.write(again.content)
					file.close()
	page = page+1


				