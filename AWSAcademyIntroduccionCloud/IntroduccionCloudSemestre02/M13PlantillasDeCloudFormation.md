<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Módulo 13: Plantillas de CloudFormation</h1>
</p>

## Terminología

| Término  | Concepto  |
| :------------: | :------------: |
| Infraestructura como Código (IaC)  | <p align="justify">Proceso de aprovisionamiento y administración de los recursos de la nube mediante la escritura de un archivo de plantilla que es legiblepor el ser humano y consumible por la máquina. Para AWS la opción integrada para IaC es CloudFormation.</p>  |
| Pila  | <p align="justify">Colección de recursos de AWS que puede administrar como una sola unidad. En otras palabras, puede crear, actualizar o eliminar un conjunto de recursos mediante la creación, actualización o eliminación de pilas.</p>  |

## Conceptos

<p align="justify">CloudFormation es un servicio que facilita la creación y gestión de recursos en AWS, como Amazon EC2 y S3, mediante Infraestructura como Código (IaC). Los usuarios pueden usar scripts y plantillas preconstruidas para aprovisionar y administrar recursos de forma rápida y fiable, conceptualizando CloudFormation como la estructura virtual de la nube, similar a la arquitectura física de los sistemas informáticos tradicionales.</p>

<p align="justify">CloudFormation permite crear, actualizar y replicar fácilmente pilas de servicios, usando lenguajes de programación o archivos de texto para modelar y aprovisionar recursos de AWS y terceros de manera automatizada y segura. Las plantillas, escritas en JSON o YAML, se pueden gestionar desde la consola de AWS, facilitando el proceso en comparación con escribir código manualmente por un equipo de DevOps.</p>

## Laboratorio del módulo 13: Creación de un entorno con CloudFormation
### Tarea: Crear una pila a partir de una plantilla
- Elija el menú Services (Servicios), localice la categoría Management & Governance (Administración y gobernanza) y elija CloudFormation.
- Elija Create Stack > With new resources (Crear pila > Con recursos nuevos [estándar]).
- Para Prepare template (Preparar plantilla), elija Use a sample template (Utilizar una plantilla de muestra).
- Para Sample templates (Plantillas de muestra), elija LAMP Stack (Pila LAMP) de la sección Simple (Simple) de la lista.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/0b085193-727b-4835-b249-c60eed39dbe1" width="900">
</p>
<p align="justify">Esta plantilla incluye una instancia única de Amazon Elastic Compute Cloud (Amazon EC2) y una base de datos MySQL para el almacenamiento.</p>
<p align="justify">Ahora que ha seleccionado una plantilla, utilizará CloudFormation Designer para visualizar sus partes. El diseñador es una herramienta gráfica para crear, ver y modificar las plantillas de CloudFormation. Puede diagramar los recursos de plantillas mediante una interfaz de arrastrar y soltar y, a continuación, editar los detalles con el editor de código integrado. El diseñador puede ayudarlo a ver con rapidez la relación entre los recursos en una plantilla.</p>

- Elija View in Designer (Ver en el diseñador).

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/010ced61-56f6-41b8-b053-cf51c7aec1c3" width="900">
</p>

El diseñador tiene cuatro paneles:

| Panel  | Descripción  |
| :------------: | :------------: |
| Canvas  | <p align="justify">Este panel es el más grande y es donde los recursos de la plantilla se muestran como un diagrama. Los cambios que realice aquí modifican de manera automática el código de la plantilla.</p>  |
| Tipos de recursos  | <p align="justify">Este panel, situado en la parte izquierda de la página, muestra todos los recursos de la plantilla que puede agregar a ella, clasificados por el nombre del servicio de AWS. Para agregar recursos a la plantilla, arrástrelos desde este panel hasta el panel canvas.</p>  |
| Editor integrado  | <p align="justify">En el editor, especifique los detalles de la plantilla, como propiedades del recurso o parámetros de la plantilla, mediante el código JSON o YAML. Cuando selecciona un elemento en el canvas, el diseñador destaca el código relacionado en el editor. Si edita el código, debe actualizar el canvas para hacer lo mismo con el diagrama.</p>  |
| Panel de mensajes  | <p align="justify">Este panel situado en la esquina superior derecha del diseñador muestra mensajes.</p>  |
