FROM python:3.6.5

WORKDIR /src
COPY . /src/

RUN pip3 install -r /src/requirements.txt

EXPOSE 5000
