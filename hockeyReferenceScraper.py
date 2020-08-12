from bs4 import BeautifulSoup
import requests
import csv


def parseSeason(url, filename, season):
	page = requests.get(url)
	with open(filename, 'w+') as csvFile:
		csvWriter = csv.writer(csvFile)
		if page.status_code == requests.codes.ok:
			header = ['matchup','season','period','time','team','strength']
			csvWriter.writerow(header)
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
			 			scoringTable = scoringSoup.find('table', {'id': 'scoring'})
			 			elts = scoringTable.find_all('tr')
			 			for tr in elts:
			 				attrs = []
			 				cols = tr.find_all('td')
			 				if cols:
			 					attrs.append(matchup)
			 					attrs.append(season)
			 					attrs.append(period)
				 				#time
				 				attrs.append(cols[0].text)
				 				#team
				 				attrs.append(cols[1].find('a').text)
				 				#strength 
				 				# don't want penalty shots
				 				if 'PS' not in cols[2].text:
				 					attrs.append(cols[2].text.strip())
			 					csvWriter.writerow(attrs)
			 				else:
			 					period = tr.text
			 					# don't want shootout goals
			 					if period == 'Shootout':
			 						break
			 	
			 	


for i in range(0,10):
	season = f'201{i}'
	url = f'https://www.hockey-reference.com/leagues/NHL_{season}_games.html'
	filename = f'hrData/hr-{season}.csv'
	parseSeason(url, filename, season)

	

	 	

			