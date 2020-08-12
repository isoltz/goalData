import pandas as pd
import numpy as np
import csv
import glob


def periodTransform(string):
	#excludes OT for simplicity
	if string == '1st Period':
		return 1
	elif string == '2nd Period':
		return 2
	elif string == '3rd Period':
		return 3
	else:
		return np.nan

df = pd.concat((pd.read_csv(f) for f in glob.glob('hrData/*.csv')))
df['period'] = df['period'].apply(periodTransform)
df['timeInSecs'] = [int(minutes) * 60 + int(seconds) for minutes, seconds in df['time'].str.split(':')]
df['globalTime'] = df.apply(lambda row: ((row.period - 1) * (20 * 60)) + row.timeInSecs, axis = 1) 
df['strength'] = df['strength'].replace(np.NaN, 'EVEN')

df = df[df.season != 2013]

totalGoals = df.matchup.count()

# back of the envelope math, each team plays 82 games in a season, two teams in each game, ~30 teams,
# so 82*15*9 (9 seasons being evaulated) ~= 11,000
totalGames = len(df.groupby(['matchup']))

totalSeconds = totalGames * 20 * 60

goalFreq = totalGoals/totalSeconds




#frequency chart broken down by minutes, seconds
# get goals per season and total seconds per season for each season
# get goals within 60 seconds, total spans of 60 seconds after every goal (might just be total goals * 60)

# could get average goals per season, average seconds per season, the find average goals per second
df1 = df[(df.period.notnull()) & (df.strength == 'EVEN')].groupby(['season']).size().reset_index(name='count') 
#print(df1)

#print(len(df[(df.period.notnull()) & (df.strength == 'EVEN')]))

# a good 2000 OT goals, 20,000 PP goals
