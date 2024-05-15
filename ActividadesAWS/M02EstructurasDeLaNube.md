<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Módulo 2: Estructuras de la nube</h1>
</p>

## Terminología
| Término | Concepto |
| :------------: | :------------: |
| Región  | <p align="justify">Áreas en las que se almacenan los datos. El almacenamiento de datos en una región más cercana a usted es uno de los motivos por los que se puede acceder a ella a la velocidad de la luz.</p>  |
| Zona de disponibilidad  |  <p align="justify">Uno o varios centros de datos que albergan muchos servidores. Cada zona de disponibilidad está aislada, pero las zonas de disponibilidad de una región están conectadas mediante enlaces de baja latencia. Una zona de disponibilidad se representa mediante un código de región seguido de un identificador de letra, por ejemplo, us-east-1a.</p> |
| Ubicación de borde  |  <p align="justify">Un sitio donde se pueden almacenar datos para reducir la latencia. A menudo, las ubicaciones de borde estarán cerca de las zonas de gran población que generarán volúmenes de tráfico elevados.</p> |
| Latencia  | <p align="justify">El retraso que se produce antes de que se inicie una transferencia de datos después de que se hayan solicitado los datos.</p>  |
| Infraestructura como Servicio (IaaS)  | <p align="justify">Un modelo en el que se utilizan máquinas virtuales y servidores para que los clientes alojen una amplia gama de aplicaciones y para que se proporcionen servicios de TI.</p>  |
| Plataforma como Servicio (PaaS)  | <p align="justify">Un modelo que proporciona una plataforma virtual para que los clientes creen software personalizado.</p> |
| Software como Servicio (SaaS)  | <p align="justify">Un modelo que proporciona aplicaciones que utilizan Internet gestionadas por un tercero.</p> |

## Antecedentes y conceptos
<p align="justify">
Las diferencias entre los componentes de la infraestructura pueden ser confusas porque todos están interconectados y están relacionados con el diseño físico de la nube de AWS. Es bueno tener un ejemplo visual concreto.</p><br>

<p align="center">Región > zona de disponibilidad > ubicación de borde</p>

## Actividad 1: Visualización de la infraestructura global de AWS
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/87389e5e-6027-4958-b95e-6e0d219f5bde">
</p>

#### Compare su diagrama con el de otro estudiante. ¿Hay alguna diferencia? ¿Qué es lo mismo?
<p align="justify">
Se diferencian en la manera en que cada uno ha representado la infraestructura global de AWS. Aunque las ubicaciones específicas pueden variar, lo importante es que ambos diagramas están destinados a comunicar los mismos conceptos básicos.</p>

#### ¿Cómo se conectan las regiones, las zonas de disponibilidad y las ubicaciones de borde?
<p align="justify">
Las regiones representan áreas geográficas independientes que contienen una o más zonas de disponibilidad, y estas zonas están interconectadas para garantizar la disponibilidad y la redundancia de los servicios. Las ubicaciones de borde, por otro lado, son instalaciones distribuidas globalmente que actúan como puntos de entrada y salida de tráfico a la red global de AWS.</p>

## Actividad 2: Tipos de servicios en la nube
<p align="justify">
  
#### Una pediatra con consultorio privado tiene tantos archivos de pacientes que se está quedando sin espacio en sus archivadores. Por este motivo, quiere trasladar sus datos a la nube. Ella quiere asegurarse de que los datos estén seguros, pero también quiere que sus pacientes puedan acceder a sus registros médicos y comunicarse con ella en línea de forma segura. Describa una forma en la que puede utilizar cada tipo de servicio en la nube y cómo beneficiaría a su negocio.
La pediatra puede utilizar Amazon S3 para almacenar archivos de pacientes, Amazon API Gateway y AWS Lambda para desarrollar una API segura, Amazon Cognito para la gestión de la autenticación, Amazon RDS para almacenar y gestionar la base de datos de registros médicos, y Amazon CloudFront para mejorar la entrega de datos a los pacientes. Con estos servicios de AWS, puede trasladar sus datos a la nube de manera segura y ofrecer acceso en línea a los registros médicos de los pacientes.
</p>
