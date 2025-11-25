FROM python:3.14-slim-bookworm

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=withfeathers/server.py

EXPOSE 8000

CMD ["gunicorn", "--chdir", "withfeathers", "-b", "0.0.0.0:8000", "server:app"]
