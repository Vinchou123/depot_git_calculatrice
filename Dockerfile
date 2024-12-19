FROM python:3.10-slim

WORKDIR /app

COPY server.py /app/server.py


EXPOSE 6767

CMD ["python", "server.py", "--port", "6767"]
