FROM python:3.7

ADD /requirements.txt /app/

WORKDIR /app

RUN pip install -r requirements.txt

ADD . /app/

EXPOSE 5000

CMD ["python", "/app/kube.py"]
