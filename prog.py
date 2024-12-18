import csv, os, random, sys, logging
from dotenv import load_dotenv
import pandas as pd

load_dotenv()  # take environment variables from .env.

logging.basicConfig(level=logging.DEBUG)

DATAFILE = os.getenv('DATAFILE')
logging.debug(f'{DATAFILE=}')
logging.debug(f'{sys.argv=}')

try:
    if len(sys.argv)>1:
        N = int(sys.argv[1])
    else:
        N = int(input('Taille des groupes ? '))
except:
    logging.error(f"Votre données n'est pas entière !")
    quit()

logging.debug(f'{N=}')

df = pd.read_csv(DATAFILE)
df = df[df.type != 'prof']
#print(df)

noms = df['Nom']
liste_nom = noms.values
random.shuffle(liste_nom)
logging.info(liste_nom)

for i in range(len(liste_nom)):
    if i%N == 0 : print('----------------------')
    print(liste_nom[i])