
FROM python:3.11-slim

WORKDIR /src/

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /src/compra_agora_scrapy/compra_agora_scrapy/spiders

CMD ["python", "main.py"]
