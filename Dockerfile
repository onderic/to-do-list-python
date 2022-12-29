FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD python main.py
FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD python main.py
