FROM python:3.10-alpine AS builder

COPY ./src /app
COPY ./requirements.txt /app/requirements.txt
RUN cd /app && pip install -r requirements.txt

# FROM python:3.10-alpine
# COPY --from=builder /app /app

# ENTRYPOINT [ "python", "/app/main.py" ]