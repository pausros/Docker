# Ediciones Docker
Dispone dos ediciones, Comunity Edition (CE) y Enterprise Edition (EE).

# Instalando docker CE
Docker está disponible para multiples plataformas, entre ellas Windows, Unix (Mac) y la gran mayoría de distribuciones linux. 
Visita la [web oficial](https://docs.docker.com/install/#supported-platforms) para conocer las disponibles.

### Crea una cuenta y registrate en [docker.com](https://store.docker.com/signup?next=%2Feditions%2Fcommunity%2Fdocker-ce-desktop-windows%3Ftab%3Dreviews)

### Windows
Visita la web oficial y [descarga Docker Community Edition](https://store.docker.com/editions/community/docker-ce-desktop-windows)

### Mac
Visita la web oficial y [descarga Docker Community Edition](https://store.docker.com/editions/community/docker-ce-desktop-mac)

### Linux
Las distribuciones linux disponen de varios métodos de instalación, los más utilizados son mediante los repositorios oficiales o descargando el paquete correspondiente e instalando manualmente.

### Cloud
Docker está disponible en los clouds de AWS y Azure.

# Docker CLI
Explorar comandos tanto de gestión como de servicio (imágenes y contenedores)
1. Ejecuta `docker`
2. Ejecutando nuestro primer contenedor `docker container run hello-world`
3. Investiga sobre los comandos `docker pull` y `docker image pull` ¿Se Observan diferencias? Descarga la imagen `alpine`
4. Ahora disponemos de imagenes en nuestro docker local. Lista las imágenes con `docker image ls` ¿Qué diferencias has observado entre la ejecución de los comandos anteriores?
5. Vamos a correr un contenedor basado en la imagen alpine, ejecuta `docker container run alpine ls -l` 
6. Ejecuta `docker container run alpine echo "curso docker from scratch"
