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
    return 'Hola Compose from scratch! Me has vistado {} veces.\n'.format(count)

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
    
6. ¿Qué diferencia hay entre `docker stop` y `docker kill`?
7. Arranca el contenedor `ubuntu`
7. Elimina el contenedor `ubuntu`
