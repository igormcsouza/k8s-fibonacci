FROM python:3.8-slim

COPY requirements.txt /opt/requirements.txt
RUN pip install -r /opt/requirements.txt

EXPOSE 5000

WORKDIR /app

COPY app.py /app/app.py

CMD FLASK_APP=app:app flask run --host=0.0.0.0