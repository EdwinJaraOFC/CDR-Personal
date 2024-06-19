<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Repaso de computación en la Nube y servicios AWS<br>Temas: Base de datos en AWS</h1>
</p>

## Ejercicio 7: Escalabilidad horizontal con réplicas de lectura
- Describe cómo se configuran y utilizan las réplicas de lectura en Amazon RDS.
- Proporciona un ejemplo de un caso de uso en el que las réplicas de lectura mejorarían significativamente el rendimiento

### Amazon Relational Database Service (Amazon RDS)
- Bases de datos relacionales
- RDBMS: Sistema de gestión de bases de datos relacionales, ejemplo: Mysql, postgreSQL, MariaDB, Oracle, Amazon Aurora
- CRUD: crear, leer, actualizar, eliminar 
- Solo se puede implementar una única instancia maestra de base de datos → operaciones de lectura y escritura

#### Amazon ofrece Multi-AZ
Implementa una copia principal (maestra) de tu base de datos en una zona de disponibilidad y una copia secundaria (en espera) se implementa en otra zona de disponibilidad
			Replicación síncrona
Copia maestra -----------------------------------------------------> Copia en espera

#### Conmutación por error
Copia maestra (X) —->    Copia en espera => Copia maestra

### Réplicas de lectura
- Se replican desde la base de datos de origen
- Facilitan el escalamiento horizontal 
- Redirigir consultas de solo lectura de datos

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/ec61a7e9-da16-42fe-9237-06ad996b9955" width="500">
</p>

#### Caso de uso → mejora de rendimiento
Podemos redirigir las consultas de lectura a nuestras réplicas de lectura y nuestra copia maestra se puede concentrar en las consultas de escritura


## Ejercicio 8: Introducción a Amazon Aurora
**Pregunta 1:** Explica qué es Amazon Aurora y cómo difiere de otros motores de base de datos compatibles con MySQL y PostgreSQL.

<p align="justify">Amazon Aurora es un servicio de base de datos relacional desarrollado por AWS que está diseñado para ser compatible con MySQL y PostgreSQL. Aurora combina la disponibilidad y el rendimiento de bases de datos comerciales de alto nivel con la simplicidad y el coste de bases de datos de código abierto.</p>

### Características de Amazon Aurora

| Característica  | Descripción  |
| :------------: | :------------: |
| Compatibilidad  | <p align="justify">Compatible con MySQL y PostgreSQL.</p>  |
| Rendimiento Mejorado  | <p align="justify">Aurora ofrece un rendimiento hasta cinco veces superior que MySQL estándar y hasta tres veces superior que PostgreSQL estándar por una décima parte del costo.</p>  |
| Alta Disponibilidad y Durabilidad  | <p align="justify">Almacena automáticamente múltiples copias de tus datos en tres zonas de disponibilildad (AZ) de AWS y puede tolerar fallos en hasta dos AZs sin pérdida de datos.</p>  |
| Escalabilidad  | <p align="justify">Permite escalar la capacidad de lectura horizontalmente añadiendo hasta 15 réplicas de lectura de baja latencia. También permite escalar verticalmente el tamaño de la instancia de base de datos sin tiempo de inactividad.</p>  |
| Seguridad  | <p align="justify">Incluye características de seguridad avanzadas, como cifrado de datos en reposo, en tránsito e integración con AWS Identity and Access Management (IAM)</p>  |
| Automatización y Gestión  | <p align="justify">Aurora se integra con otros servicios de AWS para proporcionar un entorno de gestión automatizado, que incluye actualizaciones automáticas de software, monitoreo y copias de seguridad.</p>  |

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/2850d782-80b1-400c-8088-5d401b4bffcf" width="900">
</p>

**Pregunta 2:** Discute las características que hacen a Amazon Aurora una opción preferida para aplicaciones de alta disponibilidad y rendimiento.

### Diferencias con Otros Motores de Base de Datos Compatibles con MySQL y PostgreSQL y ventajas de Amazon Aurora sobre estas

| Característica  | Amazon Aurora  | MySQL/PostgreSQL en RDS estándar  |
| :------------: | :------------: | :------------: |
| Arquitectura de Almacenamiento  | <p align="justify">Almacenamiento SSD distribuido y replicado en múltiples AZs.</p>  | <p align="justify">Replicación a nivel de base de datos o almacenamiento.</p>  |
| Rendimiento y Latencia  | <p align="justify">Replicación de datos optimizada y gestión de buffer caché que mejora rendimiento y reduce latencia.</p>  | <p align="justify">Mayores latencias y menor rendimiento debido a una arquitectura de almacenamiento y replicación más tradicionales.</p>  |
| Escalabilidad de Lectura  | <p align="justify">Añadir réplicas de lectura con latencia muy baja y carga balanceada automáticamente entre las réplicas.</p>  | <p align="justify">Configuración de réplicas de lectura más compleja y menos eficiente.</p>  |
| Resiliencia y Recuperación  | <p align="justify">Recuperación en segundos y múltiples copias de los datos asegurando alta durabilidad.</p>  | <p align="justify">Recuperación más lenta y menor durabilidad sin configuraciones adicionales.</p>  |
| Coste y Eficiencia  | <p align="justify">Más coste-efectivo a largo plazo debido a alta eficiencia y menor necesidad de gestión manual.</p>  | <p align="justify">Mayores costes de operación y mantenimiento, especialmente en configuraciones de alta disponibilidad.</p>  |
