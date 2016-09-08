FROM python:3.4

RUN useradd -m -s /bin/false app
RUN mkdir -p /usr/src/app
RUN chown -R app /usr/src/app

WORKDIR /usr/src/app/

RUN pip install --upgrade pip virtualenv
COPY requirements.txt /usr/src/app
RUN pip install -r requirements.txt

COPY . /usr/src/app/
RUN python setup.py develop

USER app

EXPOSE 8080
CMD [ "asyncapp" ]
