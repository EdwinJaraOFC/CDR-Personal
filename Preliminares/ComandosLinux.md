<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Actividad: Línea de Comandos en Linux</h1>
</p>

<p align="justify">
Linux, como sistema operativo de tipo Unix, se utiliza ampliamente en servidores, supercomputadoras y sistemas distribuidos. La línea de comandos de Linux es una herramienta poderosa para la automatización de tareas repetitivas y la gestión eficiente de recursos del sistema. Es fundamental para interactuar con servicios en la nube y sistemas distribuidos, muchos de los cuales ofrecen interfaces basadas en CLI (Command Line Interface) para su gestión y configuración.
</p>

## LinuxCommand.org
### Qué es el Shell?
Es un programa que toma comandos del teclado y se los da al sistema operativo para que los ejecute. Era la única interfaz de usuario disponible en un sistema tipo Unix como Linux. Hoy en día, tenemos interfaces gráficas de usuario (GUI) además de interfaces de línea de comandos (CLI), como el shell.

### Qué es un terminal?
Es un programa que abre una ventana y te permite interactuar con el shell.

### Iniciando en la terminal
#### Probando el teclado

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/ed713ad5-c821-40e6-aab5-8458a9810080">
</p>

### Navegación
#### Organización del sistema de archivos
Al igual que Windows, los archivos en un sistema Linux están organizados en lo que se llama una estructura de directorios jerárquica. Esto significa que están organizados en un patrón de directorios en forma de árbol (llamados carpetas en otros sistemas), que pueden contener archivos y subdirectorios. El primer directorio del sistema de archivos se llama directorio raíz. El directorio raíz contiene archivos y subdirectorios, que contienen más archivos y subdirectorios, y así sucesivamente.

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/b3cb7e4c-b7ad-49bb-ae82-05a15584ff09">
</p>

Una diferencia importante entre Windows y los sistemas operativos tipo Unix, como Linux, es que Linux no emplea el concepto de letras de unidad. Mientras que las letras de las unidades de Windows dividen el sistema de archivos en una serie de árboles diferentes (uno para cada dispositivo), Linux siempre tiene un único árbol. Diferentes dispositivos de almacenamiento pueden ser diferentes ramas del árbol, pero siempre hay un solo árbol.

#### pwd
Ver el nombre del directorio de trabajo.

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/c6183c61-4452-4973-ab68-9502270c9bd4">
</p>

Cuando iniciamos sesión por primera vez en nuestro sistema Linux, el directorio de trabajo se configura en nuestro directorio de inicio. Aquí es donde guardamos nuestros archivos.

#### cd
Cambiar el directorio de trabajo.

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/38d657d6-62c0-43e9-bc9a-bd9c3dde2c0f">
</p>
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/07e549a4-451d-4da1-8ab6-35977785af1d">
</p>

### Mirando alrededor
#### ls
Lista los archivos en el directorio de trabajo.

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/d0db67be-8596-4eac-a2ff-f7e683bfab01">
</p>

#### ls /bin
Enumera los archivos en el directorio /bin (o cualquier otro directorio que deseemos especificar)
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/37f4f58c-eef8-4cde-85a8-f32950097e52">
</p>

#### ls -l
Enumera los archivos en el directorio de trabajo en formato largo

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/755f8247-5292-4629-9173-9d57b025c88e">
</p>

#### less
Permite visualizar archivos de texto.

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/c20e7025-ced3-4c2a-9414-d24ce3d596f0">
</p>
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/e95d7b44-54b2-4b2b-a4ed-4ae3cb450ab3">
</p>

#### file
Determina qué tipo de datos contiene un archivo.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/525ef421-bcf6-4317-a145-eb034cd8c219">
</p>

### Manipulando archivos
#### cp
Copia archivos y directorios. En su forma más simple, copia un único archivo.

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/bf3cceb7-4520-4493-9d95-c8c24aefb059">
</p>
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/ecac9ba0-6ea4-4a9c-9866-e65187ec8adc">
</p>

#### mv
Mueve o cambia el nombre de archivos y directorios según cómo se utilice.

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/dcd7f385-5c90-4a95-9579-1b66533e7e76">
</p>
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/010bd20c-1122-4972-8f2b-3c92e7aea3ca">
</p>

