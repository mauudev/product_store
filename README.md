# Product Store

Consta de dos servicios, el frontend y backend.

## Despliegue via docker-compose

Dirigirse a la carpeta `infra` y ejecutar:

```bash
docker compose up --build
```

Luego la aplicacion estara ejecutandose en `http://localhost:8080`
El API server en `http://localhost:8000/docs`

## Inicializacion Manual

El manejador de dependencias del backend es `Poetry`, se debe instalar para manejar todas las dependencias.

Para iniciar el API server del backend, dirigirse a la carpeta `backend` y ejecutar los siguientes comandos:

La aplicacion usa Postgres como motor de base de datos, por lo que es necesario levantar el contenedor de docker via `docker-compose`.
Dirigirse a la carpeta `infra` y ejecutar:

```bash
docker compose up
```

Una vez levantado el contenedor, necesitamos crear las tablas, para ello ejecutar dentro de la carpeta `backend`:

```bash
make migrate
```

Ahora podemos iniciar el servidor:

```bash
make shell # crea un entorno virtual de python
make install # instala todas las dependencias
make run # inicia el server
```

Para iniciar el frontend, dirigirse a la carpeta `frontend` y ejecutar el siguiente comando:

```bash
npm run dev
```
