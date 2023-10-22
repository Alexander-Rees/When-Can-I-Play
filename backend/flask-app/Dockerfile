# Working from Python version 3.9
FROM python:3.9-slim-bullseye

# setting the working directory inside the container to /code
WORKDIR /code

# copying the requirements.txt file from the host system to
# inside the container
COPY src/requirements.txt requirements.txt

RUN apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config

# install requirements inside the container using pip
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install flask
RUN pip install mysqlclient
RUN pip install flask-mysqldb

# expose port 4000 from the container
EXPOSE 4000

# tell the container to run the flask application
CMD ["python", "app.py"]
