FROM ubuntu:22.04

ENV LANG="en_US.UTF-8"
ENV LANGUAGE="en_US:en"
ENV LC_ALL="en_US.UTF-8"
ENV PYTHONUNBUFFERED=1

RUN set -eux; \
	apt-get update; \
	apt-get install -y gosu; \
	rm -rf /var/lib/apt/lists/*; \
# verify that the binary works
	gosu nobody true

RUN apt-get update && apt-get install -y\
    gettext \
    locales \
    python3 \
    python3-dev \
    python3-setuptools \
    python3-pip \
    python3-enchant graphviz \
    build-essential && \
#    libldap2-dev \
#    libsasl2-dev \
#    tox \
#    lcov \
#    valgrind \
#    ldap-utils && \
    apt-get clean

RUN locale-gen en_US.UTF-8

COPY ./requirements.txt /project/
WORKDIR /project

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt
