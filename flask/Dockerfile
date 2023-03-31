FROM python:latest

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

RUN apt-get update -y && apt-get install -y python3 python3-pip

COPY app.py /app

EXPOSE 5000

CMD ["python3", "app.py"]
