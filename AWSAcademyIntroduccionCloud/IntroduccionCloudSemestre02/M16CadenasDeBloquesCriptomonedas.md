<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Módulo 16: Cadena de bloques y criptomonedas</h1>
</p>

## Terminología

| Término  | Concepto  |
| :------------: | :------------: |
| Cadena de bloques  | <p align="justify">Tecnología de base de datos descentralizada que mantiene un conjunto de transacciones en constante crecimiento protegido contra la manipulación y revisión mediante criptografía.</p>  |
| Criptomoneda  | <p align="justify">Tokens digitales que se implementan con tecnologías de cadena de bloques que comparten algunas de las cualidades de las monedas duras y se pueden comprar, intercambiar y gastar independientemente de una autoridad bancaria central.</p>  |
| Minería de criptomonedas (Criptominería)  | <p align="justify">Agregar transacciones al libro mayor de transacciones de la cadena de bloques existente distribuidas entre todos los usuarios de una cadena de bloques.</p>  |
| Base de datos descentralizada  | <p align="justify">Base de datos que no cuenta con una única ubicación, sino que las partes de la información se almacenan en diferentes ubicaciones que se encuentran conectadas entre sí.</p>  |
| Endurecimiento (datos o sistemas)  | <p align="justify">Hace referencia a reducir las vulnerabilidades en una tecnología. El objetivo es reducir el riesgo de seguridad.</p>  |
| Hash  | <p align="justify">Función matemática que se utiliza en la criptografía que toma una entrada de datos, como una lista de todas las transacciones, y devuelve una cadena nueva de una longitud fija.</p>  |
| Transacciones inmutables  | <p align="justify">Transacción que no se puede cambiar. Los datos de la cadena de bloques no se pueden modificar.</p>  |
| Contrato inteligente  | <p align="justify">Este cuenta con los términos del acuerdo escritos en el código. El código existe en una red de cadena de bloques. El código controla la ejecución del contrato. Las transacciones se pueden ratrear y no se pueden revertir. Los contratos inteligentes permiten transacciones entre partes anónimas sin necesidad de una autoridad central, un sistema legal o un mecanismo de aplicación externo.</p>  |

## Conceptos
### El desglose de la cadena de bloques
<p align="justify">Una cadena de bloques almacena transacciones en una cadena de datos conformada por bloques. Cada bloque tiene dos partes: la cabecera y el cuerpo. El cuerpo del bloque contiene todas las transacciones (es decir, los datos) asignadas al bloque. La cabecera del bloque contiene información como una marca de tiempo, el hash del bloque anterior, un hash de todas las transacciones contenidas en el cuerpo del bloque y el tamaño de hash que se requiere para el bloque nuevo.</p>

<p align="justify">Imagine la siguiente cadena de bloques: usted es médico. Tiene un paciente con una enfermedad crónica que lo visita anualmente para un procedimiento. Para cada procedimiento, tiene una carpeta separada (cuerpo del bloque) que contiene las notas, la medicación, la información de facturación y los resultados de laboratorio. El primer elemento de cada carpeta es una lista (cabecera del bloque) como una tabla de contenido, que incluye el número y la ubicación de la carpeta de cada procedimiento anterior. Cada lista tiene un código de barras (hash) que, cuando se escanea, verifica la autenticidad de esa carpeta.</p>

<p align="justify">Un hash criptográfico (denominado hash) es una función matemática que toma una entrada de datos, como una lista de todas las transacciones, y devuelve una salida de longitud fija. La salida puede parecer una colección aleatoria de letras y números, pero el resultado de la función hash tiene algunas características muy importantes:</p>

1. La función hash siempre producirá una cadena idéntica cuando se le proporcionen entradas idénticas. Un pequeño cambio en la entrada producirá un resultado muy diferente.
2. Es imposible descifrar un hash para obtener el mensaje original. Los mensajes se verifican con el hash al realizar la operación hash con el mensaje y comparar los resultados con el hash de verificación. Esta es la razón por la que se utiliza hash para proteger los datos.

<p align="justify">Dentro de una cadena de bloques, la cabecera de un bloque siempre contiene el hash de la cabecera del bloque anterior. De esta manera, cada bloque de la cadena de bloques es validado por el siguiente bloque de la secuencia.</p>

<p align="justify">Cada bloque de la cadena de bloques se encuentra protegido contra la manipulación o la revisión porque cambiar incluso un carácter en la entrada genera grandes cambios en el hash resultante. Si un atacante intentara cambiar los datos de un bloque, los valores hash de enlace en todos los bloques posteriores serían incorrectos. La estructura enlazada de la cadena de bloques es una de las formas en que se protegen contra modificaciones y manipulaciones. Sin embargo, el hashing no es la única forma en que se validan los bloques.</p>

