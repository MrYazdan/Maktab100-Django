FROM python:3

# cd /usr/src/app
WORKDIR /usr/src/app

# cp -r ./* /usr/src/app
COPY . .

ENV MODE prod

RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# -p 8080:8080
# EXPOSE 8080:8080 -> deprecated !

CMD ["gunicorn", "config.wsgi:application", "-b", "0.0.0.0:8080"]