FROM python:3.5-jessie

RUN apt-get update && apt-get install -y git ca-certificates net-tools
WORKDIR /root
RUN mkdir multisensorsplatform
COPY ./ ./multisensorsplatform/
RUN pip install -qr ./multisensorsplatform/requirements.txt
ENTRYPOINT ["python3", "./multisensorsplatform/webserver.py", "--port", "8080"]

EXPOSE 8080