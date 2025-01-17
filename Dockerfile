FROM python:3.9.2-slim-buster

WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app

RUN apt -qq update && apt -qq install -y python3-dev mediainfo ffmpeg build-essentials

COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt

#CMD ["bash","pkg.sh"]
CMD ["bash","run.sh"]
