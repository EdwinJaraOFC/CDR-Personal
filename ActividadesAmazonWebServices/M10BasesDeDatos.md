<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Módulo 10: Bases de Datos</h1>
</p>

## Finalidad del módulo
Obtendremos información sobre Amazon Relational Database Service (Amazon RDS), Amazon DynamoDB y el almacén de datos con Amazon Redshift. También compararemos las bases de datos relacionales y no relacionales y el procesamiento de transacciones en línea (OLTP) y el procesamiento analítico en línea (OLAP).

## Terminología
| Término  | Concepto  |
| :------------: | :------------: |
| Base de datos relacional  | Colección de conjuntos de datos organizados como registros y columnas en tablas. En un sistema de base de datos relacional, se definen relaciones entre las tablas de base de datos. Piense en una base de datos relacional como un conjunto de datos con relaciones 1 a 1 y 1 a varios. Por ejemplo, una base de datos de clientes haría coincidir a cada cliente con un identificador que identifica al cliente de forma exclusiva. Los desarrolladores utilizan un lenguaje de consulta estructurada (SQL) para interactuar con la base de datos.  |
| Amazon Relational Database Service (Amazon RDS)  | Amazon RDS permite a los desarrolladores crear y administrar bases de datos relacionales en la nube. También permite a los desarrolladores realizar un seguimiento de grandes cantidades de datos, organizarlos y buscarlos de manera eficiente.  |
| Amazon DynamoDB  | Servicio de base de datos no relacional en AWS. Los datos se almacenan en pares clave-valor.  |
| Base de datos no relacional  | También se denomina base de datos "NoSQL" o "No solo SQL". Cada entrada se almacena en un par clave-valor en el que cada clave se adjunta a valores. Cada entrada puede tener un número diferente de valores adjuntos a una clave.  |
| Amazon Redshift  | Servicio de almacenamiento de datos de AWS, que puede almacenar enormes cantidades de datos de forma que se pueda consultar rapidamente con fines de inteligencia empresarial (BI).  |
| Procesamiento de transacciones en línea (OLTP)  | Categoría de procesamiento de datos que se centra en tareas orientadas a las transacciones. El OLTP normalmente consiste en insertar, actualizar o eliminar pequeñas cantidades de datos en una base de datos.  |
| Procesamiento analítico en línea (OLAP)  | Método informático que permite a los usuarios extraer y consultar datos de forma eficiente y selectiva para analizarlos desde diferentes puntos de vista.  |
| Amazon Aurora  | Motor de base de datos relacional compatible con MySQL y PostgreSQL creado para la nube. Combina el rendimiento y la disponibilidad de las bases de datos empresariales tradicionales con la simplicidad y la rentabilidad de las bases de datos de código abierto.  |
| MySQL  | Sistema de administración de base de datos relacional de código abierto.  |

## Antecedentes
OLTP y OLAP

Existen muchos tipos diferentes de bases de datos. Para decidir cuál de ellos necesita, es importante saber cómo se van a procesar los datos. Hay dos tipos de procesamiento de datos: el procesamiento de transacciones en línea (OLTP) y el procesamiento analítico en línea (OLAP).

Las operaciones OLAP son principalmente de solo lectura; es decir, leen los datos y realizan varios tipos de procesamiento, como suma, agrupación y clasificación. Los sistemas de administración de base de datos relacional tienen funciones integradas para realizar este tipo de operaciones. Debido a que están integradas, se hacen de manera eficiente. En una base de datos no relacional, los valores se deben extraer de los pares clave-valor, lo que puede ser un proceso que requiere mucho tiempo.

Sin embargo, las operaciones del OLTP necesitan actualizar la base de datos además de leerla. La actualización puede consistir en agregar, modificar o eliminar valores. La actualización puede ser compleja porque muchas de las tablas de una base de datos relacional son virtuales. Es decir, las tablas deben combinarse en tiempo real con tablas no virtuales. Considere el siguiente ejemplo.

