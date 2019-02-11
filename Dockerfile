FROM python:3.6-alpine
RUN mkdir -p /opt/tornado-file-storage
COPY . /opt/tornado-file-storage
WORKDIR /opt/tornado-file-storage
RUN pip install -r requirements.txt
EXPOSE 8888
ENTRYPOINT ["python3", "main.py"]
