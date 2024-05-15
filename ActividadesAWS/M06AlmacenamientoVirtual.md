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

## Laboratorio: Adjuntar un volumen de EBS
### Objetivo
Crear un volumen de EBS y asociarlo a una instancia EC2.

### Preguntas
#### ¿Algún paso en el laboratorio fue confuso? ¿Dónde podría buscar respuestas?
<p align="justify">
No fue confuso en absoluto, puedo encontrar más información en la documentación de AWS.</p>

#### ¿Cómo cree que Amazon EBS podría ayudar a que una escuela funcione de manera más eficaz?
<p align="justify">
Amazon EBS puede ayudar a una escuela almacenando la base de datos de estudiantes, registros académicos, entre otros.</p>

#### ¿Qué problema considera importante y cómo podría utilizar sus conocimientos sobre Amazon EBS y otros servicios en la nube para solucionar ese problema?
<p align="justify">
Al utilizar Amazon EBS y otros servicios en la nube de AWS, las escuelas pueden abordar eficazmente el desafío de gestionar grandes cantidades de datos educativos al tiempo que garantizan la seguridad, la disponibilidad y el rendimiento del acceso a los datos en un entorno digitalizado y de aprendizaje remoto.</p>
