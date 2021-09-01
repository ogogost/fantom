FROM python:3.7.1

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/
COPY requirements.txt requirements.txt


# CMD ["python", "test9.py"]
CMD ["python", "Postgres/mappool_3.py"]
CMD ["python", "Postgres/client6.py"]