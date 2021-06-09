FROM python:3.8

ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
ADD prometheus-exporter.py /app/app.py


CMD ["python", "/app/app.py"]
