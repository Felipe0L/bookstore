# syntax=docker/dockerfile:1
FROM python:3.12.1-slim

# Instalações básicas
RUN apt-get update && apt-get install --no-install-recommends -y \
    curl \
    build-essential \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Instala o Poetry
RUN pip install poetry

# Define o diretório de trabalho
WORKDIR /opt/pysetup

# Copia os arquivos de dependências primeiro (para cache)
COPY pyproject.toml poetry.lock README.md ./

# Instala apenas as dependências (sem tentar instalar o projeto)
RUN poetry install --no-root && poetry show

# Copia o restante do projeto
COPY . .

# Expõe a porta (caso use runserver)
EXPOSE 8000

# Comando padrão (ajuste se usar outro servidor)
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]

