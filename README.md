# Aplicacion de Tienda de Productos

Este repositorio contiene una aplicacion que simula una tienda de productos.
La aplicacion se divide en dos partes: el frontend y el backend.
Ambos componentes se despliegan utilizando Docker Compose para una facil configuracion y despliegue.

## Estructura del Repositorio

- `frontend`: La interfaz de usuario de la tienda, desarrollada en ReactJS con Vite.
- `backend`: El servidor de la API, construido con FastAPI en Python, que interactua con una base de datos PostgreSQL utilizando SQLAlchemy con la extensión asyncio.
- `infra`: Archivos Docker Compose y scripts para la orquestación de contenedores.

## Requisitos Previos

- Docker: Asegúrate de tener Docker instalado en tu máquina.
- Docker Compose: Instala Docker Compose para facilitar el despliegue de los servicios.

## Configuracion y Despliegue

Clonar el repo.
Dentro del directorio infra, ejecuta el siguiente comando para iniciar los contenedores:

```bash
docker compose up -d --build
```

Una vez que los contenedores estén en ejecución, puedes acceder al frontend en http://localhost:8080 y al backend en http://localhost:8000/docs.
