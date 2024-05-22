<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Módulo 9: Monitoreo de la nube</h1>
</p>

## Finalidad del módulo
Conocer las herramientas que Amazon Web Services (AWS) proporciona para monitorear los servicios en la nube. Estos incluyen AWS Config, AWS CloudTrail y Amazon CloudWatch.

## Terminología
| Término  | Concepto  |
| :------------: | :------------: |
| Amazon CloudWatch  | Servicio de monitoreo para monitorear los recursos de AWS y las aplicaciones que ejecuta en AWS.  |
| AWS CloudTrail  | Servicio para monitorear y registrar cada acción que se lleva a cabo en su cuenta de AWS por motivos de seguridad.  |
| AWS Config  | Servicio que permite analizar, auditar y evaluar las configuraciones de los recursos de AWS.  |
| Amazon Simple Notification Service (Amazon SNS)  | Una herramienta de AWS que permite enviar textos, correos y mensajes a otros servicios en la nube y enviar notificaciones al cliente de varias formas desde la nube.  |

## Antecedentes
<p align="justify">
AWS proporciona herramientas poderosas para supervisar todos los servicios en la nube. Estas herramientas funcionan conjuntamente para proporcionar un paquete de servicios que empoderan a los usuarios de la nube con conocimientos.</p>
<p align="justify">
CloudWatch es un servicio de monitoreo para monitorear los recursos de AWS y las aplicaciones que ejecuta en AWS.</p>
<p align="justify">
CloudTrail y CloudWatch son servicios de monitoreo en la nube, pero realizan diferentes funciones:</p>
<p align="justify">
CloudTrail monitorea y registra todas las acciones que los usuarios han realizado en una cuenta de AWS determinada. Esto significa que CloudTrail registra cada vez que alguien carga datos, ejecuta un código, crea una instancia de Amazon Elastic Compute Cloud (Amazon EC2) o realiza cualquier otra acción.</p>
<p align="justify">
CloudWatch supervisa lo que hacen los distintos servicios y qué recursos están utilizando. CloudTrail registra actividades, mientras que CloudWatch monitorea las actividades. CloudWatch lo ayuda a asegurarse de que sus servicios en la nube se ejecuten sin problemas. Los servicios también pueden ayudarlo a no utilizar ni más ni menos recursos de lo esperado, lo que es importante para el seguimiento del presupuesto.</p>
<p align="justify">
AWS Config es un servicio que permite sopesar, auditar y evaluar las configuraciones de los recursos de AWS. AWS Config monitorea y registra de manera continua sus configuraciones de recursos de AWS y permite automatizar la evaluación de las configuraciones registradas con respecto a las deseadas.</p>

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/50b80484-68b9-4461-bcab-f0ca77b0c383">
</p>
Fuente de la imagen: https://aws.amazon.com/config/

<p align="justify">
Amazon SNS es la forma en que AWS se comunica dentro de la nube y con el mundo exterior. Cuando se inicia un evento o un programa alerta a AWS para enviar notificaciones, Amazon SNS envía los mensajes a los usuarios u otros servicios de AWS.</p>

## Laboratorio: Creación de una alarma de CloudWatch que inicia un mensaje de Amazon SNS
### Objetivo
Utilizar CloudWatch para configurar un evento de alerta de mensaje de texto.

### Tarea 1: Crear y suscribirse a un tema de SNS
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/33d5827e-5f55-46de-8b71-3a7a6d7ccd23">
</p>

### Tarea 2: Crear una alarma de CloudWatch
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/57d3aaf2-4d7a-4749-b146-4b210d67a2c7">
</p>
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/d3e947f0-3571-4538-8a13-4cc1108f5bcc">
</p>