La base de datos de una tienda departamental tiene tablas que contienen información sobre clientes y productos. La tabla de clientes contiene datos relacionados únicamente con los clientes, como el nombre y la dirección. La tabla de productos contiene datos relacionados únicamente con productos, como el nombre y el precio. Para registrar la información sobre las compras, se debe crear una tabla en la que la clave principal combine el ID del cliente y el ID del producto, y que muestre la cantidad de un producto determinado que compró un cliente en particular.

Para mostrar una lectura completa de la compra, la tabla de clientes y la tabla de productos deben combinarse en tiempo real con la tabla de compras para mostrar detalles como el nombre del cliente, el nombre del producto, la cantidad de producto comprado y el costo de la venta. El tipo de operación que combina tablas en tiempo real se denomina unión o JOIN. El resultado de JOIN es una tabla virtual y, en la mayoría de los casos, no se puede actualizar directamente.

Por último, las consideraciones de integridad deben tratarse en una base de datos relacional. En el ejemplo, si es necesario eliminar un producto de la tabla de productos, debe haber reglas para asegurarse de que también se tratan las referencias al producto. Este tipo de reglas se conocen como reglas de integridad y consistencia.

El OLTP se realiza mejor en bases de datos no relacionales, mientras que los procesos del OLAP se realizan mejor en bases de datos relacionales.

Comparación de OLTP y OLAP
![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/b03d1740-445f-4349-a171-d466c7864740)

Aplicaciones del OLTP

Registrar pedidos en línea.
Procesar compras.
Almacenar detalles de clientes.
Aplicaciones del OLAP

Analizar los patrones de compra para hacer recomendaciones.
Hacer un seguimiento de las tendencias de compra para hacer publicidad específica.
Analizar las tendencias estacionales de compra para asegurarse de que los artículos estén en stock.
Servicios de bases de datos de AWS

Amazon RDS es la base de datos relacional clásica que utiliza SQL, Oracle, Aurora u otros sistemas de base de datos similares. Imagine que se trata de un libro de calificaciones en el que cada estudiante es una fila y todos los estudiantes tienen el mismo número de tareas (columnas). Las empresas pueden utilizar el código para buscar datos específicos en función de la información de las filas y columnas. Amazon RDS resulta útil para las empresas que almacenan una cantidad moderada de datos de estructura uniforme, lo que significa que cada ID único (como el nombre del estudiante) se adjunta al mismo número de puntos de datos (calificaciones).

Amazon RDS se utiliza principalmente para el OLTP porque tiene mejores métodos para mantener la integridad y consistencia de la base de datos al procesar datos.

DynamoDB es una base de datos no relacional, lo que significa que no se pueden utilizar sistemas tradicionales como SQL o Aurora. Cada elemento de la base de datos se almacena como un par clave-valor o un archivo de notación de objetos de JavaScript (JSON). Esto significa que cada fila puede tener un número diferente de columnas. No es necesario que todas las entradas se emparejen de la misma manera. Esto permite una flexibilidad en el procesamiento que funciona bien para los blogs, los videojuegos y la publicidad. 

Aurora es un motor de base de datos relacional diseñado específicamente para funcionar con la nube de AWS. Aurora es hasta cinco veces más rápido que las bases de datos MySQL estándar y tres veces más rápido que las bases de datos PostgreSQL estándar. Está diseñado para proporcionar la seguridad, la disponibilidad y la fiabilidad de las bases de datos comerciales a una décima parte del costo. Aurora está completamente administrada por Amazon RDS, que automatiza tareas administrativas que consumen mucho tiempo, tales como aprovisionar hardware, configurar una base de datos, aplicar parches y realizar copias de seguridad.

Amazon Redshift es un almacén de datos rápido y completamente administrado que hace eficiente y rentable analizar todos sus datos a través de SQL estándar y de las herramientas de inteligencia empresarial existentes.

## Laboratorio: Creación de una instancia de base de datos de Amazon RDS
### Objetivo
Comparar bases de datos relacionales y no relacionales.
