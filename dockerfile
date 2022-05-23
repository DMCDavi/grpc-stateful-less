FROM python:3.8.10

WORKDIR /usr/app

RUN pip install --upgrade pip

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "./examples/python/helloworld/greeter_server.py"]