FROM python:3.7

RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "/app/kube.py"]












# FROM python:3.7

# RUN mkdir /app
# # Setting Home Directory for containers
# WORKDIR /app
# # Installing python dependencies
# COPY requirements.txt /app

# RUN pip install -r requirements.txt
# # Copying src code to Container
# COPY . /app
# # Application Environment variables
# ENV APP_ENV development
# # Exposing Ports
# EXPOSE 5000
# # Running Python Application
# CMD ["python", "/app/main.py"]