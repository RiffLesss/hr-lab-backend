FROM python:3.8

RUN mkdir -p /usr/src/hr-lab
WORKDIR /usr/src/hr-lab
COPY requirements.txt /usr/src/hr-lab/


RUN python3 -m pip install -r requirements.txt --no-cache-dir

COPY . /usr/src/hr-lab

ENTRYPOINT ["sh", "prod_run.sh"]
