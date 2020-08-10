from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

#need average time between goals
#need 

#change this to fstring, loop through years in URL
url = 'https://www.hockey-reference.com/leagues/NHL_2019_games.html'
filename = 'hr-data2019.csv'
page = requests.get(url)


if page.status_code == requests.codes.ok:
	soup = BeautifulSoup(page.text, 'lxml')
	gamesTable = soup.find_all('th', {'class': 'left', 'data-stat': 'date_game'})
	for game in gamesTable:
	 	link = game.find('a')
	 	if link:
	 		gameURL = link.get('href')
	 		gamePage = requests.get('https://www.hockey-reference.com'+gameURL)
	 		if gamePage.status_code == requests.codes.ok:
	 			
	 	

			