FROM python:3

# cd /usr/src/app
WORKDIR /usr/src/app

# cp -r ./* /usr/src/app
COPY . .

RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ENV MODE ${MODE}

CMD ["gunicorn", "config.wsgi:application", "-b", "0.0.0.0:8000"]