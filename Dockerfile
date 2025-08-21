# Imagen base de Python
FROM python:3.11-slim

# Crear carpeta de trabajo dentro del contenedor
WORKDIR /code

# Instalar dependencias de sistema (opcional, útil para psycopg2 y compilaciones)
RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

# Copiar archivo de dependencias
COPY requirements.txt /code/requirements.txt

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r /code/requirements.txt

# Copiar todo el código del proyecto
COPY . /code

# Comando por defecto para arrancar FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
