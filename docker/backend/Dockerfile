################################
# Base build Image
################################  
FROM python:3.10.1-bullseye AS compile-image
ARG SWEETHOME_PRODUCTION
RUN apt-get -qq update && \
    apt-get -y install --no-install-recommends gcc libssl-dev gdal-bin

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# build python dependencies    
COPY ./requirements.txt ./requirements.dev.txt /
RUN /usr/local/bin/python -m pip install --upgrade pip && \
    pip install -r requirements.txt
RUN if [ "${SWEETHOME_PRODUCTION}" = "False" ] ; then pip install -r requirements.dev.txt; fi

################################
# Image
################################    
FROM python:3.10.1-slim-bullseye as runtime-image
COPY --from=compile-image /opt/venv /opt/venv

# TODO: gettext are only needed for dev environment
RUN apt-get -qq update && \
    apt-get -y install --no-install-recommends libssl-dev gdal-bin netcat && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# set work directory
WORKDIR /opt/sweethome

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH="/opt/venv/bin:$PATH"