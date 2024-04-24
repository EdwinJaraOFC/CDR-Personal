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
El directorio en el que nos encontramos se llama directorio de trabajo. Para ver el nombre del directorio de trabajo, usamos el comando pwd.

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/c6183c61-4452-4973-ab68-9502270c9bd4">
</p>

Cuando iniciamos sesión por primera vez en nuestro sistema Linux, el directorio de trabajo se configura en nuestro directorio de inicio. Aquí es donde guardamos nuestros archivos.

#### cd
Para cambiar el directorio de trabajo (donde estamos parados en el laberinto) usamos el comando cd. Para hacer esto, escribimos cd seguido de la ruta del directorio de trabajo deseado.

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/583031f5-9e27-4c8a-b948-7e639572d063">
</p>

#### ls
Para enumerar los archivos en el directorio de trabajo, usamos el comando ls.

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/18a152f4-6b29-4f81-a449-1dd78e10dd12">
</p>

### Mirando alrededor
#### ls -l
Si usamos el -l opción con ls, obtendrá un archivo que enumera que contiene una gran cantidad de información sobre los archivos ser listado.

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/a37e64da-abb2-434d-a537-fd2f3849adb7">
</p>

### Manipulando archivos
#### mkdir
Se utiliza el comando para crear directorios.

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/1e613b19-cadf-43bf-a69d-2f4114bc2745">
</p>

#### rm
El comando elimina archivos y directorios.

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/07408ef4-8d7a-46e9-bd38-483b65aed659">
</p>

### Trabajando con comandos
#### help

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/f653b49b-a1a0-4d40-98f4-22e86fdb65b4">
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

### Expansión
Con la expansión, escribimos algo y se expande a otra cosa antes de que el caparazón actúe sobre ello. Para demostrar lo que queremos decir con esto, echemos un vistazo al comando echo.

#### echo
Imprime sus argumentos de texto en la salida estándar:

<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/c208bd3e-c570-4a15-ba18-70d529c1e4fb">
</p>
