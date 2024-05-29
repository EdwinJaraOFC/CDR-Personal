<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Módulo 4: Servidores Virtuales</h1>
</p>

## Terminología
|  Término | Concepto  |
| :------------: | :------------: |
| Amazon Elastic Compute Cloud (Amazon EC2)  | <p align="justify">Servicio web que ofrece capacidad de cómputo escalable en la nube. Considérelo como alquilar un equipo en la nube.</p>  |
| Amazon Simple Storage Service (Amazon S3)  | <p align="justify">Servicio que almacena datos para los usuarios en la nube.</p>  |
| Sistema de nombres de dominio (DNS)  | <p align="justify">Sistema de nomenclatura para computadoras, dispositivos y recursos conectados a una red.</p>  |
|  Bucket de Amazon S3 |  <p align="justify">Un contenedor de objetos (como imágenes, archivos de audio, documentos, etc.) en Amazon S3.</p> |
| Política  | <p align="justify">Objeto de AWS que, cuando se asocia a una identidad o un recurso, define sus permisos. AWS evalúa estas políticas cuando una entidad principal (usuario o rol) realiza una solicitud.</p>  |
|  Nombre de dominio | <p align="justify">Etiqueta que identifica una red de computadoras bajo control centralizado.</p>  |
|  Amazon Route 53 |  <p align="justify">El servicio web DNS de AWS.</p> |
|  Nube privada virtual (VPC) |  <p align="justify">Red virtual dedicada a su cuenta de AWS. Esta infraestructura está aislada de forma lógica de otras redes virtuales de la nuve de AWS. Todos sus servicios de AWS se pueden lanzar desde una VPC. Resulta útil para proteger los datos y administrar quién puede acceder a la red.</p> |
|  Notación de objetos JavaScript (JSON) | <p align="justify">Sintaxis para almacenar e intercambiar datos.</p>  |
| Sitio web dinámico  | <p align="justify">Sitio web que cambia según las interacciones del usuario; a menudo se crea con Python, JavaScript, PHP o ASP con lenguaje de marcado de hipertexto (HTML).</p>  |
| Sitio web estático  |  <p align="justify">Un sitio web que no cambia según las interacciones del usuario; normalmente se crea con HTML y hojas de estilo en cascada (CSS).</p> |

## Conceptos Generales
<div align="center"; style="display: flex; justify-content: space-between;">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/5293303b-639b-4cd8-b233-0ad252466e4a" width="380px"/>
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/a26c8c4f-5546-4d5a-ae4b-a43307c25e70" width="615px"/>
</div>

## Laboratorio 1 del módulo 4: Lanzamiento de una instancia de EC2
### Tarea 1: Comenzar a crear la instancia y asignarle un nombre
Las etiquetas te permiten clasificar los recursos de AWS de diferentes maneras: por ejemplo, por finalidad, propietario o entorno. Name es otra etiqueta diferente. La clave de esta etiqueta es Name y el valor es Web Server 1.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/14f1c374-6706-4dd9-9cad-2cf677439326" width="800">
</p>

### Tarea 2: Imágenes de aplicación y SO
El tipo de imagen de máquina de Amazon (AMI) que selecciones determina el sistema operativo (SO) que se ejecutará en la instancia de EC2 que inicies. En este caso, has seleccionado Amazon Linux 2023 como SO invitado.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/ea6e03aa-f864-4c0b-b796-dfc01880757a" width="800">
</p>

### Tarea 3: Elegir el tipo de instancia
El Tipo de instancia define los recursos de hardware asignados a la instancia. Este tipo de instancia tiene 1 unidad de procesamiento central virtual (CPU) y 1 GiB de memoria.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/06b2710e-81ad-458e-99cc-1fec667f4951" width="800">
</p>

### Tarea 4: Seleccionar un par de claves
El par de claves vockey que has seleccionado te permitirá conectarte a esta instancia mediante SSH después de que se haya iniciado.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/fa55f25c-367d-4f62-8e9d-91a96a63c7de" width="800">
</p>

