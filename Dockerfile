FROM python:3.10-slim
WORKDIR /spygram

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY api api/
COPY data data/
COPY feed feed/
COPY logs logs/
COPY static static/
COPY app.py .
COPY config.py .

CMD flask run -h 0.0.0.0 -p 80