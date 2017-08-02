FROM python:3.6.2-alpine
LABEL maintainer "Arata Furukawa <info@ornew.net>"

COPY minecraft-status.py /minecraft-status.py
ENTRYPOINT [ "python", "/minecraft-status.py" ]
