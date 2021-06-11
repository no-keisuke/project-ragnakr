FROM python:3.9.5-slim-buster

COPY . /app
WORKDIR /app

RUN apt-get update
RUN apt-get install -y gcc

RUN pip install -r requirements.txt

# for production
# CMD [ "gunicorn", "-b", ":8080", "app:app" ]

# for development
CMD [ "python", "app.py" ]
