FROM python:3.9

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app

EXPOSE 80
EXPOSE 5678

# CMD ["python", "-m", "debugpy", "--listen", "0.0.0.0:5678", "--wait-for-client", "app.main"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]

