<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Módulo 8: Seguridad II</h1>
</p>

## Finalidad del módulo
Continuar desarrollando la comprensión de la seguridad en la nube. El módulo cubre las diferencias entre AWS Shield y AWS WAF. Aprenderemos qué es un ataque de denegación de servicio distribuido (DDoS). También obtendremos información sobre Amazon Inspector y AWS Artifact.

## Terminología
| Término  | Concepto  |
| :------------: | :------------: |
| AWS Shield  | <p align="justify">Servicio de protección contra DDoS administrado que protege las aplicaciones que se ejecutan en AWS.</p>  |
| AWS WAF  | <p align="justify">Servicio que le da control sobre qué tráfico permitir o bloquear en sus aplicaciones web mediante la definición de reglas de seguridad web personalizables.</p>  |
| Denegación de servicio distribuido  | <p align="justify">Intento malicioso de hacer que un sistema dirigido, como un sitio web o una aplicación, no esté disponible para los usuarios finales. Para lograrlo, los atacantes utilizan una variedad de técnicas que consumen recursos de red o de otros tipos, lo que interrumpe el acceso de los usuarios finales legítimos.</p>  |
| Amazon Inspector  | <p align="justify">Un servicio de evaluación de seguridad automatizada. Le ayuda a probar la accesibilidad a la red de sus instancias de Amazon EC2 y el estado de seguridad de las aplicaciones que se ejecutan en las instancias.</p>  |
| AWS Artifact  | <p align="justify">Un recurso crucial para la información relacionada con la conformidad. Proporciona acceso bajo demanda a los informes de seguridad y conformidad de AWS y a determinados acuerdos en línea.</p>  |

## Antecedentes

Se deben abordar cuatro áreas de seguridad para la informática en la nube:

- Datos: protección de la información almacenada y procesada en la nube
- Permisos: regulación de quién tiene acceso a los recursos y datos en la nube
- Infraestructura: protección de las máquinas y el hardware que ejecutan, almacenan y procesan datos en la nube
- Evaluación: inspección de la infraestructura, los permisos y los datos para asegurarnos de que están seguros

<p align="justify">
Shield y AWS WAF son servicios que abordan los ataques a la infraestructura, principalmente la red utilizada para acceder a los recursos de la nube.<br>
Amazon Inspector aborda la evaluación investigando qué tan bien se protegen los recursos en la nube que utilizamos, como nuestras instancias EC2. También investiga si estos recursos siguen las pautas de prácticas recomendadas.</p>
<p align="justify">
La naturaleza de la nube la hace susceptible a los ciberataques que pueden hacer que los sitios web, las aplicaciones y los procesos dejen de funcionar. Cuando una empresa de miles de millones de dólares como Amazon confía en la nube, la empresa necesita saber que está protegida contra los ataques.</p>
<p align="justify">
Uno de los principales tipos de ciberataque se denomina DDoS. Los DDoS se producen cuando los atacantes configuran programas que envían miles o millones de solicitudes a una aplicación, sitio web o servicio al mismo tiempo. Este pico en el tráfico puede consumir recursos hasta el punto en que el sitio web o la aplicación ya no están accesibles para los usuarios legítimos.</p>
<p align="justify">
Los ataques DDoS pueden llevarse a cabo por muchas razones, como motivos de competencia, políticos o económicos. Sea cual sea el motivo, AWS cuenta con servicios que minimizan estas amenazas para los usuarios de la nube.</p>

Shield trabaja junto con Elastic Load Balancing, Amazon CloudFront y Amazon Route 53 para protegerlo contra ataques DDoS. Hay dos niveles de servicio:

- AWS Shield Standard está disponible para todos los usuarios de AWS sin costo adicional. Protege a los usuarios de los ataques DDoS más comunes. Esta protección se aplica de forma automática y transparente a cualquier recurso de ELB, distribuciones de CloudFront y recursos de Route 53.
- AWS Shield Advanced proporciona una capacidad adicional de mitigación de DDoS para ataques volumétricos, detección inteligente de ataques y mitigación de ataques en las capas de la aplicación y la red. Los usuarios tienen acceso las 24 horas del día, los 7 días de la semana al equipo de respuesta DDoS (DRT) para una mitigación personalizada durante los ataques. Los usuarios también obtienen métricas e informes avanzados en tiempo real y protección de costos por DDoS para protegerse contra los picos en las facturas tras un ataque DDoS. Shield Advanced está disponible por un costo adicional.

<p align="justify">
AWS WAF es otra herramienta de defensa proporcionada por AWS. Ayuda a proteger las aplicaciones web de vulnerabilidades que pueden afectar la disponibilidad o la seguridad, o consumir recursos. AWS WAF puede monitorear el tráfico web de una aplicación y decidir qué tráfico dejar pasar en función de la solicitud específica que se está realizando. Los usuarios de AWS pueden crear su propio conjunto de reglas para dirigir el tráfico permitido por AWS WAF hacia direcciones IP específicas.</p>

<p align="justify">
Amazon Inspector no protege activamente sus servicios de AWS. En su lugar, monitorea los servicios y le proporciona actualizaciones sobre cualquier vulnerabilidad o cualquier lugar en el que no siga las prácticas recomendadas. Esto puede resultar útil para los expertos para asegurarse de que cumplen los estándares de conformidad de seguridad y para los nuevos usuarios que puedan conocer las prácticas recomendadas.</p>

<p align="justify">
Amazon Inspector funciona ejecutando una evaluación en sus instancias EC2; la evaluación comprueba varias prácticas recomendadas predeterminadas. Tras realizar una evaluación, Amazon Inspector elabora una lista detallada de los resultados de seguridad priorizados por nivel de severidad. Estos hallazgos se pueden revisar directamente o como parte de informes de evaluación detallados disponibles a través de la consola o API de Amazon Inspector.</p>

<p align="justify">
Las evaluaciones de seguridad de Amazon Inspector le ayudan a verificar si hay accesibilidad a la red no deseada de sus instancias EC2 y de vulnerabilidades en esas instancias EC2. Las evaluaciones de Amazon Inspector se ofrecen como paquetes de reglas predefinidas asignados a prácticas recomendadas de seguridad y definiciones de vulnerabilidades comunes. Algunos ejemplos de reglas integradas incluyen la comprobación del acceso a las instancias EC2 desde Internet, la activación del inicio de sesión remoto en el usuario raíz o las versiones de software vulnerables instaladas. Los investigadores de seguridad de AWS actualizan periódicamente estas reglas.</p>

<p align="justify">
AWS Artifact es un recurso centralizado para información relacionada con la conformidad. Las distintas organizaciones exigen que los proveedores de servicios en la nube (CSP) cumplan con muchas certificaciones y reglas diferentes para alojar sus datos o solicitudes de proceso. Las organizaciones que manejan información confidencial, como información bancaria, información personal o registros médicos deben asegurarse de que su servicio en la nube cumple con ciertos estándares de seguridad. AWS Artifact enumera y proporciona detalles sobre los diferentes estándares de conformidad que cumplen.
</p>
