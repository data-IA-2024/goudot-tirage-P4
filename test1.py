import csv, pandas, os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

print('DATAFILE=', os.getenv('DATAFILE'))
print('PATH', os.getenv('PATH'))