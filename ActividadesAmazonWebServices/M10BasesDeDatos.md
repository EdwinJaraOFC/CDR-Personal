<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Módulo 10: Bases de Datos</h1>
</p>

## Finalidad del módulo
Obtendremos información sobre Amazon Relational Database Service (Amazon RDS), Amazon DynamoDB y el almacén de datos con Amazon Redshift. También compararemos las bases de datos relacionales y no relacionales y el procesamiento de transacciones en línea (OLTP) y el procesamiento analítico en línea (OLAP).

## Terminología
| Término  | Concepto  |
| :------------: | :------------: |
| Base de datos relacional  | <p align="justify">Colección de conjuntos de datos organizados como registros y columnas en tablas. En un sistema de base de datos relacional, se definen relaciones entre las tablas de base de datos. Por ejemplo, una base de datos de clientes haría coincidir a cada cliente con un identificador que identifica al cliente de forma exclusiva. Los desarrolladores utilizan un lenguaje de consulta estructurada (SQL) para interactuar con la base de datos.</p>  |
| Amazon Relational Database Service (Amazon RDS)  | <p align="justify">Amazon RDS permite a los desarrolladores crear y administrar bases de datos relacionales en la nube. También permite a los desarrolladores realizar un seguimiento de grandes cantidades de datos, organizarlos y buscarlos de manera eficiente.</p>  |
| Amazon DynamoDB  | <p align="justify">Servicio de base de datos no relacional en AWS. Los datos se almacenan en pares clave-valor.</p>  |
| Base de datos no relacional  | <p align="justify">También se denomina base de datos "NoSQL" o "No solo SQL". Cada entrada se almacena en un par clave-valor en el que cada clave se adjunta a valores. Cada entrada puede tener un número diferente de valores adjuntos a una clave.</p>  |
| Amazon Redshift  | <p align="justify">Servicio de almacenamiento de datos de AWS, que puede almacenar enormes cantidades de datos de forma que se pueda consultar rapidamente con fines de inteligencia empresarial (BI).</p>  |
| Procesamiento de transacciones en línea (OLTP)  | <p align="justify">Categoría de procesamiento de datos que se centra en tareas orientadas a las transacciones. El OLTP normalmente consiste en insertar, actualizar o eliminar pequeñas cantidades de datos en una base de datos.</p>  |
| Procesamiento analítico en línea (OLAP)  | <p align="justify">Método informático que permite a los usuarios extraer y consultar datos de forma eficiente y selectiva para analizarlos desde diferentes puntos de vista.</p>  |
| Amazon Aurora  | <p align="justify">Motor de base de datos relacional compatible con MySQL y PostgreSQL creado para la nube. Combina el rendimiento y la disponibilidad de las bases de datos empresariales tradicionales con la simplicidad y la rentabilidad de las bases de datos de código abierto.</p>  |
| MySQL  | <p align="justify">Sistema de administración de base de datos relacional de código abierto.</p>  |

## Laboratorio del módulo 10: Creación de una instancia de base de datos de Amazon RDS
### Tarea 1. Configurar una instancia de base de datos RDS
En la sección Configuration (Configuración), configure:
- En Engine type (Tipo de motor), elija Microsoft SQL Server.
- En DB instance size (Tamaño de la instancia de la base de datos), elija Free tier (Nivel gratuito).
- Marque la casilla junto a Auto generate a password (Generar automáticamente una contraseña).

![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/f81b60f8-be4a-458d-9a90-97e1753c3d2b)

### Tarea 2. Descargue e instale SQL Server Management Studio
Para conectarse a la instancia de la base de datos RDS, deberá descargar e instalar SQL Server Management Studio.

![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/7658dc98-66a0-472f-a517-7c673a2381bc)

### Tarea 3. Haga que la base de datos sea de acceso público
- En la Configuración adicional. En Public access, seleccione Acceso público.
- En la sección Programación de las modificaciones, en Cuándo aplicar las modificaciones, seleccione Aplicar inmediatamente.

![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/574faff1-026d-4c50-a572-eeb466c6765e)
![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/227b3f52-a307-4227-b21c-02226279d7be)

### Tarea 4. Actualizar el grupo de seguridad de la VPC
De forma predeterminada, el grupo de seguridad predeterminado de la nube virtual privada (VPC) no permite el tráfico entrante de SQL Server desde fuentes externas. 
- Primero obtenga su dirección IP.
- Ahora, modifique el grupo de seguridad para permitir las conexiones entrantes de SQL Server desde el equipo o la instancia de WindowsWorkstation.
- Seleccione Editar reglas de entrada y elija Agregar regla.
- En Tipo, seleccione MSSQL.
- En Origen, elija Personalizado e ingrese la dirección IP o la dirección IP de la instancia de WindowsWorkstation en el cuadro de texto.
- Agregue /32 al final de la dirección IP. El texto completo debe ser similar al siguiente 123.12.123.23/32
- 
![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/47bf3814-084f-4213-a890-e137a0aa4db1)

### Tarea 5. Conectarse a la instancia de la base de datos
![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/688cfb4f-6b6d-4e99-b587-d52213bacb41)
![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/08a12f19-e820-4088-9fac-78bfb4c1dc61)

### Tarea 6. Explorar la estructura de la base de datos relacional
![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/e7a57fa8-8a6d-4772-90a5-d85077063f63)

