# Use a imagem base do Python
FROM python:3.11-slim

# Defina o diretório de trabalho
WORKDIR /usr/

# Copie os arquivos de dependências
COPY requirements.txt ./

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código para o contêiner
COPY . .

