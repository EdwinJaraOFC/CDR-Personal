<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Módulo 4: Servidores Virtuales</h1>
</p>

## Finalidad del módulo
<p align="justify">
Aprenderemos a crear una instancia de Amazon Elastic Compute Cloud (Amazon EC2) y utilizarla para alojar un sitio web. También aprenderemos la finalidad de las claves de acceso, un sistema de nombres de dominio (DNS), Amazon Route 53 y nubes privadas virtuales.</p>

## Terminología
### Amazon Elastic Compute Cloud (Amazon EC2)
Servicio web que ofrece capacidad informática escalable en la nube. Considérelo como alquilar una computadora en la nube.

### Amazon Simple Storage Service (Amazon S3)
Servicio proporcionado por Amazon Web Services (AWS) que almacena datos para los usuarios en la nube.

### Sistema de nombres de dominio (DNS)
Sistema de nomenclatura para computadoras, dispositivos y recursos conectados a una red.

### Bucket de Amazon Simple Storage Service (Amazon S3)
Un contenedor de objetos (como imágenes, archivos de audio, archivos de video, documentos, etc.) en Amazon S3.

### Política
Objeto de AWS que, cuando se asocia a una identidad o un recurso, define sus permisos. AWS evalúa estas políticas cuando una entidad principal (usuario o rol) realiza una solicitud.

### Nombre de dominio
Etiqueta que identifica una red de computadoras bajo control centralizado.

### Amazon Route 53
El servicio web DNS de AWS.

### Nube privada virtual (VPC)
Red virtual dedicada a su cuenta de AWS. Esta infraestructura está aislada de forma lógica de otras redes virtuales de la nuve de AWS. Todos sus servicios de AWS se pueden lanzar desde una VPC. Resulta útil para proteger los datos y administrar quién puede acceder a la red.

### Notación de objetos JavaScript (JSON)
Sintaxis para almacenar e intercambiar datos.

### Sitio web dinámico
Sitio web que cambia según las interacciones del usuario; a menudo se crea con Python, JavaScript, PHP o ASP con lenguaje de marcado de hipertexto (HTML).

### Sitio web estático
Un sitio web que no cambia según las interacciones del usuario; normalmente se crea con HTML y hojas de estilo en cascada (CSS).

## Preguntas de enfoque

1. A menudo, la finalidad de un sitio web (o aplicación) no es el mismo para un usuario que para el creador. Por ejemplo, el motor de búsqueda de Google proporciona un servicio a los usuarios proporcionando capacidades de búsqueda rápidas y eficaces. Sin embargo, para Google, las búsquedas proporcionan datos sobre los usuarios que Google puede analizar para presentar a los usuarios anuncios específicos. Piense en un sitio web (o aplicación) que usa a menudo. ¿Cuál es la finalidad del sitio web (o aplicación) para el usuario y el creador? ¿Son estas finalidades similares o diferentes?

2. El nombre de dominio de un sitio web suele ser nuestra primera impresión de un sitio web, incluso antes de ver el contenido. Nombres como Wikipedia, Twitter y Facebook evocan ideas sobre cómo se utilizarán. Sin embargo, nombres como Google y Amazon no dicen mucho sobre su finalidad. ¿Qué factores cree que son importantes a la hora de nombrar un sitio web y por qué? ¿Cómo afecta el nombre de un sitio web a la experiencia y las impresiones que el usuario tiene en ese sitio? Al nombrar su propio sitio web, ¿cuáles serán, al menos, los dos factores más importantes para usted? 

3. Muchos sitios web almacenan datos sobre su uso del sitio web en la computadora (denominados cookies) o en el sitio web (denominados variables de sesión). Estos datos permiten al sitio web no solo personalizar su uso, sino también conocer sus patrones e historial de uso. Esto significa que los sitios web pueden ofrecer mejores recomendaciones y completar formularios de forma automática rápidamente. Sin embargo, también significa que pueden vender su información a anunciantes. Esto puede significar un acceso más fácil y eficiente a costa de la privacidad. Cuando se trata de este tipo de recopilación de datos, ¿considera que el intercambio vale la pena? ¿Por qué sí o por qué no? ¿Deberían los sitios web ser más transparentes acerca de qué tipos de datos están recopilando? ¿Debería poder optar por no participar?

## Laboratorio 1: Lanzamiento de una instancia EC2
### Objetivo
Crear una instancia de EC2 que aloja un sitio web sencillo.
### Preguntas
1. ¿Necesita una explicación más detallada de los pasos para crear una instancia EC2 para alojar un sitio web? ¿Dónde cree que podría buscar más información sobre esa parte del proceso?
2. Abrió el servidor para que se acceda desde cualquier puerto. ¿En qué cree que la configuración del grupo de seguridad sería diferente para una gran empresa como AWS?
3. ¿Tiene alguna otra pregunta sobre el proceso de creación de una instancia EC2 y la ejecución de un sitio web?

## Laboratorio 2: Creación de un bucket de S3
### Objetivo
Crear un bucket de S3.
### Preguntas
1. ¿Necesita una explicación más detallada de alguno de los pasos para crear un bucket de S3 para alojar un sitio web? ¿Dónde cree que podría buscar más información sobre esa parte del proceso?
2. Los buckets de S3 escalan automáticamente para ajustarse al tamaño de los datos almacenados. ¿Por qué cree que esto es útil para las empresas que utilizan el servicio Amazon S3?
3. ¿Qué tipos de datos cree que pueden beneficiarse de almacenarse en la nube? ¿Cómo el almacenamiento de los datos en la nube hace que sus datos estén más seguros y protegidos? 
4. ¿Cómo cree que los buckets de S3 están relacionados con las instancias EC2?
