<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Módulo 12: Elastic Beanstalk y CloudFormation</h1>
</p>

## Finalidad del módulo
Comprender para qué sirven AWS Elastic Beanstalk y AWS CloudFormation y pueda utilizarlos.

## Terminología
| Término  | Concepto  |
| :------------: | :------------: |
| AWS Elastic Bean stalk  | <p align="justify">Administra automáticamente los detalles de implementación del aprovisionamiento de capacidad, el balanceo de carga, el escalado automático y el monitoreo del estado de una aplicación. Es como ejecutar una macro o un archivo por lotes que coloca un contenedor alrededor de una aplicación existente para que se ejecute sin problemas en la nube de AWS.</p>  |
| AWS CloudFormation  | <p align="justify">Este servicio brinda a los desarrolladores y empresas una manera fácil de crear un conjunto de recursos de AWS relacionados y aprovisionarlos de forma ordenada y previsible. Proporciona un medio para combinar una pila de servicios de AWS, similar a escribir macros o archivos por lotes en Linux o Windows.</p>  |
| Pila  | <p align="justify">Conjunto de recursos de AWS que puede administrar como una sola unidad. Puede crear, actualizar o eliminar un conjunto de recursos mediante la creación, actualización o eliminación de pilas.</p>  |

## Antecedentes
### ¿En qué se diferencia Elastic Beanstalk de CloudFormation?
Estos servicios están diseñados para complementarse entre sí. Elastic Beanstalk proporciona un entorno para implementar y ejecutar aplicaciones en la nube con facilidad. Está integrado con herramientas para desarrolladores y proporciona una experiencia única para que administre el ciclo de vida de las aplicaciones. CloudFormation es un mecanismo de aprovisionamiento práctico para una amplia gama de recursos de AWS. Admite las necesidades de infraestructura de muchos tipos diferentes de aplicaciones, como aplicaciones empresariales existentes, heredadas o creadas con diversos recursos de AWS y soluciones basadas en contenedores (incluidas aquellas creadas con Elastic Beanstalk).

Para ser claros, Elastic Beanstalk es como ejecutar un archivo.bat y CloudFormation es como escribirlo. Elastic Beanstalk permite a los desarrolladores cargar y ejecutar su código; luego, se encarga de toda la configuración de fondo en la nube, como lanzar instancias EC2 y asociar almacenamiento en bloques elástico. Con CloudFormation, básicamente está configurando una plantilla para todos los recursos en la nube que desea ejecutar para que todo se pueda realizar de una sola vez y de manera repetible.

CloudFormation admite entornos de aplicaciones de Elastic Beanstalk como uno de los tipos de recursos de AWS. Esto le permite, por ejemplo, crear y administrar una aplicación alojada en Elastic Beanstalk, junto con una base de datos de Amazon Relational Database Service (Amazon RDS) para almacenar los datos de la aplicación. Además de las instancias de base de datos de RDS, también se puede agregar al grupo cualquier otro recurso de AWS compatible.

## Laboratorio del módulo 12: Uso de Elastic Beanstalk y CloudFormation
### Tarea 1. Implementar una aplicación con Elastic Beanstalk

### Tarea 2. Implementar una aplicación mediante CloudFormation
