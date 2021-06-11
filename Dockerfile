# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /code
#ENV FLASK_APP=app.py
#ENV FLASK_RUN_HOST=0.0.0.0
#RUN apk add --no-cache gcc musl-dev linux-headers
RUN apk add --no-cache python
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["python", "dbInit.py"]
CMD ["python", "app.py"]