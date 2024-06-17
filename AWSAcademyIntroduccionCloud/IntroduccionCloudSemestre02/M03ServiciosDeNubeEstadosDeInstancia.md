<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Módulo 3: Servicios de nube y estados de instancia</h1>
</p>

## Terminología

| Término  | Concepto  |
| :------------: | :------------: |
| Amazon Elastic Compute Cloud (Amazon EC2)  | <p align="justify">Servicio que proporciona capacidad de cómputo de tamaño modificable y segura en la nube.</p>  |
| Instancia EC2  | <p align="justify">Servidor virtual en EC2 para ejecutar aplicaciones en la infraestructura AWS.</p>  |
| Amazon Elastic Block Store (Amazon EBS)  | <p align="justify">Almacenamiento para instancias EC2.</p>  |
| Volúmenes de almacén de instancias  | <p align="justify">Almacenamiento temporal que no es persistente a través de detenciones de instancias, terminaciones o fallas de hardware.</p>  |
| Amazon Machine Image (AMI)  | <p align="justify">Tipo especial de dispositivo virtual que se utiliza para crear una VM en EC2.</p>  |
| Dirección IPv4  | <p align="justify">Número de 32 bits que identifica una interfaz de red en un equipo de forma única, por lo general se escribe en dígitos decimales y se le otorga el formato de 4 campos de 8 bits separados por puntos.</p>  |
| Dirección IPv6  | <p align="justify">Cadena alfanumerica de 128 bits que identifica un dispositivo en el esquema de direccionamiento para IPv6.</p>  |
| Dirección IP elástica  | <p align="justify">Dirección IPv4 estática diseñada para la informática en la nube que se encuentra asociada con su cuenta AWS. La dirección IP elástica permanece en su lugar a través de eventos que normalmente hacen que la dirección cambie, como detener o reinicar la instancia.</p>  |

## Conceptos
<p align="justify">
Uno de los principales beneficios de la tecnología en la nube es la capacidad de pagar solo por lo que necesita y por las cosas a medida que las usa. Para que esto sea posible, el costo de las máquinas virtuales en AWS se divide en los estados por los que pasan las instancias durante su vida útil. Cuando lanza una instancia en la nube, un servidor pasa por varios estados.</p>

<p align="justify">
Cuando lanza una instancia, adopta el estado Pendiente. Esto significa que AWS está preparando la instancia y usted aún no puede acceder a ella. Una vez que puede acceder a ella, adopta el estado En ejecución. Puede conectarse a la instancia en ejecución y usarla de la misma manera que usaría una computadora.</p>

<p align="justify">
Tan pronto como la instancia pasa al estado En ejecución, se le factura por cada segundo (con un mínimo de 1 minuto) que mantiene la instancia en ejecución, aun cuando esta permanece inactiva y no se conecta a ella.</p>

<p align="justify">
Cuando ya no la necesita, puede detenerla o terminarla. Tan pronto como el estado de la instancia cambia a Terminando instancia o Terminado, deja de incurrir en cargos por esa instancia. Puede detener o hibernar una instancia y reiniciarla más adelante. Sin embargo, es posible que al hacerlo se pierdan algunos datos temporales. A continuación, encontrará una tabla que muestra los efectos de detener y reiniciar una instancia.</p>
