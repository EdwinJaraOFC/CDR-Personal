<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Repaso de computación en la Nube y servicios AWS<br>Temas: Base de datos en AWS</h1>
</p>

## Ejercicio 8: Introducción a Amazon Aurora
Explica qué es Amazon Aurora y cómo difiere de otros motores de base de datos compatibles con MySQL y PostgreSQL.

<p align="justify">Amazon Aurora es un servicio de base de datos relacional desarrollado por AWS que está diseñado para ser compatible con MySQL y PostgreSQL. Aurora combina la disponibilidad y el rendimiento de bases de datos comerciales de alto nivel con la simplicidad y el coste de bases de datos de código abierto.</p>

### Características de Amazon Aurora

| Característica  | Descripción  |
| :------------: | :------------: |
| Compatibilidad  | <p align="justify">Aurora es compatible con MySQL, lo que significa que las aplicaciones y herramientas que funcionan con MySQL también funcionarán con Aurora sin modificaciones significativas. También es compatible con PostgreSQL, permitiendo el uso de aplicaciones y herramientas diseñadas para PostgreSQL.</p>  |
| Rendimiento Mejorado  | <p align="justify">Aurora ofrece un rendimiento hasta cinco veces superior al de una base de datos MySQL estándar y hasta tres veces superior al de una base de datos PostgreSQL estándar. </p>  |
| Alta Disponibilidad y Durabilidad  | <p align="justify">Aurora almacena automáticamente múltiples copias de tus datos en tres Availability Zones (AZ) de AWS y puede tolerar fallos en hasta dos AZs sin pérdida de datos. Ofrece opciones de recuperación automática y copias de seguridad continuas en Amazon S3.</p>  |
| Escalabilidad  | <p align="justify">Aurora permite escalar la capacidad de lectura horizontalmente añadiendo hasta 15 réplicas de lectura de baja latencia. También permite escalar verticalmente el tamaño de la instancia de base de datos sin tiempo de inactividad.</p>  |
| Seguridad  | <p align="justify">Aurora incluye características de seguridad avanzadas, como cifrado de datos en reposo, en tránsito e integración con AWS Identity and Access Management (IAM)</p>  |
| Automatización y Gestión  | <p align="justify">Aurora se integra con otros servicios de AWS para proporcionar un entorno de gestión automatizado, que incluye actualizaciones automáticas de software, monitoreo y copias de seguridad.</p>  |
