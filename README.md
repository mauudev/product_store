# Product Store

Consta de dos servicios, el frontend y backend.
El manejador de dependencias del backend es `Poetry`, se debe instalar para manejar todas las dependencias.

Para iniciar el API server del backend, dirigirse a la carpeta `backend` y ejecutar los siguientes comandos:

```bash
make shell # crea un entorno virtual de python
make install # instala todas las dependencias
make run # inicia el server
```

Para iniciar el frontend, dirigirse a la carpeta `frontend` y ejecutar el siguiente comando:

```bash
npm run dev
```
