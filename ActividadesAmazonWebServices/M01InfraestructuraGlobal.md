<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Módulo 1: Infraestructura global</h1>
</p>

## Terminología
| Término | Concepto |
| :------------: | :------------: |
| Informática en la nube | <p align="justify">Es la distribución de recursos de TI bajo demanda a través de Internet mediante un esquema de pago por uso.</p>|
| Amazon Web Services (AWS) | <p align="justify">Una plataforma que proporciona una amplia gama de servicios de informática en la nube.</p>|
| Almacenamiento en nube | <p align="justify">Guardar datos mediante un proveedor de servicios en la nube (CSP) en lugar de una máquina física.</p>|
| Servidor | <p align="justify">Un equipo diseñado para procesar solicitudes y entregar datos a otro equipo a través de Internet o de una red local. En la nube, un servidor está alojado por un proveedor externo al que se accede a través de Internet.</p>|


## Antecedentes y conceptos
### ¿Qué tipos de servicios en la nube existen?
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/d43bdcde-5149-406a-9f2b-967b9c0506c0">
</p>

### ¿Cuáles son las principales diferencias en la forma en que las empresas utilizan los servicios?
<p align="justify">
  
- **Infraestructura como servicio (IaaS):** Usada por grandes empresas para crear sus propias estructuras que satisfacen sus necesidades.
- **Plataforma como servicio (PaaS):** Usada por empresas y desarrolladores para construir y ofrecer aplicaciones a sus clientes.
- **Software como servicio (SaaS):** Usadas por empresas y usuarios para acceder a aplicaciones y servicios listos para usarse en la web.</p>

## Laboratorio 1 del módulo 4: Lanzamiento de una instancia de EC2
### Tarea 1: Comenzar a crear la instancia y asignarle un nombre
Las etiquetas te permiten clasificar los recursos de AWS de diferentes maneras: por ejemplo, por finalidad, propietario o entorno. Name es otra etiqueta diferente. La clave de esta etiqueta es Name y el valor es Web Server 1.
![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/14f1c374-6706-4dd9-9cad-2cf677439326)

### Tarea 2: Imágenes de aplicación y SO
Name es otra etiqueta diferente. La clave de esta etiqueta es Name y el valor es Web Server 1.
![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/ea6e03aa-f864-4c0b-b796-dfc01880757a)

### Tarea 3: Elegir el tipo de instancia
El Tipo de instancia define los recursos de hardware asignados a la instancia. Este tipo de instancia tiene 1 unidad de procesamiento central virtual (CPU) y 1 GiB de memoria.
![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/06b2710e-81ad-458e-99cc-1fec667f4951)

### Tarea 4: Seleccionar un par de claves
El par de claves vockey que has seleccionado te permitirá conectarte a esta instancia mediante SSH después de que se haya iniciado.
![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/fa55f25c-367d-4f62-8e9d-91a96a63c7de)

### Tarea 5: Configuración de red
La red indica la nube virtual privada (VPC) en la que quieres lanzar la instancia. Puede tener varias redes; por ejemplo, una para desarrollo, una segunda para pruebas y una tercera para producción.
![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/14d38ada-9985-4e3e-a2b8-a0305a6b3bdd)

Un grupo de seguridad actúa como un firewall virtual que controla el tráfico de una o varias instancias. Cuando inicias una instancia, la asocias a uno o varios grupos de seguridad. Añades reglas a cada grupo de seguridad que permiten que el tráfico fluya a sus instancias asociadas o desde ellas. Las reglas de un grupo de seguridad se pueden modificar en cualquier momento. Las nuevas reglas se aplican automáticamente a todas las instancias que estén asociadas al grupo de seguridad.
![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/4d91c33c-af47-43ec-a506-e642165e3711)

### Tarea 6: Configurar el almacenamiento
Volumen raíz (denominado también volumen de arranque)
![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/8c86d2f9-6bb8-4dfd-bd99-199ce07cd9c4)

### Tarea 7: Detalles avanzados
Este script bash se ejecutará sin permisos de usuario raíz en el SO invitado de la instancia. Se ejecutará automáticamente cuando la instancia se inicie por primera vez. Este script hace lo siguiente:
- Actualiza el servidor
- Instala un servidor web Apache (httpd)
- Configura el servidor web para que comience automáticamente durante el arranque
- Activa el servidor web
- Crea una página web sencilla<br>
![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/d9ad2277-ec78-4314-a730-a7b24fc31886)

### Tarea 8: Revisar la instancia y lanzarla
![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/ee52942a-43c6-44ff-8f35-08528ea627c7)

### Tarea 9: Acceder a la instancia de EC2
Dirección IPv4 pública: 54.234.58.248<br>
![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/53f995a6-3ec0-412c-9e0f-6950845f71e5)

### Tarea 10: Actualizar el grupo de seguridad
No se podía acceder al servidor web porque el grupo de seguridad no permite el tráfico entrante en el puerto 80, que se utiliza para las solicitudes web HTTP.
![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/d316065e-1be4-48bd-b06b-5edf67f6f609)

### Tarea 11: Crear una regla de entrada
![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/88e69497-560d-4dc6-b77b-1d874e3e3b4a)

### Tarea 12: Probar la regla
![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/407d72ef-700d-4ccf-aac5-29f4eb246c26)
![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/3cb23b1b-515e-4edd-89cc-24edeb7fee10)
