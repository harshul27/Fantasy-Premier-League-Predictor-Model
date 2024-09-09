import requests, json
from pprint import pprint
import pandas as pd
base_url = 'https://fantasy.premierleague.com/api/'
r = requests.get(base_url+'bootstrap-static/').json()

pd.set_option('display.max_columns', None)
# create players dataframe
players = pd.json_normalize(r['elements'])
pprint(players[['id', 'web_name', 'team', 'element_type']].head())
#teams
teams = pd.json_normalize(r['teams'])
pprint(teams)
#positions
positions = pd.json_normalize(r['element_types'])
pprint(positions.head())
#combine data into a dataframe
df = pd.merge(
    left=players,
    right=teams,
    left_on='team',
    right_on='id'
)
df.merge(
    positions,
    left_on='element_type',
    right_on='id'
)
#pprint(df[['first_name', 'second_name', 'name']].head())
df = df.rename(
    columns={'name':'team_name', 'singular_name':'position_name'}
)
pprint(df[['first_name', 'second_name', 'team_name', 'position_name']].head())

#per gameweek record


