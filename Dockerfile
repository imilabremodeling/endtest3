FROM python:3.8
VOLUME ["endtest"]
WORKDIR /app
COPY . .
CMD ["python", "endtest.py"]
