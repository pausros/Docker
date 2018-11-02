FROM python:3.6-slim
LABEL maintainer="ajgil"

RUN useradd -ms /bin/bash runner
USER runner
WORKDIR /home/runner

COPY very-useful.py /opt/
ENV ARGS=""

CMD python3 /opt/very-useful.py $ARGS
