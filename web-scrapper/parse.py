from bs4 import BeautifulSoup
import requests

search = input("Enter search term:")
params = {"q": search}
r = requests.get("http://www.bing.com/search", params=params)

soup = BeautifulSoup(r.text, features="html.parser")

results1 = soup.find("ol", {"id": "b_results"})
links = results1.findAll("li", {"class": "b_algo"})

for item in links:
	item_text = item.find("a").text
	item_href = item.find("a").attrs["href"]
	
	if item_text and item_href:
		print(item_text) 
		print(item_href)

results2 = soup.findAll("div", {"class": "b_caption"})

for item in results2:
	text = item.find("p").text
	if text:
		print(text)
