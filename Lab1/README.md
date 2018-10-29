## Contenedores & Imágenes

### Isolation
Veamos un ejemplo práctico
1. Ejecuta una shell interactiva de alpine `docker container run -it alpine /bin/ash`
2. En la shell interactiva escribe:
```sh
echo "Hello docker from scratch" > /home/hello.txt

ls /home
```
3. Sal del contenedor con `exit`
4. Para ver como funciona el aislamiento, ejecuta `docker container run alpine ls /home`
5. Comprobamos que el fichero `hello.txt` no existe, esto es debido a que esta ejecución se ha realizado en una nueva instancia y por tanto separada.

### Contenedores y cli
1. Descarga la imagen oficial de `ubuntu` y ejecuta en un contenedor interactivo una shell `bash`
2. Muestra los contenedores en ejecución usando el comando `docker container`y `docker ls`
3. Muestra todos los contenedores tanto en ejecución como parados
4. Para el contenedor `ubuntu`
5. ¿Qué diferencia hay entre `docker stop` y `docker kill`?
6. Arranca el contenedor `ubuntu`
7. Elimina el contenedor `ubuntu`

### Comando `exec`
6. Inicia el contenedor del apartado **Isolation** usando `start` y lista el archivo `hello.txt` usando `exec`
