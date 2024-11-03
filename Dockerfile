FROM python:3.11.5-alpine

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 9089
ENTRYPOINT [ "python" ]
CMD ["server.py" ]