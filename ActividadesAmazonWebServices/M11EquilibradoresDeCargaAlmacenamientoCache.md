<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Módulo 11: Balanceadores de carga y almacenamiento en caché</h1>
</p>

## Finalidad del módulo
Aprenderemos la finalidad de Amazon ElastiCache y los beneficios del almacenamiento en caché de datos. También aprenderremos sobre Elastic Load Balancing.

## Terminología
| Término  | Concepto  |
| :------------: | :------------: |
| Amazon ElastiCache  |  <p align="justify">Es un servicio web en memoria rápida para almacenar datos efímeros y acceder a ellos con latencias extremadamente bajas, ideal para aplicaciones en tiempo real, cachés, mensajería y más.</p> |
| Caché  |  <p align="justify">Capa de almacenamiento de datos de alta velocidad que almacena un subconjunto de datos transitorios, de modo que las solicitudes futuras de esos datos se entregan más rápido de lo que sería posible si se accediera a la ubicación de los datos en el almacenamiento principal.</p> |
| Elastic Load Balancing  | <p align="justify">Distribuye automáticamente el tráfico entrante de las aplicaciones de varios destinos, como las instancias de Amazon EC2 y las funciones de AWS Lambda. Si el tráfico a un sitio web aumenta repentinamente, ese tráfico se puede dirigir a otras instancias EC2 o instancias Lambda que se hayan establecido de antemanto para este fin. Este balanceador de carga evita la sobrecarga de un solo servidor debido al aumento del tráfico que se dirige hacia él.</p>  |
| RAM  | <p align="justify">Almacenamiento de memoria volátil y temporal. Estos son los datos que se conservan temporalmente mientras un equipo está en uso.</p>  |

## Antecedentes
Para tipos de datos muy solicitados o que requieren un uso intensivo de memoria, un servicio de almacenamiento en caché de datos como ElastiCache puede ayudar a garantizar que se pueda acceder a los datos y procesarlos con extrema rapidez. Este servicio funciona almacenando los datos en una memoria extremadamente rápida, pero temporal, que es más rápida que el almacenamiento basado en disco. La desventaja es que la memoria rápida tiene menos espacio de almacenamiento y no almacena los datos de forma permanente.

El tráfico intenso puede apagar aplicaciones y sitios web si el servidor no puede manejar la carga. Por eso AWS cuenta con ELB, que puede detectar cuando hay demasiadas solicitudes y desviar automáticamente el tráfico hacia un nuevo servidor para mantener la velocidad y la estabilidad. Existen tres tipos de ELB en AWS.

### Balanceador de carga de aplicaciones
- Es el más adecuado para compensar la carga del tráfico del protocolo de transferencia de hipertexto (HTTP) y HTTP seguro (HTTPS)
- Operando a nivel de solicitud individual (capa 7), el balanceador de carga de aplicaciones dirige el tráfico a los destinos de Amazon Virtual Private Cloud (Amazon VPC) en función del contenido de la solicitud.
- La compensación del balanceador de carga de aplicaciones se realiza en función del contenido del localizador de recursos uniforme (URL). Por ejemplo, si el URL termina en /main, la solicitud se dirigirá a una instancia; si el URL termina en blog/, se dirigirá a otra instancia si se ha realizado el trabajo de definición del balanceador de carga de aplicaciones por adelantado para hacer que esto suceda.

### Balanceador de carga de red
- Es el más adecuado para compensar la carga del tráfico del protocolo de control de transmisión (TCP), el protocolo de datagramas de usuario (UDP) y la Transport Layer Security (TLS) donde se requiere un rendimiento extremo.
- El balanceador de carga de red, que funciona a nivel de conexión (capa 4), dirige el tráfico a los destinos dentro de la Amazon VPC y es capaz de gestionar millones de solicitudes por segundo mientras mantiene latencias ultrabajas.
- Debido al aumento de la velocidad que se puede lograr en la capa de conexión, el tipo de compensación de carga del balanceador de carga de red es más conveniente cuando se intenta evitar mayores volúmenes de tráfico de red. Por ejemplo, para evitar retrasos cuando el interés en un sitio web se vuelve viral, elegirá utilizar la compensación del balanceador de carga de red.

### Balanceador de carga clásico
- El balanceador de carga clásico proporciona una compensación de carga básica en varias instancias EC2 y funciona a petición y según los niveles de conexión.
- El balanceador de carga clásico está diseñado para aplicaciones que se construyeron dentro de la red EC2-Classic.

