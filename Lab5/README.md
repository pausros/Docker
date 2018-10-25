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
``
flask
redis
``
Muestra los contenedores en ejecución
4. Muestra todos los contenedores 
5. Para el contenedor `ubuntu`
6. ¿Qué diferencia hay entre `docker stop` y `docker kill`?
7. Arranca el contenedor `ubuntu`
7. Elimina el contenedor `ubuntu`
