<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Módulo 3: Consola de AWS</h1>
</p>

## Terminología
### Amazon Simple Storage Service (Amazon S3)
Servicio proporcionado por AWS que almacena datos para los usuarios en la nube.
### Amazon Elastic Compute Cloud (Amazon EC2)
Un servicio web que ofrece capacidad de cómputo escalable en la nube. Considérelo como alquilar un equipo en la nube.
### Amazon Elastic Block Store (Amazon EBS)
Almacenamiento para instancias EC2 específicas. Considérelo como la unidad de almacenamiento de su instancia EC2.
### Amazon Relational Database Service (Amazon RDS)
Esto permite a los desarrolladores crear y administrar bases de datos relacionales en la nube. Piense en una base de datos relacional como un conjunto de datos con relaciones 1 a 1. Por ejemplo, una base de datos de transacciones en un almacén departamental coincidiría con cada cliente con sus compras. Amazon RDS permite a los desarrolladores realizar un seguimiento de grandes cantidades de estos datos, organizarlos y buscarlos fácilmente. Las bases de datos relacionales están equipadas con un lenguaje de consulta estructurado no procedimental (SQL) que simplifica las interacciones con la base de datos.
### Amazon DynamoDB
Servicio de bases de datos no relacionales de AWS. Los datos se almacenan en pares de clave-valor.
### AWS Lambda
Lambda le permite ejecutar código sin necesidad de aprovisionar o administrar sercidores. Solo pagará por el tiempo de cómputo que consuma. No se cobra nada cuando el código no se está ejecutando. Con Lambda, puede ejecutar código para casi cualquier tipo de aplicación o servicio backend sin tener que realizar tareas de administración. Solo tiene que cargar el código y Lambda se encargará de todo lo necesario para ejecutar y escalar el código con alta disponibilidad. Puede configurar su código para que se active automáticamente desde otros servicios de AWS o puede llamarlo directamente desde cualquier aplicación web o móvil.
### Amazon Virtual Private Cloud (Amazon VPC)
Un servicio que proporciona una red virtual dedicada a su cuenta de AWS. Esta infraestructura está aislada de forma lógica de otras redes virtuales de la nube de AWS. Todos sus servicios de AWS se pueden lanzar desde una VPC. Sirve para proteger los datos y adinistrar quién puede acceder a la red.
### AWS Identy and Management (IAM)
Implica el control de los usuarios que necesiten acceder a recursos informáticos.
### AWS CloudTrail
Monitorea todas las acciones que se realizan en su cuenta de AWS por motivos de seguridad.
### Amazon CloudWatch
CloudWatch es un servicio de supervisión para monitorizar los recursos de AWS y las aplicaciones que ejecuta en AWS.
### Amazon Redshift
El servicio de almacenamiento de datos de AWS puede almacenar enormes cantidades de datos de forma que se puedan consultar rápidamente con fines de inteligencia empresarial.
## Antecedentes y conceptos
Los servicios en la nube de AWS incluyen una gran cantidad de herramientas diferentes que funcionan juntas para cubrir todas las necesidades informáticas de un usuario, completamente en la nube.

Amazon VPC es la red virtual que define dónde lanza los recursos de AWS. Esta red virtual se parece mucho a una red tradicional que opera en su propio centro de datos, con las ventajas de utilizar la infraestructura escalable de AWS.

Estas son algunas diferencias entre los servicios:

Amazon S3 y Amazon EBS son formas de almacenamiento de datos. Existen algunas diferencias clave:

Amazon EBS solo se puede utilizar cuando se conecta a una instancia EC2 y se puede acceder a Amazon S3 por sí solo.
Amazon EBS no puede contener tantos datos como Amazon S3.
Amazon EBS solo se puede adjuntar a una instancia EC2, mientras que varias instancias EC2 pueden acceder a los datos de un bucket de S3.
Amazon S3 experimenta más retrasos que Amazon EBS al escribir datos.
Amazon RDS, Amazon Redshift y DynamoDB están relacionados con las bases de datos, pero existen diferencias:

Amazon RDS es la base de datos relacional clásica que utiliza SQL Server, Oracle Database, Amazon Aurora u otros sistemas de bases de datos similares. Considérelo como un libro de calificaciones en el que cada alumno es una fila y todos tienen el mismo número de tareas (columnas) a las que se adjuntan. Las empresas pueden utilizar el código para buscar datos específicos en función de la información de las filas y columnas. Amazon RDS resulta útil para las empresas que almacenan una cantidad moderada de datos de estructura uniforme, lo que significa que cada ID único, como el nombre del estudiante, se adjunta al mismo número de puntos de datos (calificaciones).
Amazon Redshift es una base de datos relacional como Amazon RDS, pero está diseñada específicamente para grandes cantidades de datos. Es una herramienta de almacenamiento de datos que es buena para los usuarios que trabajan con big data.
DynamoDB es una base de datos no relacional, lo que significa que no se pueden utilizar sistemas tradicionales como SQL Server o Aurora. Cada elemento de la base de datos se almacena como un par de clave-valor o como una notación de objetos JavaScript (JSON). Esto significa que cada fila podría tener un número diferente de columnas. No es necesario que todas las entradas se emparejen de la misma manera. Esto permite una flexibilidad en el procesamiento que funciona bien para blogs, juegos y publicidad.
CloudTrail y CloudWatch son servicios de monitorización en la nube, pero realizan diferentes funciones:

CloudTrail monitorea todas las acciones que los usuarios han realizado en una cuenta de AWS determinada. Esto significa que cada vez que alguien carga datos, ejecuta código, crea una instancia EC2, cambia un tipo de unidad S3 o cualquier otra acción que se pueda realizar en AWS, CloudTrail lo registrará. Esto resulta muy útil por razones de seguridad para que los administradores puedan saber quién está utilizando su cuenta y qué están haciendo. Si algo sale mal o si surge un problema de seguridad, CloudTrail será la mejor prueba para averiguar lo ocurrido.

CloudWatch monitorea lo que hacen los distintos servicios y qué recursos están utilizando. Si CloudTrail monitorea personas, CloudWatch monitorea servicio. CloudWatch es excelente para asegurarse de que sus servicios en la nube funcionan sin problemas y no utilizan más o menos recursos de los esperados, lo que es importante para el seguimiento del presupuesto. CloudWatch es excelente para asegurarse de que todos los recursos están funcionando, lo que puede resultar complicado si una gran empresa utiliza cientos de máquinas y unidades diferentes. Los monitores y alarmas se pueden configurar a través de CloudWatch para iniciar automáticamente una alerta cuando una métrica alcanza un límite específico.
