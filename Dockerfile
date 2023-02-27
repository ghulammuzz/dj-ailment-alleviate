FROM python:latest

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY req.txt req.txt

RUN pip install -r req.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]

