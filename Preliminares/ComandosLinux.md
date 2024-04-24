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

<p align= "center">
  <img src="">
</p>

#### Sustitución de comando

<p align= "center">
  <img src="">
</p>

#### Quoting

<p align= "center">
  <img src="">
</p>

#### Doble comillas

<p align= "center">
  <img src="">
</p>

#### Comillas simples

<p align= "center">
  <img src="">
</p>

#### Caracteres que escapan

<p align= "center">
  <img src="">
</p>

#### Más trucos de barra invertida

<p align= "center">
  <img src="">
</p>

### Permisos
#### Permisos de archivos

<p align= "center">
  <img src="">
</p>

#### chmod

<p align= "center">
  <img src="">
</p>

#### Permisos de directorio

<p align= "center">
  <img src="">
</p>

#### Convertirse en el superusuario por un corto tiempo

<p align= "center">
  <img src="">
</p>

#### Cambiar la propiedad del archivo

<p align= "center">
  <img src="">
</p>

#### Cambiar la propiedad del grupo

<p align= "center">
  <img src="">
</p>

### Control de Trabajo

<p align= "center">
  <img src="">
</p>

#### Un ejemplo práctico

<p align= "center">
  <img src="">
</p>

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
