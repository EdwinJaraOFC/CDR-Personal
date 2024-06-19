<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Módulo 5: Servidores web dinámicos II</h1>
</p>

## Terminología

| Término  | Concepto  |
| :------------: | :------------: |
| Amazon CloudFront  | <p align="justify">Servicio de red de entrega de contenido (CDN) que entrega contenido como videos, datos, aplicaciones, etc., de forma segura.</p>  |
| Red de entrega de contenido (CDN)  | <p align="justify">Red de servicios distribuidos que proporciona páginas web y otro contenido web de forma segura en función de la ubicación geográfica del usuario.</p>  |
| Ubicación de borde  | <p align="justify">Ubicación donde el contenido web se almacena (en caché) de forma temporal.</p>  |
| Origen  | <p align="justify">Ubicación donde se almacena de forma permanente todos los objetos asociados a la página web.</p>  |
| Distribución  | <p align="justify">Colección de ubicaciones de borde.</p>  |
| Periodo de vida (TTL)  | <p align="justify">Tiempo mínimo y máximo para almacenar contenido en caché en una ubicación de borde.</p>  |

## Conceptos
<p align="justify">CloudFront es un servicio de CDN rápido que entrega de manera segura datos, videos, aplicaciones e interfaces de programación de aplicaciones (API) a clientes en todo el mundo con latencia baja y altas velocidades de transferencia, todo dentro de un entorno fácil de usar para los desarrolladores. CloudFront está integrado con Amazon Web Services (AWS), ubicaciones físicas que se conectan directamente con la infraestructura global de AWS y otros servicios de AWS. CloudFront funciona sin interrupciones con servicios tales como AWS Shield para la mitigación de ataques de denegación de servicio distribuidos (DDoS), Amazon Simple Storage Service (Amazon S3), Elastic Load Balancing (ELB) o Amazon Elastic Compute Cloud (Amazon EC2) como orígenes de sus aplicaciones y Lambda@Edge para ejecutar código personalizado más próximo a usuarios de clientes y personalizar la experiencia del usuario.</p>

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/dad23ca8-b533-44f1-8f09-4a9871a42fe7" width="650">
</p>

## Laboratorio del módulo 5: Creación de una distribución de CloudFront
### Tarea 1: Crear un bucket
<p align= "center">
  <img src=https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/5c41c85a-4ad9-45ed-9dca-0f6b897b063a"" width="900">
</p>
<p align= "center">
  <img src=https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/c09bc5e7-85d8-4134-b5d0-77b420563b76"" width="900">
</p>

### Tarea 2: Añadir una política de buckets para el acceso público
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadForGetBucketObjects",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::<EXAMPLE-BUCKET>/*"
            ]
        }
    ]
}
```

### Tarea 3: Crear una distribución con CloudFront
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/ba495723-5ce7-4b73-8bac-b5a59936628b" width="900">
</p>

### Tarea 4: Probar la distribución
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/580e8778-f67c-4ded-acee-7f37e2e7bcac" width="900">
</p>

### Tarea 5: Modificar la distribución
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/54d17096-c86f-4dab-8898-d20a7a6ade09" width="900">
</p>

### Tarea 6: Desactivar la distribución
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/f95da63d-0bc3-44d4-86d5-49c342ae025b" width="900">
</p>
