FROM python:3.10-slim

WORKDIR /usr/src/app

COPY problems.py .

CMD ["python", "problems.py"]

ENTRYPOINT ["python", "problems.py"]
