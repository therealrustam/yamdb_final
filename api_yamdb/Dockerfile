FROM python:3.7-slim 

COPY ./ /app

WORKDIR /app

COPY api_yamdb/requirements.txt pwd

RUN pip3 install -r api_yamdb/requirements.txt --no-cache-dir

WORKDIR /app/api_yamdb

CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000"] 
