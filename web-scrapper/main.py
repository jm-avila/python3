from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os

def StartSearch():
	search = input("Search for:")
	params = {"q": search}

	r = requests.get("http://www.bing/images/search", params=params)

	soup = BeautifulSoup(r.text, "html.parser")
	links = soup.findAll("a", {"class": "thumb"})

	for item in links:
		try:
			img_obj = requests.get(item.attrs["href"])
			title = item.attrs["href"].split("/")[-1]
			try:
				img = Image.open(BytesIO(img_obj.content))
				img.save("./scrapped_images/", title, img.format)
			except:
				print("Could not save image.")
		except:
			print("Could not request image.")
	StartSearch()	

StartSearch()

