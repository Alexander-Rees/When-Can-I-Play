FROM ubuntu:latest

RUN apt-get update && apt-get install -y sqlite3

COPY init.sql init.sql

CMD ["sqlite3", "when_can_i_play.db", ".read init.sql"]
