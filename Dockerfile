FROM python:3.11.3-bullseye

WORKDIR /app
#ENV FLASK_HOST="0.0.0.0"
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
ENV FLASK_APP=app.py

COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh
RUN apt-get update && apt-get install -y netcat

ENTRYPOINT ["entrypoint.sh"]
