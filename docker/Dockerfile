FROM python:3.11-slim

# Configurar el directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios desde la carpeta 2
COPY  requirements.txt .
COPY  . .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Configurar PYTHONPATH para que encuentre los módulos correctamente
ENV PYTHONPATH=/app

# Exponer el puerto usando la variable de entorno
EXPOSE ${API_PORT}

# Comando para iniciar la aplicación
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${API_PORT}"]