<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Módulo 2: Seguridad Compartida</h1>
</p>

## Terminología

| Término  | Concepto  |
| :------------: | :------------: |
| Amazon Inspector  | <p align="justify">Servicio de evaluación de seguridad automatizado que ayuda a probar la accesibilidad de la red de las instancias de EC2 y el estado de seguridad de las aplicaciones que se ejecutan en las instancias.</p>  |
| AWS Trusted Advisor  | <p align="justify">Servicio de evaluación de seguridad que se aplica a una cuenta completa de AWS. </p>  |
| Amazon Simple Storage Service (Amazon S3) | <p align="justify">Servicio en el que se almacenan datos de los usuarios en la nube.</p>  |
| Autenticación Multifactor (MFA)  | <p align="justify">Añade una capa extra de seguridad al tener más de un método de autenticación a fin de verificar la identidad del usuario para un inicio de sesión u otra transacción.</p>  |
| AWS Identity and Access Management (IAM)  | <p align="justify">Implica la aplicación de controles a los usuarios que necesitan acceder a los recursos informáticos.</p>  |
| Amazon Elastic Block Store (Amazon EBS)  | <p align="justify">Almacenamiento para instancias EC2 específicas.</p>  |
| Amazon Relational Database Service (Amazon RDS)  | <p align="justify">Permite a los desarrolladores crear y administrar bases de datos relacionales en la nube. Piense en una base de datos relacional como un conjunto de datos con relaciones 1 a 1.</p>  |

## Conceptos
<p align="justify">
Trusted Advisor es una herramienta en línea que escanea su infraestructura de AWS, la compara con las prácticas recomendadas de AWS en cinco categorías, y brinda orientación en tiempo real para ayudar a los clientes a proporcionar recursos a la vez que siguen las prácticas recomendadas de AWS. Destaca los problemas potenciales con la forma en que el cliente utiliza AWS.</p>

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/54fdcd3a-9d4a-4548-83f9-10a8544563ba" width="600">
</p>

<p align="justify">
Amazon Inspector prueba la accesibilidad a la red de las instancias EC2 de los clientes y el estado de seguridad de las aplicaciones que se ejecutan en esas instancias. Amazon Inspector produce una lista detallada de hallazgos de seguridad, priorizados por nivel de severidad. Estos hallazgos se pueden revisar directamente o como parte de informes de evaluación detallados que están disponibles a través de la consola Amazon Inspector o la interfaz de programa de aplicación (API). La automatización es un principio central de las prácticas de seguridad modernas; los clientes de AWS pueden automatizar las pruebas de seguridad con Amazon Inspector.</p>

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/884686bf-1b8f-4548-b565-4463cba15d77" width="600">
</p>

Esta es la principal diferencia entre estos servicios:
- Trusted Advisor se aplica a la cuenta de AWS y a las administraciones de AWS.
- Amazon Inspector se aplica al contenido de varias instancias EC2.
