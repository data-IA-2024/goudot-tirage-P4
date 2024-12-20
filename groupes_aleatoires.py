import csv, os, random, sys, logging
from dotenv import load_dotenv
import pandas as pd

load_dotenv()  # take environment variables from .env.

#Librairie logging pour remplcer le debuggage par print()
logging.basicConfig(level=logging.DEBUG)

#logging.debug('msg go in log file')
#logging.info('')
#logging.warning('')
#logging.error('')
pd.Dataframe

DATAFILE = os.getenv('DATAFILE')
logging.debug(f'mon fichier : {DATAFILE=}')
logging.debug(f'{sys.argv=}')
try:

    if len(sys.argv) > 1:
        N = int(sys.argv[1])
    else:
        N = int(input('Taille des groupes ? '))
    logging.debug(f'{N=}')
except:
    logging.error(f"Votre donnée n'est pas entière !")
    quit()

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

    