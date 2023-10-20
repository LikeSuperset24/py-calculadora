# Utiliza una imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de tu proyecto al contenedor
COPY . /app

# Instala las dependencias de tu aplicación


# Especifica el comando que se ejecutará cuando se inicie el contenedor
CMD ["python", "main.py"]
