FROM python:3.5
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

ADD . /code/
RUN chmod +x boot.sh

CMD ["./boot.sh"]
