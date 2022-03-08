
FROM python:3.7-slim

COPY ./ /app

WORKDIR /app

COPY requirements.txt pwd

RUN pip3 install -r requirements.txt --no-cache-dir

CMD ["gunicorn", "api_yamdb.wsgi", "--bind", "0:8000"]
