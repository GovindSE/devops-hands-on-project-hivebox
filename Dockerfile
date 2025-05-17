FROM python:3.12-slim
WORKDIR  /app

copy . .

RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
CMD ["flask","run"]