<p align="justify">Las cadenas de bloques también utilizan sistemas de libro mayor distribuidos para garantizar que la cadena de bloques se encuentre protegida contra la manipulación. Los miembros de una red de cadena de bloques mantienen un registro de qué bloques son válidos. En el caso de que se cambie un bloque y haya dudas sobre la validez, se pueden comparar varias copias del libro mayor. En una red de cadena de bloques que utiliza un sistema de libro mayor distribuido, se lleva a cabo un voto mayoritario y todos los miembros emiten su voto en función de su propio registro de la cadena de bloques. Este método dificulta la modificación exitosa de un bloque en la cadena de bloques, incluso cuando no existe una autoridad central única que controle el libro mayor. Para hacerlo con éxito, el atacante tendría que cambiar el 51 % de los libros mayores de los miembros.</p>

### Ventajas de las cadenas de bloques
<p align="justify">La cadena de bloques tiene ventajas sobre otros tipos de datos almacenamiento porque es rápida y segura y no requiere una sola fuente de autoridad para validar las transacciones que contiene. Sus métodos de cifrado y validación hacen que sea mucho más difícil para los atacantes manipular o invalidar los datos. Esto permite que las cadenas de bloques reemplacen a la autoridad central que requieren muchos sistemas de transacciones empresariales.</p>

### ¿Qué son las criptomonedas?
<p align="justify">Las criptomonedas son monedas alternativas implementadas mediante el uso de cadenas de bloques. Bitcoin fue la primera criptomoneda. Las criptomonedas a menudo aparecen en las noticias porque han tenido un gran impacto en el público. Muchas personas confunden bitcoin (o criptomonedas en general) con cadenas de bloques. Es importante recordar que las criptomonedas son solo una aplicación posible de las cadenas de bloques.</p>

### ¿Qué es Bitcoin?
<p align="justify">Bitcoin es una criptomoneda creada en 2008. El software de código abierto de Bitcoin se lanzó en 2009 y rápidamente popularizó la idea de las cadenas de bloques.</p>

<p align="justify">Una característica importante de la red de Bitcoin es la minería. Los criptomineros son los que crean los nuevos bloques que se agregan a la cadena de bloques. Los criptomineros compiten con otros mineros a fin de resolver un complicado problema matemático para cada bloque nuevo, que se conoce como prueba de trabajo. El proceso se conoce como minería porque el creador de Bitcoin comparó a los mineros de las criptomonedas con los mineros del oro.</p>

<p align="justify">La minería de criptomonedas implica crear un hash que es menor o igual al tamaño de hash requerido en el último bloque en la cadena de bloques. Puede sonar simple, pero este proceso tiene un trampa. El nivel de dificultad para encontrar un hash aceptable aumenta a intervalos regulares. En el momento de escribir este artículo, el nivel de dificultad actual es de 12 900 000 000. Esto significa que la posibilidad de que una computadora procese un hash por debajo del objetivo especificado es de 1 en 12 900 000 000. Esto plantea la pregunta: ¿por qué los criptomineros gastarían el tiempo, la energía y la potencia informática en la minería? Los mineros son recompensados ​​por extraer con éxito un bloque con sus propios bitcoins.</p>

### Productos de cadena de bloques de AWS
<p align="justify">AWS proporciona tres productos de cadena de bloques para crear soluciones de cadenas de bloques basadas en la nube.</p>

#### 1. Amazon Quantum Ledger Database (Amazon QLDB)
<p align="justify">Una base de datos de libro mayor completamente administrada que proporciona un registro de transacciones transparente, inmutable y criptográficamente verificable propiedad de una autoridad central confiable. Amazon QLDB realiza un seguimiento de todos los cambios en los datos de aplicaciones y mantiene un historial completo y verificable de los cambios a lo largo del tiempo.</p>

#### 2. Amazon Managed Blockchain
<p align="justify">Un servicio completamente administrado que le permite configurar y administrar una red de cadena de bloques escalable con solo unos pocos clics mediante el uso de los populares marcos de código abierto Hyperledger Fabric y Ethereum. Managed Blockchain elimina la sobrecarga necesaria para crear la red y escala de forma automática a fin de satisfacer las demandas de miles de aplicaciones que ejecutan millones de transacciones. Managed Blockchain permite crear aplicaciones en las que varias partes pueden ejecutar transacciones sin necesidad de una autoridad central de confianza. Hoy, la creación de una red de cadena de bloques escalable con tecnologías existentes es difícil de configurar y administrar.</p>

#### 3. AWS Blockchain Templates
<p align="justify">Le permite implementar el marco de referencia de la cadena de bloques que elija como contenedores en un clúster de Amazon Elastic Container Service (Amazon ECS) o directamente en una instancia de Amazon Elastic Compute Cloud (Amazon EC2) que ejecuta Docker. Su red de cadena de bloques se crea en su propia Amazon Virtual Private Cloud (Amazon VPC), lo que le permite utilizar sus subredes de VPC y listas de control de acceso a la red. Puede asignar permisos granulares mediante AWS Identity and Access Management (IAM) para restringir a qué recursos puede acceder un clúster de Amazon ECS o una instancia EC2.</p>
