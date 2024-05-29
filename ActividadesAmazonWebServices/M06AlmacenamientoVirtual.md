<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Módulo 6: Almacenamiento Virtual</h1>
</p>

## Finalidad del módulo
Compararemos Amazon Elastic Block Store (Amazon EBS) con Amazon Simple Storage Service (Amazon S3) y aprenderemos sobre los distintos niveles de almacenamiento y cómo elegir el mejor tipo de almacenamiento para una determinada situación.

## Terminología
| Término  | Concepto  |
| :------------: | :------------: |
| Amazon Elastic Block Store (EBS)  | <p align="justify">Almacenamiento para instancias específicas de Amazon EC2.</p>  |
| Amazon Elastic Compute Cloud (EC2)  | <p align="justify">Servicio web que ofrece capacidad informática escalable en la nube.</p>  |
| Unidad de disco duro (HDD)  |  <p align="justify">Almacenamiento más lento que utiliza un disco giratorio para almacenar datos.</p> |
| Operaciones de entrada y salida por segundo (IOPS)  |  <p align="justify">Medida de rendimiento frecuente que se utiliza para comparar dispositivos de almacenamiento.</p> |
| Unidad de estado sólido (SDD)  | <p align="justify">Almacenamiento muy rápido que utiliza memoria flash.</p>  |

## Antecedentes y conceptos
<p align="justify">
Elastic Block Store (EBS) y Simple Storage Service (S3) son dos servicios de almacenamiento en la nube ofrecidos por Amazon Web Services (AWS), pero tienen diferentes propósitos y características:

Elastic Block Store (EBS):

- Bloques de almacenamiento: EBS proporciona almacenamiento de bloques para instancias de Amazon EC2 (Elastic Compute Cloud).
- Persistencia: Los datos en EBS son persistentes y se mantienen incluso después de que se apague la instancia EC2 a la que está adjunto el volumen de EBS.
- Acceso de nivel de bloque: EBS permite el acceso de nivel de bloque, lo que lo hace adecuado para sistemas de archivos que requieren acceso de bajo nivel, como sistemas de archivos de bases de datos.
- Uso para sistemas de archivos y bases de datos: EBS se utiliza comúnmente para almacenar el sistema de archivos raíz de una instancia EC2, así como para almacenar datos de bases de datos que requieren un alto rendimiento y persistencia.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/a3491935-125e-4f35-be1c-41c43cf302d3">
</p>

Simple Storage Service (S3):

- Almacenamiento de objetos: S3 ofrece almacenamiento de objetos para datos en la nube, que pueden ser archivos, imágenes, videos, documentos, etc.
- Escalabilidad y durabilidad: S3 es altamente escalable y está diseñado para ofrecer una alta durabilidad de los datos. Los datos se almacenan en múltiples ubicaciones y están replicados automáticamente.
- Acceso a través de API HTTP: S3 proporciona acceso a los datos a través de una API HTTP, lo que facilita su integración con una amplia variedad de aplicaciones y servicios.
- Adecuado para almacenamiento de objetos: S3 es ideal para almacenar grandes cantidades de datos no estructurados, como archivos multimedia, copias de seguridad, archivos de registro, etc.</p>

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/e599b144-8cf2-4d7b-94ea-7de609978021">
</p>

## Laboratorio del módulo 6: Asociar un volumen de EBS
### Tarea 1. Comenzar a crear la instancia y asignarle un nombre
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/46dceaad-197a-466b-8456-3e39101768a6" width="800">
</p>

### Tarea 2. Imágenes de aplicación y SO
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/d907735c-7540-4bae-94ae-9c6c5db8f5c5" width="800">
</p>

### Tarea 3. Elegir el tipo de instancia
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/9d5aacfb-5ea6-425a-b619-94432abc63b7" width="800">
</p>

### Tarea 4. Seleccionar un par de claves
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/d9423a5c-e5b9-4ca8-a3c1-dcbad7f9876d" width="800">
</p>

### Tarea 5. Configuración de red
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/30c6543b-602c-4119-9579-ccb638f7cb46" width="800">
</p>

### Tarea 6. Configurar el almacenamiento
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/e46b61ee-02c3-40b7-96bf-3b6104a94aee" width="800">
</p>

### Tarea 7: Detalles avanzados
```
#!/bin/bash
yum update -y
yum -y install httpd
systemctl enable httpd
systemctl start httpd
echo '<html><h1>Hello World!</h1></html>' > /var/www/html/index.html
```
Este script bash se ejecutará sin permisos de usuario raíz en el SO invitado de la instancia. Se ejecutará automáticamente cuando la instancia se inicie por primera vez. Este script hace lo siguiente:
- Actualiza el servidor
- Instala un servidor web Apache (httpd)
- Configura el servidor web para que comience automáticamente durante el arranque
- Activa el servidor web
- Crea una página web sencilla<br>

### Tarea 8: Revisar la instancia y lanzarla
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/fc7f0381-c405-48f4-985b-b2d5e46da8b1" width="800">
</p>

### Tarea 9. Acceder a la instancia de EC2
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/f96419b0-acf2-440a-8e31-92e81e1c30ab" width="800">
</p>

### Tarea 10. Actualizar el grupo de seguridad
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/33c935db-8ab9-4012-80a7-d505e39600c6" width="800">
</p>

### Tarea 11: Crear una regla de entrada
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/055a5437-78be-495c-81b8-78c75c4d3db8" width="800">
</p>
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/82e9bcd0-fa6e-444a-86c2-da1afddd36f2" width="800">
</p>

### Tarea 12. Probar la regla
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/ba8eb08e-4644-4cd8-93b2-5ddc5a5e4828" width="800">
</p>

### Tarea 13: Adjuntar un volumen de EBS a la instancia de EC2
El volumen de EBS que vas a crear pronto tendrá que estar en la misma zona de disponibilidad.
- En Elastic Block Store, selecciona Volúmenes. Selecciona Crear volumen.
- En Tamaño, introduce 1 para crear un volumen con 1 GiB.
- En Zona de disponibilidad, selecciona la misma zona de disponibilidad en la que se ejecuta la instancia de EC2.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/c92c1a79-a32f-4314-9a6b-2d638b39d832" width="800">
</p>

- Selecciona el menú desplegable Instancia y selecciona tu instancia de EC2. Luego asocia el volumen a la instancia.
- El estado del volumen cambia a en uso. El nuevo volumen se ha adjuntado a la instancia de EC2.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/79ee59c0-84a1-420b-8816-a7533c52b3f6" width="800">
</p>
