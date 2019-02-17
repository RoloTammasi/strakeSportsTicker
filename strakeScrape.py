#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup
import requests

def getData():
    
    r  = requests.get(url)
    data = r.text
    return BeautifulSoup(data, "lxml")

url = "https://www.strakejesuit.org/athletics#"
events = []
scroll = ""

soup = getData()

for article in soup.findAll("article"):
    
    if article.find("span", class_="fsAthleticsScore") is not None:

        event = article.find(class_="fsDate")["datetime"][:10] + " "

        event += article.find("a", class_="fsAthleticsEventDetailLink").text + " "

        try: 
            event += article.find("span", class_="fsAthleticsVs").text + " "
        except:
            pass

        event += article.find("div", class_="fsAthleticsOpponentNames").text + " "

        try:
            event += article.find("span", class_="fsAthleticsResult").text + " "
        except:
            pass
            
        try: 
            event += article.find("span", class_="fsAthleticsScore").text + " "
        except:
            pass

        event = event.replace('\n', '')
        
        events.append(event + " || ")

for event in events:
    scroll += event

with open("strake_sports_ticker.txt", "w") as f:
    f.write(scroll)
f.close()
