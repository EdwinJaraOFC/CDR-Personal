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
```
cd ~
aws s3api create-bucket --bucket (bucket-name) --region us-east-1
```
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/3b1b0df2-9521-44e2-8bd7-56beb6b5864b" width="800">
</p>

- La región us-east-1 se ha introducido en el comando. Al crear un bucket, la práctica recomendada es elegir una región cercana para minimizar la latencia y los costes o para cumplir los requisitos normativos. Los objetos almacenados en una región nunca abandonan esa región a menos que los transfieras explícitamente a otra región.
- Al crear un bucket con este comando, el bucket está abierto al público. Te recomendamos que mantengas habilitada toda la configuración a menos que sepas que tendrás que desactivar uno o más ajustes para tu caso de uso, por ejemplo, para alojar un sitio web público.

### Tarea 2. Añadir una política de bucket
- Desactiva la casilla de Bloquear todo el acceso público.
- Selecciona ACL habilitadas.
```
{
   "Version":"2012-10-17",
   "Statement":[
      {
         "Sid":"PublicReadForGetBucketObjects",
         "Effect":"Allow",
         "Principal":"*",
         "Action":[
            "s3:GetObject"
         ],
         "Resource":[
            "arn:aws:s3:::example-bucket/*"
         ]
      }
   ]
}
```
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/b297f19e-f9a8-40c3-839b-c56a83bbec06" width="500">
</p>

### Tarea 3. Subir un documento HTML
- Expande la sección Permisos.
- En ACL predefinidas, selecciona Conceder acceso de lectura público.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/2c472638-d772-402d-b97e-3a88dba27371" width="800">
</p>

### Tarea 4. Probar el sitio web
- Habilita la sección Alojamiento de sitios web estáticos.
- Desplázate de nuevo hacia abajo hasta la sección Alojamiento de sitios web estáticos y copia la URL del Punto de enlace de sitio web del bucket en el portapapeles.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/a89cf7f6-ffc8-4b40-b274-08760863b623" width="800">
</p>

### Tarea 5. Crear una distribución de CloudFront para servir al sitio web
- En la sección Origen, selecciona el cuadro de texto que aparece junto a Dominio de origen y selecciona el punto de enlace de tu bucket de S3.
- Para Viewer Protocol Policy (Política de protocolo de visor), asegúrate de que HTTP y HTTPS estén seleccionados. En Web Application Firewall (WAF), selecciona Do not enable security protections (No habilitar protecciones de seguridad).
- Cuando el Estado de la distribución sea Habilitado, puedes probarlo.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/f0a2d82e-bc71-4032-b94a-7fa644002763" width="800">
</p>

- Copia el valor de Nombre de dominio de la distribución y guárdalo en un editor de texto para utilizarlo en un paso posterior.
- Crea un nuevo archivo HTML para probar la distribución.
- Crea un nuevo archivo de texto con el Bloc de notas y copia en él el siguiente texto:

```
<html>
    <head>My CloudFront Test</head>
    <body>
        <p>My test content goes here.</p>
        <p><img src="http://domain-name/object-name" alt="my test image">
    </body>
</html>
```

- Reemplaza domain-name por el nombre de dominio que copiaste antes para la distribución de CloudFront.
- Reemplaza object-name por el nombre del archivo de imagen que cargaste en el bucket de S3.
- Utiliza un navegador de Internet para abrir el archivo HTML que acabas de crear.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/558b20f2-3e32-4bc5-b061-df82ad8c7b9a" width="800">
</p>
