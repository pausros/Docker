## Docker-compose
1. Crea el directorio `primercompose` para alojar el proyecto.
2. Crea un fichero llamado `app.py` y copia el siguiente código:
```python
import time
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)
# redis es un contenedor que utiliza el puerto por defecto

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hola Docker Compose from scratch! Me has vistado {} veces.\n'.format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
```

3. Crea un fichero llamado `requirements.txt`y añade: 
```
flask
redis
```
4. Crea un Dokerfile para construir la imagen Docker que contendrá todas las dependencias python que requiera la aplicación, incluido Python
```
FROM python:3.4-alpine
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```
5. Definir los servicios en un fichero Compose, para ello crea un archivo `docker-compose.yml` y añade lo siguiente:
```yml
version: '3'
services:
  web:
    build: .
    ports:
     - "5000:5000"
  redis:
    image: "redis:alpine"
```
    
6. Construye y ejecuta la aplicación con Compose, `docker-compose up` Una vez tengamos los servicios activos, abre un navegador pon `http://localhost:5000` En caso de no resolver interfaz local, prueba con `http://0.0.0.0:5000`

Ya tenemos nuestra web y cache funcionando. ¿Qué ocurre si hemos de modificar el código fuente de la aplicación? Deduce la respuesta

### Añadir volumen
Añadiendo un punto de montaje o 'bind mount' podremos modificar el código 'on the fly'. Para obtener más información sobre volúmenes y puntos de montaje, visita este [enlace](https://docs.docker.com/storage/)

7. Edita `docker-compose.yml`y añade:
```yml
version: '3'
services:
  web:
    build: .
    ports:
     - "5000:5000"
    volumes:
     - .:/code
  redis:
    image: "redis:alpine"
 ```
 
8. Ahora, ejecuta el sistema en background, `docker-compose up -d` (--detach)
9. Edita el archivo local `app.py` y sustituye `return` por:
```python
return 'Compose from scratch mola! Me has vistado {} veces.\n'.format(count)
```
### Comandos
Compose dispone de una lista importante de comandos.
#### run
`docker-compose run` permite ejecutar comandos disponibles para los servicios. Mostraremos las variables de entorno disponibles para el servicio `web` y `redis`

10. Ejecuta `docker-compose run web env` haz lo mismo para el servicio `redis`
#### ps
Muestra los procesos/servicios activos.
#### up, start y stop
Se inician los servicios con los comandos `up`y `start` y se paran con `stop`.

11. Para todos los servicios iniciados `docker-compose stop`
12. Inicia con `start`
13. Muestra los procesos
14. Parar el servicio `redis` Comprueba el resultado, ¿Qué ha pasado?
15. Para todos los servicios
15. Inicia en background utilizando `up`
16. Para el servicio `redis` Comprueba resultado.

#### down
Es el comando que lo 'tira' todo, elimina contenadores incluso los datos de los volumenes utilizando el flag `--volumes`

18. `docker-compose down --volumes`

