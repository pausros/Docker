FROM python:3.6-slim

LABEL maintainar='ajgil'

COPY requirements.txt /tmp/

RUN pip3 install -r /tmp/requirements.txt

COPY app.py /opt

EXPOSE 8050

CMD python3 /opt/app.py
