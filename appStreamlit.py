import streamlit as st
import pandas as pd
import dotenv, logging, os

dotenv.load_dotenv()  # take environment variables from .env.

logging.basicConfig(level=logging.DEBUG)

DATAFILE = os.getenv('DATAFILE')
logging.debug(f'{DATAFILE=}')

st.write("""
# Tirage au sort
""")

df = pd.read_csv(DATAFILE)
st.dataframe(df)