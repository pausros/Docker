## Reto: Docker fron scratch streaming real time

EticSearch la spin-off que nació hace algun tiempo de E-tic Sistemes se consolida. Especializada en tratamiento de la información, su lema es 'powering data, smart data' amplió el catalogo de servicios centrándose en las últimas tecnologías orientadas a microservicios, las ventajas de docker y la fácilidad subyacente tanto a nivel de sistemas como la construcción de aplicaciones.

Un nuevo cliente desea realizar un análisis en tiempo real del precio del bitcoin debido a que está implementando una aplicación con tecnología blockchan. Nuestro CTO, ha elaborado un entorno docker con scripts python, Influx y Grafana.

Como especialistas de la compañia hemos de preparar un entorno docker para realizar las pruebas, construye:

1. Añade un servicio influxdb basado en la última imagen oficial en dockerHub. Mapea el puerto `8086` y el volumen `/var/lib/influxdb` y que se reinicie siempre.
2. Añade un servicio grafana basado en la última imagen oficial en dockerHub. Mapea el puerto `3000` y el volumen `/var/lib/grafana` y que se reinicie siempre.
3. Modifica el script python para que pueda conectar con el host influx.
4. Construye el servicio 'app' basado en el Dockerfile.
5. Inicia todos los servicios, observa los logs y comprueba que no hay errores.
6. Deten el sistema.
7. Arranca en modo background.

