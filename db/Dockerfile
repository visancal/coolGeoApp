FROM postgis/postgis:14-3.1-alpine
MAINTAINER Vicent Sanjaime 

ENV POSTGRES_USER coolgeoapp
ENV POSTGRES_PASSWORD coolgeoapp
ENV POSTGRES_DB coolgeoapp

ADD a.sql /docker-entrypoint-initdb.d/
ADD b.sql /docker-entrypoint-initdb.d/
ADD c.sql /docker-entrypoint-initdb.d/