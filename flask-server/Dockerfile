# FROM tiangolo/uwsgi-nginx-flask:python3.6

# COPY requirements.txt /

# WORKDIR /

# RUN pip install -r ./requirements.txt --no-cache-dir

# COPY app/ /app/

# WORKDIR /app

# ENV FLASK_APP=app.py
# CMD flask db upgrade && flask run -h 0.0.0.0 -p 5000


# python:alpine is 3.{latest}
FROM python:alpine 
LABEL maintainer="Mohammad Ahmad"

# RUN pip install flask
COPY requirements.txt /

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

WORKDIR /
# RUN pip install -r ./requirements.txt --no-cache-dir
COPY app/ /app/
WORKDIR /app/app/
# ENV FLASK_APP=app.py
# CMD flask db upgrade && flask run -h 0.0.0.0 -p 5000



# RUN pip install -r requirements.txt
# RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
# ENTRYPOINT ["python", "app.py"]