#### rm
Elimina archivos y directorios.

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/ce7401aa-4715-4131-90b0-1225bfb40bd9">
</p>

#### mkdir
Se utiliza el comando para crear directorios.

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/d4e98e5c-b074-4386-af03-2e7619516dc6">
</p>

### Trabajando con comandos
#### type
Muestra el tipo de comando que ejecutará el shell, dado un nombre de comando particular.

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/f2a5bb08-2688-4b98-a769-fdb803594a1c">
</p>

#### which
Determinar la ubicación exacta de un ejecutable determinado

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/e1914d9f-2078-44dd-aa48-bef8e7044d2d">
</p>

#### help
Función de ayuda incorporada

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/f653b49b-a1a0-4d40-98f4-22e86fdb65b4">
</p>

#### --help
Muestra una descripción de la sintaxis y las opciones admitidas del comando.

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/beabd71e-31f8-40fb-be03-f709b632742f">
</p>

#### man
Proporcionaa una documentación formal denominada manual o página de manual.

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/31cee8e1-747d-4beb-8d8c-de4b91d62c46">
</p>
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/a9f713d2-bc1f-4a84-8c31-f8798517e444">
</p>

### Redirección de Entrada/Salida
#### Salida Estándar
Para redirigir la salida estándar a un archivo, el carácter ">" se usa así:

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/c4150af6-7495-418d-a39d-d107e00ee11b">
</p>
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/158d1649-e14e-4469-a824-028cdf9a1027">
</p>

Tener los nuevos resultados adjunto al archivo en su lugar, usamos ">>" como este:

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/3ff43007-084d-43a9-b5c5-37f4cf86f0bd">
</p>
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/214d1b45-74e9-46da-a35d-43aa8f84ffc7">
</p>

#### Entrada Estándar
Para redirigir la entrada estándar desde un archivo en lugar del teclado, el personaje "<" se usa así:

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/7d5258f2-3eb5-438e-9220-931d8dec2ebd">
</p>
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/a9736a81-32c1-4e25-a533-336b84fb4f86">
</p>

Podríamos redirigir la salida estándar a otro archivo como este:

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/d7e304f6-fae8-4f7e-b6b8-481739c24fb3">
</p>
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/26cc638c-ef85-444b-9b9a-2a7e0818705a">
</p>

#### Pipelines
Con las pipelines, la salida estándar de un comando se introduce en la entrada estándar de otro.

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/aa3be459-f20d-4e00-adaf-7875472858f4">
</p>
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/45caa345-94ce-423d-add0-d2ce89c69ce9">
</p>

### Expansión
Con la expansión, escribimos algo y se expande a otra cosa antes de que el caparazón actúe sobre ello. Para demostrar lo que queremos decir con esto, echemos un vistazo al comando **echo:** Imprime sus argumentos de texto en la salida estándar.

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/c208bd3e-c570-4a15-ba18-70d529c1e4fb">
</p>
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/00caf455-2760-49fa-a5f6-5f684463f5a4">
</p>

#### Expansión de nombre de ruta
Mecanismo por el cual funcionan los comodines

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/2aec919b-5806-477a-9c69-62b318e0c77b">
</p>

#### Expansión de tilde
El carácter de tilde (“~”) tiene un significado especial, cuando se usa al principio de una palabra, se expande al nombre del directorio de inicio del usuario designado o, si no se nombra ningún usuario, al directorio de inicio del usuario actual.

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/d1683c9a-048b-4e28-8c91-d5706f89e57b">
</p>

#### Expansión aritmética
Permite realizar aritmética mediante expansión. Esto nos permite usar el símbolo del shell como calculadora. Tiene la forma "*$((expression))*".

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/d09cd407-adbf-4c4b-9f7d-22d7e5c6527e">
</p>

#### Expansión de llaves
Podemos crear múltiples cadenas de texto a partir de un patrón que contenga llaves.

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/ce253c07-d8f9-4acb-9a4e-d14e221bbddb">
</p>

Los patrones que se van a expandir entre llaves pueden contener una parte inicial llamada preámbulo y una parte final llamada posdata. La expresión de llave en sí puede contener una lista de cadenas separadas por comas o un rango de números enteros o caracteres individuales. Es posible que el patrón no contenga espacios en blanco incrustados.

