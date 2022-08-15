FROM python:latest

WORKDIR /job

COPY requirements.txt /job
RUN pip install -r requirements.txt

COPY job.py /job
CMD python job.py

