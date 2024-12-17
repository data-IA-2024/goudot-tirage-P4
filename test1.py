import csv
import os
import random
from dotenv import load_dotenv
import pandas as pd

NB_PERSONNES_PAR_GROUPES = int(input("Combien de personnes par groupe ? "))


load_dotenv()
file = os.getenv('DATAFILE')
df = pd.read_csv(file)

nb_groupes = len(df) // NB_PERSONNES_PAR_GROUPES
df["groupe"] = None

for i in range(nb_groupes):
    group = df[df['groupe'].isnull()].sample(NB_PERSONNES_PAR_GROUPES)
    group['groupe'] = i
    df.loc[group.index, 'groupe'] = i


print(df)

print("\n")

for i in range(nb_groupes):
    group = df[df['groupe'] == i]
    print(f"Groupe {i}:")
    print(group['Nom'].values)