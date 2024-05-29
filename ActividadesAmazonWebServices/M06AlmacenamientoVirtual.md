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
El almacenamiento de Amazon EBS se implementa como una serie de bloques de longitud fija que el sistema operativo puede leer y escribir. No se almacena nada de lo que representan estos bloques o sus atributos. Los bloques se parecen mucho a los sistemas de archivos del Sistema de archivos de nueva tecnología (NTFS) o de la Tabla de asignación de archivos (FAT) que se ejecutan en su equipo PC o Mac. Esto significa que se puede acceder a ellos rápidamente.</p>

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/a3491935-125e-4f35-be1c-41c43cf302d3">
</p>

<p align="justify">
El almacenamiento de Amazon S3 se implementa como un objeto que la aplicación que lo utiliza debe leer y escribir. Los objetos contienen metadatos, es decir, datos sobre los atributos del objeto que ayudan al sistema a catalogar e identificar dicho objeto. Algunos ejemplos de objetos son imágenes, videos y música. Los objetos no se pueden procesar de forma incremental. Deben leerse y escribirse en su totalidad. Esto puede tener implicaciones de rendimiento y consistencia.</p>
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
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/384cb740-8177-40c9-ba11-24d470fc8d94" width="800">
</p>

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
