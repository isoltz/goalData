from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv


# scraping the goal data from https://www.icydata.hockey/
# hardcoded pageCount to range of 1-32 based on the URLs on the website
for pageCount in range(1,32):
	filename = f'dataset{pageCount}.csv'
	url = f'http://www.icydata.hockey/player_stats/{pageCount}/goals'
	page = requests.get(url)

	with open(filename, 'w+') as csvFile:
		csvWriter = csv.writer(csvFile)
		if page.status_code == requests.codes.ok:
			soup = BeautifulSoup(page.text, 'lxml')
			goalsTable = soup.find_all('tr')
			for goal in goalsTable:
				cols = goal.find_all('td')
				attributes = [ele.text.strip() for ele in cols]
				csvWriter.writerow(attributes)
