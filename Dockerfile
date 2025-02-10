FROM python:3.8-slim-buster
WORKDIR /app
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . /app
CMD ["streamlit", "run", "appStreamlit.py"]
