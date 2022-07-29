FROM python:latest

WORKDIR /app

RUN apt-get update && \
    apt-get install -y gdal-bin libgdal-dev libsqlite3-mod-spatialite && \
	apt-get clean

COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# ARG FLASK_APP=api
# ARG FLASK_ENV=development
# THE BELOW WILL BE COVERED BY THE ARGS IN THE docker-compose.yaml FILE!
COPY . /app

CMD ["pytest","."]
# CMD ["flask","run","--host","0.0.0.0","--port","5000"]
