
FROM python:3.11-slim

WORKDIR /src/

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

#pacotes básicos e bibliotecas necessárias para o Playwright
RUN apt-get update && apt-get install -y \
    libglib2.0-0 libnss3 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdrm2 \
    libexpat1 libgbm1 libasound2 libpangocairo-1.0-0 libx11-6 libxcomposite1 \
    libxdamage1 libxext6 libxfixes3 libxrandr2 libxkbcommon0 libwayland-client0 \
    libwayland-cursor0 libwayland-egl1 libgdk-pixbuf2.0-0 libgtk-3-0 libxinerama1 \
    libdbus-1-3 libnspr4 libsm6 shared-mime-info fonts-liberation \
    libpango-1.0-0 libcairo2 libasound2 libatspi2.0-0 fonts-noto-color-emoji \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Instala Playwright e os navegadores
RUN pip install playwright
RUN playwright install

COPY . .

WORKDIR /src/servimed_scrapy/servimed_scrapy/spiders

#CMD ["python", "main.py","511082"]
CMD ["tail", "-f", "/dev/null"]