FROM debian:stretch-slim

RUN apt-get update && \
    apt-get install -y python3-pip python3-dev build-essential
COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]

CMD ["app.py"]
