# Workshop demo App Backend

Aplicación Python que utiliza Flask para crear un Api Backend que escucha peticiones para leer y escribir de una base de datos PostgreSQL.

## Descripción de la funcionalidad

La aplicación es un API Backend que escucha peticiones en el puerto 5000. Consta de dos rutas: ```/send```  y  ```/get```

- Cuando se invoca la ruta ```/send``` la aplicación espera recibir, mediante un ```POST``` un Json con los datos que va a grabar en la base PostgreSQL

- Cuando se invoca la ruta ```/get``` la aplicación trae de la base PostgreSQL los últimos 5 registros grabados y devuelve un Json con la información

Se puede probar el funcionamiento de la aplicación con los siguientes comandos:

```bash
> curl -X POST -d @example.json https://<URL API>:5000/send
```

o 

```bash
> curl -X GET https://<URL API>:5000/get
```

## Instalación de la aplicación

La aplicación tiene algunas dependencias que deben ser instaladas antes de poder ser ejecutada. Se instala con:

```bash
> pip3 install -r requierements.txt
```

Luego, se jecuta la apicación en background con el siguiente comando:

```bash
> nohup python3 api.py &
```

Esto ejecuta la aplicación, la deja corriendo en background, y los mensajes del sistema se guardan en un archivo ```nohup.out```

***IMPORTANTE***: La base PostgreSQL tiene que estar levantada en el mismo host donde corre la aplicación ANTES de iniciar la ejecución de la API.

