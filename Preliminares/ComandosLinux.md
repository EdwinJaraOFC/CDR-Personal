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

![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/d8f9f7e1-720d-400a-a7f7-c72671315ee4)

### Navegación
#### Organización del sistema de archivos
Al igual que Windows, los archivos en un sistema Linux están organizados en lo que se llama una estructura de directorios jerárquica. Esto significa que están organizados en un patrón de directorios en forma de árbol (llamados carpetas en otros sistemas), que pueden contener archivos y subdirectorios. El primer directorio del sistema de archivos se llama directorio raíz. El directorio raíz contiene archivos y subdirectorios, que contienen más archivos y subdirectorios, y así sucesivamente.

![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/b3cb7e4c-b7ad-49bb-ae82-05a15584ff09)

Una diferencia importante entre Windows y los sistemas operativos tipo Unix, como Linux, es que Linux no emplea el concepto de letras de unidad. Mientras que las letras de las unidades de Windows dividen el sistema de archivos en una serie de árboles diferentes (uno para cada dispositivo), Linux siempre tiene un único árbol. Diferentes dispositivos de almacenamiento pueden ser diferentes ramas del árbol, pero siempre hay un solo árbol.

#### pwd
El directorio en el que nos encontramos se llama directorio de trabajo. Para ver el nombre del directorio de trabajo, usamos el comando pwd.

![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/8144620e-4374-455a-8770-719659c796fc)

Cuando iniciamos sesión por primera vez en nuestro sistema Linux, el directorio de trabajo se configura en nuestro directorio de inicio. Aquí es donde guardamos nuestros archivos.

Para enumerar los archivos en el directorio de trabajo, usamos el comando ls.

![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/18a152f4-6b29-4f81-a449-1dd78e10dd12)

#### cd
Para cambiar el directorio de trabajo (donde estamos parados en el laberinto) usamos el comando cd. Para hacer esto, escribimos cd seguido de la ruta del directorio de trabajo deseado.

![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/583031f5-9e27-4c8a-b948-7e639572d063)

