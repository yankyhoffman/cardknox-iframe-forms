FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y libpq-dev build-essential && apt-get clean

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && rm requirements.txt

RUN mkdir /app
WORKDIR /app

EXPOSE 8000

CMD ["./manage.py", "runserver", "0.0.0.0:8000"]
