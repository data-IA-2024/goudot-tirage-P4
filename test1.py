import csv, pandas, os
from dotenv import load_dotenv

load_dotenv()

file = os.getenv('DATAFILE')

csv = csv.reader(open(file, 'r'))

for row in csv:
    print(row)

print('OK')