FROM python:3.6-slim

COPY requirements.txt /tmp/

RUN pip3 install -r /tmp/requirements.txt

COPY app.py /opt 

EXPOSE 5000

CMD python3 /opt/app.py
