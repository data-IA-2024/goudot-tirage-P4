from modules.temitableaux import teamatize
import pandas as pd

df = pd.read_csv('list_p4.csv')

teams = teamatize(df['Prénom'].values, 4)

for team in teams:
    print(team)

