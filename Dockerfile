FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install flask

COPY ./app.py ./app.py

CMD ["python3", "app.py"]
