<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Módulo 6: Lambda</h1>
</p>

## Terminología

| Término  | Concepto  |
| :------------: | :------------: |
| AWS Lambda  | <p align="justify">Permite ejecutar código sin necesidad de administrar servidores.</p>  |
| Amazon Elastic Compute Cloud (Amazon EC2)  | <p align="justify">Servicio web que proporciona capacidad de cómputo de tamaño modificable y segura en la nube.</p>  |

## Conceptos
<p align="justify">Con Lambda, puede ejecutar código para casi cualquier tipo de aplicación o servicio backend sin tener que realizar tareas de administración. Solo tiene que cargar el código y Lambda se encargará de todo lo necesario para ejecutar y escalar el código con alta disponibilidad. Puede configurar el código para que inicie automáticamente desde otros servicios de Amazon Web Services (AWS) o lo puede llamar directamente desde cualquier sitio web o aplicación móvil.</p>

<p align="justify">Una diferencia importante entre Lambda y Amazon EC2 es el costo de operación. Los modelos de precios de los dos servicios son bastante diferentes. El costo de Lambda se basa en el uso de funciones Lambda y la cantidad de almacenamiento que utilizan las funciones, mientras que el costo de Amazon EC2 se basa en el tipo de imagen de máquina utilizado y la cantidad y el tipo de almacenamiento utilizado. Para cargas de trabajo livianas y medianas, Lambda es una solución mucho menos costosa que Amazon EC2.</p>

<p align="justify">Trabajar con Amazon EC2 para administrar sus instancias desde el momento que las lanza hasta su terminación, garantiza que los clientes tengan el mejor rendimiento posible y la experiencia resultante con las aplicaciones o sitios que aloja en sus instancias.</p>

La siguiente ilustración representa las transiciones entre los estados de las instancias:
<p align= "center">
  <img src=https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/6146f707-3b7b-4716-939d-5fb7f67a16e8"" width="900">
</p>

Amazon EC2 ofrece las siguientes opciones de compra en función de sus necesidades:
- Instancias bajo demanda
- Instancias reservadas
- Instancias programadas
- Instancias de spot
- Alojamientos dedicados
- Instancias dedicadas
- Reservaciones de capacidad

<p align="justify">Si necesita una reservación de capacidad, compre instancias reservadas o reservaciones de capacidad para una zona de disponibilidad específica o bien compre instancias programadas. Las instancias de spot son una opción rentable si usted es flexible en relación al momento en que se ejecutan sus aplicaciones y si estas se pueden interrumpir. Los alojamientos dedicados o las instancias dedicadas pueden ayudarlo a abordar los requisitos de conformidad y reducir costos mediante sus licencias de software vinculadas al servidor existentes.</p>

<p align="justify">Lambda es un entorno informático sin servidor que facilita la ejecución de código en respuesta a eventos como cambios en buckets de Amazon Simple Storage Service (Amazon S3), actualizaciones a una tabla de Amazon DynamoDB o eventos personalizados generados por sus aplicaciones o dispositivos. Con Lambda, no tiene que aprovisionar sus propias instancias. Lambda realiza todas las actividades operativas y administrativas en su nombre, entre ellas, el aprovisionamiento de capacidad, el monitoreo del estado de la flota, la aplicación de parches de seguridad a los recursos de cómputo subyacentes, la implementación de código, la ejecución de frontend de servicio web y el monitoreo y registro de código. Lambda proporciona escalado y alta disponibilidad a su código sin esfuerzo adicional de su parte.</p>

## Laboratorio del módulo 6: Creación de una función de Lambda
### Tarea 1: Crear una función de Lambda
Seleccione Create a function (Crear función) y configure lo siguiente:
- En Function name (Nombre de la función), ingrese my-function.
- En la sección Permissions (Permisos), expanda la opción Change default execution role (Cambiar el rol de ejecución predeterminado).
- En Execution role (Rol de ejecución): elija Use an existing role (Utilizar un rol existente).
- En Existing role (Rol existente), elija LambdaAccessToCloudWatch.
- Seleccione Create function (Crear función).

Lambda crea una función Node.js que escribe el texto "Hello from Lambda!". <br>
**Nota:** En este laboratorio se utiliza Node.js, pero Lambda es capaz de utilizar varios lenguajes, incluidos Python y C#.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/c7e48cb0-644b-48fd-8ddf-5ff891ad2872" width="900">
</p>

### Tarea 2: Probar la función
Puede utilizar el diseñador para probar su función.
- Vaya a la sección Code source (Fuente de código) y elija la pestaña Test (Prueba). Aquí puede crear nuevos scripts de prueba o modificar los existentes.
- En Event name (Nombre del evento), escriba mytestevent y, a continuación, elija Save (Guardar).
- Para ejecutar la prueba, elija Test (Probar).
- Los resultados de la prueba aparecen en la sección Code source (Fuente del código). En el estado debería aparecer Succeeded (Realizado correctamente). En la sección Function logs (Registros de la función) de los resultados, puede ver la Duration (Duración), que es el tiempo que ha tardado en completarse la función. También se muestra otra información sobre la prueba.
#### Nota
- Un evento de prueba es un objeto JSON que imita la estructura de las solicitudes emitidas por los servicios AWS para invocar una función de Lambda. Se utiliza para ver el resultado de la invocación de la función.
- Para invocar la función sin guardar un evento, configure el evento JSON y luego elija probar.
  
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/604f81cd-d8b0-4a6a-8804-62d4b84dce2a" width="900">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/b88e7807-4078-43d2-9352-50d3c08284fc" width="900">
</p>

### Tarea 3: Ver las métricas y registros de CloudWatch
<p align= "center">
  <img src=https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/d3ac8634-ed4e-4be6-8a04-9e87101ca226"" width="900">
  <img src=https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/5e68357d-ae14-4a63-8180-957d8025a4fe"" width="900">
</p>
