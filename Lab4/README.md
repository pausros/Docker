## Dockerfile

1. En el directorio `webserver` se encuentran los archivos necesarios para ejecutar un servidor `nginx`. Construye tu imagen y ejecuta un contenedor web en el puerto 80
2. Código portable y mantenible dentro de `python-useful`. Construye una imagen y ejecuta un contenedor.
3. Pasa argumentos al contendor anterior.
4. Crea una imagen `jupyter` ejecuta un contenedor y accede a la libreta a través del puerto `8888`
5. El directorio `alpine` contiene instrucciones para construir tu primera imagen, ¡Adelante!

### versiones
1. Construye una imagen `extractor` y nombrala con el tag `1.0`
3. Extrae las dependencias a un archivo `requirements.txt`. Modifica el Dockerfile y actualiza la imagen a versión `2.0`
4. Quita el comando `RUN chmod a+x *.py` y actualiza la imagen a la versión `3.0`
5. Ejecuta el contenedor `extractor:2.0`
6. Ejecuta el contenedor `extractor:3.0`
