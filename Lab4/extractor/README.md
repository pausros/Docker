### Dockerfile: versiones de imagen
1. Construye una imagen `extractor` y nombrala con el tag `1.0`
3. Extrae las dependencias a un archivo `requirements.txt`. Modifica el Dockerfile y actualiza la imagen a versión `2.0`
4. Quita el comando `RUN chmod a+x *.py` y actualiza la imagen a la versión `3.0`
5. Ejecuta el contenedor `extractor:2.0`
6. Ejecuta el contenedor `extractor:3.0`

### Intentalo
```sh
$ docker image build -t extractor:1.0 .
$ docker container run -it --rm -p 5000:5000 extractor:1.0
```
