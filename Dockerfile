FROM python:3.8
ADD . /kairos
WORKDIR /kairos
RUN pip install -r requirements.txt