### Tarea 5: Configuración de red
La red indica la nube virtual privada (VPC) en la que quieres lanzar la instancia. Puede tener varias redes; por ejemplo, una para desarrollo, una segunda para pruebas y una tercera para producción.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/14d38ada-9985-4e3e-a2b8-a0305a6b3bdd" width="800">
</p>

Un grupo de seguridad actúa como un firewall virtual que controla el tráfico de una o varias instancias. Cuando inicias una instancia, la asocias a uno o varios grupos de seguridad. Añades reglas a cada grupo de seguridad que permiten que el tráfico fluya a sus instancias asociadas o desde ellas.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/4d91c33c-af47-43ec-a506-e642165e3711" width="800">
</p>

### Tarea 6: Configurar el almacenamiento
Volumen raíz (denominado también volumen de arranque).
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/8c86d2f9-6bb8-4dfd-bd99-199ce07cd9c4" width="800">
</p>

### Tarea 7: Detalles avanzados
Este script bash se ejecutará sin permisos de usuario raíz en el SO invitado de la instancia. Se ejecutará automáticamente cuando la instancia se inicie por primera vez. Este script hace lo siguiente:
- Actualiza el servidor
- Instala un servidor web Apache (httpd)
- Configura el servidor web para que comience automáticamente durante el arranque
- Activa el servidor web
- Crea una página web sencilla<br>
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/d9ad2277-ec78-4314-a730-a7b24fc31886" width="800">
</p>

### Tarea 8: Revisar la instancia y lanzarla
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/ee52942a-43c6-44ff-8f35-08528ea627c7" width="800">
</p>

### Tarea 9: Acceder a la instancia de EC2
Dirección IPv4 pública: 54.234.58.248<br>
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/53f995a6-3ec0-412c-9e0f-6950845f71e5" width="800">
</p>

### Tarea 10: Actualizar el grupo de seguridad
No se podía acceder al servidor web porque el grupo de seguridad no permite el tráfico entrante en el puerto 80, que se utiliza para las solicitudes web HTTP.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/fd3bb33c-7f6a-4410-bc35-28ae0fc350d6" width="800">
</p>

### Tarea 11: Crear una regla de entrada
Configura lo siguiente:
- Tipo: HTTP
- Fuente: Cualquier lugar-IPv4
- Selecciona Guardar reglas

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/13248397-ddc9-4bee-a75d-ad5676e5f1c1" width="800">
</p>

### Tarea 12: Probar la regla
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/606458df-2ffb-4f79-b57e-b1ee7e7e6705" width="800">
</p>
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/3cb23b1b-515e-4edd-89cc-24edeb7fee10" width="500">
</p>

## Laboratorio 2 del módulo 4: Creación de un bucket de S3
### Tarea 1: Crear un bucket de S3
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/ebe97fe5-6e06-47fd-b6a9-973622401ffd" width="800">
</p>
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/fcff8d20-e849-4ddd-a848-fa91f7be7d1e" width="800">
</p>
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/69ebabd9-6f0d-4e87-961c-b003cbec0123" width="800">
</p>
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/8d993489-957b-422d-b3eb-edb71ece66cf" width="800">
</p>

### Tarea 2: Añadir una política de bucket para que el contenido esté disponible públicamente
La política del bucket, escrita en JSON, proporciona acceso a los objetos almacenados en el bucket. Las políticas de bucket no se aplican a los objetos que pertenecen a otras cuentas.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/ad89d471-a0ea-4715-9de9-0832bda5246a" width="800">
</p>

### Tarea 3: Subir un documento HTML
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/fc4eb5f7-2249-4aaa-a8ad-29dd5dc7ff88" width="800">
</p>
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/40e7da00-66bc-463a-944a-72a3881ef7c6" width="800">
</p>

### Tarea 4: Probar el sitio web
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/0343cb82-53e2-407c-9ecf-6d9036e10831" width="800">
</p>
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/7044d494-382e-4683-81a8-f8f90544bb2b" width="800">
</p>
