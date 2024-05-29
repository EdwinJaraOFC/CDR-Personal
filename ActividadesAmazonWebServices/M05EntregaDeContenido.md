<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Módulo 5: Entrega de Contenido</h1>
</p>

## Finalidad del módulo
Obtendremos información sobre la red de entrega de contenido (CDN) de Amazon Web Services (AWS), Amazon CloudFront. 

## Terminología
| Término  | Concepto  |
| :------------: | :------------: |
| Amazon CloudFront  | <p align="justify">Servicio CDN rápida que entrega datos, aplicaciones e interfaces de programación de aplicaciones (API) de forma segura a clientes de todo el mundo con baja latencia y altas velocidades de transferencia.</p>  |
| AWS Direct Connect  |  <p align="justify">Proporciona la capacidad de establecer una conexión de red dedicada/privada desde su entorno en las instalaciones a AWS.</p> |
| Almacenamiento en caché  | <p align="justify">Almacena los datos solicitados con frecuencia en ubicaciones de borde para que se pueda acceder a ellos con mayor rapidez.</p>  |
| Red de entrega de contenido (CDN)  | <p align="justify">Sistema de servidores distribuidos (red) que entrega páginas y contenido web a un usuario, en función de las ubicaciones geográficas del usuario, el origen de la página web y el servidor de entrega de contenido.</p>  |
| Distribución  | <p align="justify">Indica a CloudFront donde obtener la información almacenada en caché y cómo administrar la entrega de contenido.</p>  |
| Ubicación de borde  | <p align="justify">Sitio en el que se pueden almacenar los datos para reducir la latencia.</p>  |
| Origen  | <p align="justify">Tipo complejo que describe el bucket de AmazonS3, el servidor de protocolo de transferencia de hipertexto (HTTP).</p>  |

## Laboratorio del módulo 5: Uso de CloudFront como CDN para un sitio web
### Tarea 1. Crear un bucket de S3 mediante AWS CLI
- AWS CLI es una herramienta de código abierto que puedes utilizar para interactuar con los servicios de AWS mediante comandos en tu shell de línea de comandos.
- AWS CloudShell es un shell basado en navegador que da acceso a la línea de comandos para los recursos de AWS en la región de AWS seleccionada.

![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/3b1b0df2-9521-44e2-8bd7-56beb6b5864b)

- La región us-east-1 se ha introducido en el comando. Al crear un bucket, la práctica recomendada es elegir una región cercana para minimizar la latencia y los costes o para cumplir los requisitos normativos. Los objetos almacenados en una región nunca abandonan esa región a menos que los transfieras explícitamente a otra región.
- Al crear un bucket con este comando, el bucket está abierto al público. Te recomendamos que mantengas habilitada toda la configuración a menos que sepas que tendrás que desactivar uno o más ajustes para tu caso de uso, por ejemplo, para alojar un sitio web público.

### Tarea 2. Añadir una política de bucket
- Desactiva la casilla de Bloquear todo el acceso público.
- Selecciona ACL habilitadas.

![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/b297f19e-f9a8-40c3-839b-c56a83bbec06)

### Tarea 3. Subir un documento HTML

### Tarea 4. Probar el sitio web

### Tarea 5. Crear una distribución de CloudFront para servir al sitio web
