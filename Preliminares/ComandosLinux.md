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
  <img src="">
</p>

#### which
Determinar la ubicación exacta de un ejecutable determinado

<p align= "center">
  <img src="">
</p>

#### help
Función de ayuda incorporada

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/f653b49b-a1a0-4d40-98f4-22e86fdb65b4">
</p>

#### --help
Muestra una descripción de la sintaxis y las opciones admitidas del comando.

<p align= "center">
  <img src="">
</p>

#### man
Proporcionaa una documentación formal denominada manual o página de manual.

<p align= "center">
  <img src="">
</p>

### Redirección de Entrada/Salida
#### Salida Estándar
Para redirigir la salida estándar a un archivo, el carácter ">" se usa así:

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/c4150af6-7495-418d-a39d-d107e00ee11b">
</p>

Tener los nuevos resultados adjunto al archivo en su lugar, usamos ">>" como este:

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/3ff43007-084d-43a9-b5c5-37f4cf86f0bd">
</p>

#### Entrada Estándar
Para redirigir la entrada estándar desde un archivo en lugar del teclado, el personaje "<" se usa así:

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/7d5258f2-3eb5-438e-9220-931d8dec2ebd">
</p>

Podríamos redirigir la salida estándar a otro archivo como este:

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/d7e304f6-fae8-4f7e-b6b8-481739c24fb3">
</p>

#### Pipelines
Con las pipelines, la salida estándar de un comando se introduce en la entrada estándar de otro.

<p align= "center">
  <img src="">
</p>

### Expansión
Con la expansión, escribimos algo y se expande a otra cosa antes de que el caparazón actúe sobre ello. Para demostrar lo que queremos decir con esto, echemos un vistazo al comando **echo:** Imprime sus argumentos de texto en la salida estándar.

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/c208bd3e-c570-4a15-ba18-70d529c1e4fb">
</p>

#### Expansión de nombre de ruta
Mecanismo por el cual funcionan los comodines

<p align= "center">
  <img src="">
</p>

#### Expansión de tilde
El carácter de tilde (“~”) tiene un significado especial, cuando se usa al principio de una palabra, se expande al nombre del directorio de inicio del usuario designado o, si no se nombra ningún usuario, al directorio de inicio del usuario actual.

<p align= "center">
  <img src="">
</p>

#### Expansión aritmética
Permite realizar aritmética mediante expansión. Esto nos permite usar el símbolo del shell como calculadora. Tiene la forma "*$((expression))*".

<p align= "center">
  <img src="">
</p>

#### Expansión de llaves
Podemos crear múltiples cadenas de texto a partir de un patrón que contenga llaves.

<p align= "center">
  <img src="">
</p>

Los patrones que se van a expandir entre llaves pueden contener una parte inicial llamada preámbulo y una parte final llamada posdata. La expresión de llave en sí puede contener una lista de cadenas separadas por comas o un rango de números enteros o caracteres individuales. Es posible que el patrón no contenga espacios en blanco incrustados.

<p align= "center">
  <img src="">
</p>

#### Expansión de parámetros
Es una característica que es más útil en scripts de shell que directamente en la línea de comando. Muchas de sus capacidades tienen que ver con la capacidad del sistema para almacenar pequeños fragmentos de datos y darle un nombre a cada fragmento.

<p align= "center">
  <img src="">
</p>

#### Sustitución de comando
Nos permite utilizar la salida de un comando como una expansión

<p align= "center">
  <img src="">
</p>

#### Quoting
El shell proporciona un mecanismo llamado *quoting* para suprimir selectivamente expansiones no deseadas.

<p align= "center">
  <img src="">
</p>

#### Doble comillas
Si colocamos texto entre comillas dobles, todos los caracteres especiales utilizados por el shell pierden su significado especial y se tratan como caracteres comunes. Las excepciones son “$”, “\” (barra invertida) y “`” (comillas invertidas). Esto significa que se suprimen la división de palabras, la expansión de nombres de rutas, la expansión de tildes y la expansión de llaves, pero aún se llevan a cabo la expansión de parámetros, la expansión aritmética y la sustitución de comandos.

<p align= "center">
  <img src="">
</p>

#### Comillas simples
Cuando necesitamos suprimir todas las expansiones, utilizamos comillas simples.

<p align= "center">
  <img src="">
</p>

#### Caracteres que escapan
A veces sólo queremos citar un solo carácter. Para hacer esto, podemos anteponer un carácter con una barra invertida, que en este contexto se llama carácter de escape. A menudo esto se hace entre comillas dobles para evitar selectivamente una expansión.

<p align= "center">
  <img src="">
</p>

### Permisos
#### Permisos de archivos
En un sistema Linux, a cada archivo y directorio se le asignan derechos de acceso para el propietario del archivo, los miembros de un grupo de usuarios relacionados y todos los demás. Se pueden asignar derechos para leer un archivo, escribir un archivo y ejecutar un archivo (es decir, ejecutar el archivo como un programa).

Para ver la configuración de permisos de un archivo, podemos usar el comando ls.

<p align= "center">
  <img src="">
</p>

#### chmod
Se utiliza para cambiar los permisos de un archivo o directorio. Para usarlo especificamos la configuración de permisos deseada y el archivo o archivos que deseamos modificar. Hay dos formas de especificar los permisos. Nos centraremos en uno de ellos, llamado método de notación octal.

<p align= "center">
  <img src="">
</p>

#### Convertirse en el superusuario por un corto tiempo
A menudo es necesario convertirse en superusuario para realizar importantes tareas de administración del sistema, pero como sabemos, no debemos permanecer conectados como superusuario. En la mayoría de las distribuciones, existe un programa que puede brindarle acceso temporal a los privilegios de superusuario. Este programa se llama su (abreviatura de usuario sustituto) y puede usarse en aquellos casos en los que necesitas ser superusuario para una pequeña cantidad de tareas. Para convertirse en superusuario, simplemente escriba el comando su. Se le solicitará la contraseña de superusuario.

<p align= "center">
  <img src="">
</p>

En la mayoría de las distribuciones modernas, se utiliza un método alternativo. En lugar de utilizar su, estos sistemas emplean el comando sudo. Con sudo, a uno o más usuarios se les otorgan privilegios de superusuario según sea necesario. Para ejecutar un comando como superusuario, el comando deseado simplemente va precedido del comando sudo. Después de ingresar el comando, se le solicita al usuario su propia contraseña en lugar de la del superusuario.

<p align= "center">
  <img src="">
</p>

De hecho, las distribuciones modernas ni siquiera establecen la contraseña de la cuenta raíz, lo que hace imposible iniciar sesión como usuario raíz. Todavía es posible un shell raíz con sudo usando la opción "-i"

<p align= "center">
  <img src="">
</p>

#### Cambiar la propiedad del archivo
Podemos cambiar el propietario de un archivo usando el comando chown.

<p align= "center">
  <img src="">
</p>

Tenga en cuenta que para cambiar el propietario de un archivo, debemos tener privilegios de superusuario. Para hacer esto, nuestro ejemplo empleó el comando sudo para ejecutar chown. chown funciona de la misma manera en directorios que en archivos.

#### Cambiar la propiedad del grupo
La propiedad del grupo de un archivo o directorio se puede cambiar con chgrp.

<p align= "center">
  <img src="">
</p>

### Control de Trabajo
#### Poner un programa en segundo plano

<p align= "center">
  <img src="">
</p>

#### Listado de procesos en ejecución

<p align= "center">
  <img src="">
</p>

#### Matar un proceso

<p align= "center">
  <img src="">
</p>

#### Un poco más sobre "matar"

<p align= "center">
  <img src="">
</p>
