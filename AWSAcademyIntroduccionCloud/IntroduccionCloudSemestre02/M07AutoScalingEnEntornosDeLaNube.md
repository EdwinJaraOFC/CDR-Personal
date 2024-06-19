<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Módulo 7: Auto Scaling en entornos de la nube</h1>
</p>

## Terminología

| Término  | Concepto  |
| :------------: | :------------: |
| Escalado automático  | <p align="justify">Monitorean sus aplicaciones y ajustan de forma automática la capacidad de mantener un rendimiento estable y predecible al menor costo posible. El término escalado significa que se pueden crear instancias nuevas según sea necesario, en función del tráfico de red o se pueden aumentar instancias existentes con almacenamiento adicional o potencia. El último tipo de escala se denomina escalado vertical.</p>  |
| Flota  | <p align="justify">Una sola instancia o un grupo de instancias.</p>  |
| Plantilla de lanzamiento  | <p align="justify">Especifica la información de configuración de la instancia.</p>  |
| Escalar horizontalmente  | <p align="justify">Agregue instancias de Amazon EC2 según sea necesario, para responder a la demanda.</p>  |
| Reducir horizontalmente  | <p align="justify">Elimine las instancias de Amazon EC2 cuando haya una reducción en la demanda.</p>  |

## Conceptos

<p align="justify">
El escalado dinámico y el escalado predictivo se pueden usar juntos para escalar con más rapidez.</p>

- Amazon EC2 Auto Scaling puede detectar cuando una instancia está en mal estado, terminarla y reemplazarla con una nueva.
- Amazon EC2 Auto Scaling ayuda a garantizar que su aplicación siempre tenga la cantidad correcta de potencia de cómputo y aprovisione la capacidad de forma proactiva con escalado predictivo.
- Amazon EC2 Auto Scaling agrega instancias solo cuando es necesario y puede escalar a través de opciones de compra para optimizar el rendimiento y el costo.

Amazon EC2 Auto Scaling realizará tres funciones principales a fin de automatizar la administración de flota para instancias EC2:
- Monitorea el estado de instancias en ejecución.
- Reemplaza de forma automática instancias deterioradas.
- Equilibra la capacidad entre las zonas de disponibilidad.

### Escalado programado
<p align="justify">Cuando el escalado se basa en la programación, los usuarios pueden escalar su aplicación con anticipación de los cambios de carga conocidos. Por ejemplo, cada semana, el tráfico de la aplicación web comienza a aumentar los miércoles, permanece alto el jueves y disminuye el viernes. Los usuarios pueden planificar sus actividades de escalado en función de los patrones conocidos de tráfico de la aplicación web.</p>

### Escalado dinámico
<p align="justify">Con Amazon EC2 Auto Scaling, los usuarios pueden seguir de cerca la curva de demanda para sus aplicaciones, lo que reduce la necesidad de aprovisionar de forma manual la capacidad de Amazon EC2 con anticipación. Un ejemplo de cuándo sería útil un escalado dinámico es cuando una canción o un video se vuelven virales. El escalado dinámico detectaría el aumento de tráfico y sincronizaría instancias nuevas para seguir el ritmo del aumento de demanda.</p>

### Escalado predictivo
<p align="justify">El escalado predictivo de Amazon EC2 Auto Scaling utiliza machine learning para anticipar y programar el número adecuado de instancias EC2 antes de cambios de tráfico. Predice el tráfico futuro, incluidos picos regulares, y ajusta automáticamente sus pronósticos basándose en patrones diarios y semanales. Esto simplifica la configuración de Auto Scaling al eliminar la necesidad de ajustes manuales, proporcionando un aprovisionamiento de capacidad más rápido, preciso y económico, resultando en aplicaciones más receptivas.</p>

### Características de AWS Auto Scaling
- Descubrimiento automático de recursos
- Estrategias de escalado integradas
- Políticas de escalado inteligente

### Plantillas de lanzamiento
<p align="justify">Una plantilla de lanzamiento, al igual que una configuración de lanzamiento, especifica la configuración de una instancia EC2, incluyendo el ID de AMI, tipo de instancia, par de claves, grupos de seguridad, entre otros parámetros. La diferencia principal es que una plantilla de lanzamiento permite tener diferentes versiones, facilitando la reutilización de un subconjunto de parámetros para crear nuevas plantillas o versiones. Por ejemplo, se puede crear una plantilla predeterminada con parámetros comunes y definir el resto en versiones posteriores de la misma plantilla.</p>
