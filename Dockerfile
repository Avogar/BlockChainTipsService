FROM python:3.8

RUN apt-get update && apt-get install -y python3-opencv zbar-tools

WORKDIR /tips-service

COPY . .

RUN pip3 install -r requirements.txt

CMD ["python3", "tips-service.py"]
