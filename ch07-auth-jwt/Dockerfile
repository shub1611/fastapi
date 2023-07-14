FROM python:3.10

WORKDIR /app
COPY requirements.txt /app
RUN pip install --upgrade pip && pip install -r /app/requirements.txt
RUN apt-get update && apt-get install vim -y
EXPOSE 8080
COPY ./ch07-auth-jwt/ /app
# CMD ["ls", "-l"]
CMD ["python", "main.py"]