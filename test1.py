import csv, os, random, sys
from dotenv import load_dotenv
import pandas as pd

load_dotenv()  # take environment variables from .env.

DATAFILE = os.getenv('DATAFILE')
print(f'{DATAFILE=}')
print(f'{sys.argv=}')

N = int(input('Taille des groupes ? '))
print(f'{N=}')

df = pd.read_csv(DATAFILE)
df = df[df.type != 'prof']
#print(df)

noms = df['Nom']
liste_nom = noms.values
random.shuffle(liste_nom)
print(liste_nom)

for i in range(len(liste_nom)):
    if i%N == 0 : print('----------------------')
    print(liste_nom[i])