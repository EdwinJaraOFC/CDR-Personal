<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Módulo 4: Servidores Virtuales</h1>
</p>

## Finalidad del módulo
<p align="justify">
Aprenderemos a crear una instancia de Amazon Elastic Compute Cloud (Amazon EC2) y utilizarla para alojar un sitio web. También aprenderemos la finalidad de las claves de acceso, un sistema de nombres de dominio (DNS), Amazon Route 53 y nubes privadas virtuales.</p>

## Terminología
|  Término | Concepto  |
| :------------: | :------------: |
| Amazon Elastic Compute Cloud (Amazon EC2)  | <p align="justify">Servicio web que ofrece capacidad informática escalable en la nube. Considérelo como alquilar una computadora en la nube.</p>  |
| Amazon Simple Storage Service (Amazon S3)  | <p align="justify">Servicio proporcionado por Amazon Web Services (AWS) que almacena datos para los usuarios en la nube.</p>  |
| Sistema de nombres de dominio (DNS)  | <p align="justify">Sistema de nomenclatura para computadoras, dispositivos y recursos conectados a una red.</p>  |
|  Bucket de Amazon Simple Storage Service (Amazon S3) |  <p align="justify">Un contenedor de objetos (como imágenes, archivos de audio, archivos de video, documentos, etc.) en Amazon S3.</p> |
| Política  | <p align="justify">Objeto de AWS que, cuando se asocia a una identidad o un recurso, define sus permisos. AWS evalúa estas políticas cuando una entidad principal (usuario o rol) realiza una solicitud.</p>  |
|  Nombre de dominio | <p align="justify">Etiqueta que identifica una red de computadoras bajo control centralizado.</p>  |
|  Amazon Route 53 |  <p align="justify">El servicio web DNS de AWS.</p> |
|  Nube privada virtual (VPC) |  <p align="justify">Red virtual dedicada a su cuenta de AWS. Esta infraestructura está aislada de forma lógica de otras redes virtuales de la nuve de AWS. Todos sus servicios de AWS se pueden lanzar desde una VPC. Resulta útil para proteger los datos y administrar quién puede acceder a la red.</p> |
|  Notación de objetos JavaScript (JSON) | <p align="justify">Sintaxis para almacenar e intercambiar datos.</p>  |
| Sitio web dinámico  | <p align="justify">Sitio web que cambia según las interacciones del usuario; a menudo se crea con Python, JavaScript, PHP o ASP con lenguaje de marcado de hipertexto (HTML).</p>  |
| Sitio web estático  |  <p align="justify">Un sitio web que no cambia según las interacciones del usuario; normalmente se crea con HTML y hojas de estilo en cascada (CSS).</p> |

## Antecedentes y conceptos
<div align="center"; style="display: flex; justify-content: space-between;">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/5293303b-639b-4cd8-b233-0ad252466e4a" width="500px"/>
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/a26c8c4f-5546-4d5a-ae4b-a43307c25e70" width="600px"/>
</div>

## Laboratorio 1: Lanzamiento de una instancia EC2
### Objetivo
Crear una instancia de EC2 que aloja un sitio web sencillo.
### Preguntas
<p align="justify">

1. ¿Necesita una explicación más detallada de los pasos para crear una instancia EC2 para alojar un sitio web? ¿Dónde cree que podría buscar más información sobre esa parte del proceso?
2. Abrió el servidor para que se acceda desde cualquier puerto. ¿En qué cree que la configuración del grupo de seguridad sería diferente para una gran empresa como AWS?
3. ¿Tiene alguna otra pregunta sobre el proceso de creación de una instancia EC2 y la ejecución de un sitio web?
</p>

## Laboratorio 2: Creación de un bucket de S3
### Objetivo
Crear un bucket de S3.
### Preguntas
<p align="justify">
  
1. ¿Necesita una explicación más detallada de alguno de los pasos para crear un bucket de S3 para alojar un sitio web? ¿Dónde cree que podría buscar más información sobre esa parte del proceso?
2. Los buckets de S3 escalan automáticamente para ajustarse al tamaño de los datos almacenados. ¿Por qué cree que esto es útil para las empresas que utilizan el servicio Amazon S3?
3. ¿Qué tipos de datos cree que pueden beneficiarse de almacenarse en la nube? ¿Cómo el almacenamiento de los datos en la nube hace que sus datos estén más seguros y protegidos? 
4. ¿Cómo cree que los buckets de S3 están relacionados con las instancias EC2?
</p>
