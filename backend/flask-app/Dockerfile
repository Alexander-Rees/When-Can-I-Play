FROM python:3.9-slim-bullseye

WORKDIR /code

COPY src/requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 4000

CMD ["python", "app.py"]
