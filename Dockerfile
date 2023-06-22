FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt .

ENV OPENAI_KEY=OPENAI_KEY
ENV ENGINE=text-davinci-003
ENV MAX_TOKENS=300
ENV TEMPERATURE=0.3

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]