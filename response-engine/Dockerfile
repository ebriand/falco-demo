FROM python:3-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY server.py /app/server.py

EXPOSE 8080

ENTRYPOINT [ "/app/server.py" ]

