FROM python:3.11-slim

WORKDIR /moneytolia_homework

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "moneytolia_homework.asgi:application", "--host", "0.0.0.0", "--port", "8000", "--reload"]
