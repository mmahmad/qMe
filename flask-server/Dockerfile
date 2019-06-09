# FROM ubuntu:latest
# MAINTAINER Mohammad Ahmad "mohammad.moaaz.ahmad@gmail.com"
# RUN apt-get update -y
# RUN apt-get install -y python-pip python-dev build-essential
# COPY . /app
# WORKDIR /app
# RUN pip install -r requirements.txt
# ENTRYPOINT ["python"]
# CMD ["app.py"]

# python:alpine is 3.{latest}
FROM python:alpine 
LABEL maintainer="Mohammad Ahmad"
RUN pip install flask
COPY . /app
WORKDIR /app
# RUN pip install -r requirements.txt
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
# ENTRYPOINT ["python", "app.py"]