from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

#need average time between goals
#need 

#change this to fstring, loop through years in URL


def parseSeason(url, filename):
	page = requests.get(url)
	with open(filename, 'w+') as csvFile:
		csvWriter = csv.writer(csvFile)
		if page.status_code == requests.codes.ok:
			soup = BeautifulSoup(page.text, 'lxml')
			gamesTable = soup.find_all('th', {'class': 'left', 'data-stat': 'date_game'})[1:]
			for game in gamesTable:
			 	link = game.find('a')
			 	if link:
			 		gameDate = link.text
			 		print(gameDate)
			 		gameURL = link.get('href')
			 		gamePage = requests.get('https://www.hockey-reference.com'+gameURL)
			 		if gamePage.status_code == requests.codes.ok:
			 			scoringSoup = BeautifulSoup(gamePage.text, 'lxml')
			 			matchup = scoringSoup.find('h1').text
			 			matchup = matchup.split('—')
			 			matchup = matchup[0].strip('Box Score') + ' ' + gameDate
			 			scoringTable = scoringSoup.find('table', {'id': 'scoring'})
			 			elts = scoringTable.find_all('tr')
			 			for tr in elts:
			 				attrs = []
			 				cols = tr.find_all('td')
			 				if cols:
			 					attrs.append(matchup)
			 					attrs.append(period)
				 				#time
				 				attrs.append(cols[0].text)
				 				#team
				 				attrs.append(cols[1].find('a').text)
				 				#strength 
				 				attrs.append(cols[2].text.strip())
			 					csvWriter.writerow(attrs)
			 				else:
			 					period = tr.text
			 	break
			 	


for i in range(0,10):
	url = f'https://www.hockey-reference.com/leagues/NHL_201{i}_games.html'
	filename = f'hr-data201{i}.csv'
	parseSeason(url, filename)
	break

	 	

			