#### Expansión de parámetros
Es una característica que es más útil en scripts de shell que directamente en la línea de comando. Muchas de sus capacidades tienen que ver con la capacidad del sistema para almacenar pequeños fragmentos de datos y darle un nombre a cada fragmento.

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/5655ace3-20f5-48c0-bba4-e2d3dfb65f84">
</p>

#### Sustitución de comando
Nos permite utilizar la salida de un comando como una expansión

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/be992420-6115-4861-a8ac-87827cdefd24">
</p>

#### Quoting
El shell proporciona un mecanismo llamado *quoting* para suprimir selectivamente expansiones no deseadas.

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/f048299e-4275-4733-be28-5a5fd34ed358">
</p>

#### Doble comillas
Si colocamos texto entre comillas dobles, todos los caracteres especiales utilizados por el shell pierden su significado especial y se tratan como caracteres comunes. Las excepciones son “$”, “\” (barra invertida) y “`” (comillas invertidas). Esto significa que se suprimen la división de palabras, la expansión de nombres de rutas, la expansión de tildes y la expansión de llaves, pero aún se llevan a cabo la expansión de parámetros, la expansión aritmética y la sustitución de comandos.

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/3a3ee5f0-086f-4fc5-a523-55dd7be52cad">
</p>

#### Comillas simples
Cuando necesitamos suprimir todas las expansiones, utilizamos comillas simples.

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/e9567e6d-180a-4c89-bff6-83e896f989a4">
</p>

#### Caracteres que escapan
A veces sólo queremos citar un solo carácter. Para hacer esto, podemos anteponer un carácter con una barra invertida, que en este contexto se llama carácter de escape. A menudo esto se hace entre comillas dobles para evitar selectivamente una expansión.

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/59feaa8a-89fa-420a-8410-82decbacae0a">
</p>

### Permisos
#### Permisos de archivos
En un sistema Linux, a cada archivo y directorio se le asignan derechos de acceso para el propietario del archivo, los miembros de un grupo de usuarios relacionados y todos los demás. Se pueden asignar derechos para leer un archivo, escribir un archivo y ejecutar un archivo (es decir, ejecutar el archivo como un programa).

Para ver la configuración de permisos de un archivo, podemos usar el comando ls.

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/e176f546-ecc1-4b1c-851c-101c7818ea15">
</p>

### Control de Trabajo
#### Poner un programa en segundo plano
Para hacernos la vida un poco más fácil, vamos a iniciar nuevamente el programa xload, pero esta vez lo pondremos en segundo plano para que vuelva a aparecer el mensaje. Para ello ejecutamos xload así:

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/f8743b16-15f4-45f8-b4fd-59256fbdaa17">
</p>

En este caso, el mensaje volvió porque el proceso se puso en segundo plano.

Ahora imagina que nos olvidamos de usar el símbolo "&" para poner el programa en segundo plano. Aún hay esperanza. Podemos escribir Ctrl-z y el proceso quedará suspendido. Esto lo podemos comprobar viendo que la ventana del programa está congelada. El proceso todavía existe, pero está inactivo. Para reanudar el proceso en segundo plano, escriba el comando bg (abreviatura de fondo). Aquí hay un ejemplo:

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/a10ec6f4-2a05-42e2-bb7d-4511059bef08">
</p>

#### Listado de procesos en ejecución
Ahora que tenemos un proceso en segundo plano, sería útil mostrar una lista de los procesos que hemos iniciado. Para hacer esto, podemos usar el comando jobs o el comando ps más poderoso.

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/18cda6b3-ca18-4470-849f-27f605fabf48">
</p>

#### Matar un proceso
Supongamos que tenemos un programa que deja de responder; ¿Cómo nos deshacemos de él? Usamos el comando matar, por supuesto. Probemos esto en xload. Primero, necesitamos identificar el proceso que queremos eliminar. Podemos usar jobs o ps para hacer esto. Si usamos trabajos, obtendremos un número de trabajo. Con ps, se nos proporciona una identificación de proceso (PID). Lo haremos de ambas maneras:

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/f502322e-1a43-4d4a-9b0b-c7e5aebe1c57">
</p>
