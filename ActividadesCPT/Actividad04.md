<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Actividad 4: Configuración inicial de un Switch</h1>
</p>

## Paso 1: Verifica la configuración predeterminada del switch
### Ingresa al modo EXEC privilegiado.
Puedes acceder a todos los comandos del switch en el modo EXEC privilegiado. Sin embargo, debido a que muchos de los comandos privilegiados configuran parámetros operativos, el acceso privilegiado se debe proteger con una contraseña para evitar el uso no autorizado.

El conjunto de comandos EXEC privilegiado incluye los comandos disponibles en el modo EXEC del usuario, muchos comandos adicionales y el comando configure a través del cual se obtiene acceso a los modos de configuración.

1. Haz clic en S1 y luego en la pestaña CLI. Presione Enter.
2. Ingresa al modo EXEC privilegiado introduciendo el comando enable:
Switch> enable
Switch#
Observa que la solicitud cambió para reflejar el modo EXEC privilegiado.

<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/24614990-7837-4ef0-afab-32c05d799d33">
</p>

### Examina la configuración actual del switch.
Ingresa el comando show running-config.<br>
Switch# show running-config<br>

Responde las siguientes preguntas:<br>

**a) ¿Cuántas interfaces Fast Ethernet tiene el switch?**
- 24 interfaces Fast Ethernet<br>

**b) ¿Cuántas interfaces Gigabit Ethernet tiene el switch?**
- 2 interfaces Gigabit Ethernet<br>

**c) ¿Cuál es el rango de valores que se muestra para las líneas vty?**
- De 0 a 15<br>

**d) ¿Qué comando muestra el contenido actual de la memoria de acceso aleatorio no volátil (NVRAM)? show star**
- show startup-config<br>

**e) ¿Por qué el switch responde con "startup-config no está presente"?**
- Porque no hemos almacenado nada aún.

<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/12bd29aa-a9fb-48be-9ed1-e45c66b05dbd">
</p>

## Paso 2: Crea una configuración básica del switch
### Asigna un nombre a un switch.
Para configurar los parámetros de un switch, quizá deba pasar por diversos modos de configuración. Observa cómo cambia la petición de entrada mientras navega por el switch.<br>

Switch# configure terminal<br>
Switch(config)# hostname S1<br>
S1(config)# exit<br>
S1#<br>

<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/953dafc5-74b2-4322-b42b-44665950e1a3">
</p>

### Proporciona acceso seguro a la línea de consola.
Para proporcionar un acceso seguro a la línea de la consola, acceda al modo config-line y establezca la contraseña de consola en cesar.<br>

S1# configure terminal<br>
Enter configuration commands, one per line. End with CNTL/Z.<br>
S1(config)# line console 0<br>
S1(config-line)# password cesar<br>
S1(config-line)# login<br>
S1(config-line)# exit<br>
S1(config)# exit<br>
%SYS-5-CONFIG_I: Configured from console by console<br>
S1#<br>

<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/fa1c849e-dda8-412c-99cf-e183a5a9f13a">
</p>

**¿Por qué se requiere el comando login?** Porque sin el login la contraseña no funciona.

### Verifica que el acceso a la consola sea seguro.
Salimos del modo privilegiado para verificar que la contraseña del puerto de consola esté vigente.<br>

S1# exit<br>
Switch con0 is now available<br>
Press RETURN to get started.<br>
User Access Verification<br>
Password:<br>
S1><br>

<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/cd165060-6e63-419b-aa0a-5ee094a573c0">
</p>

### Proporciona un acceso seguro al modo privilegiado.
Establece la contraseña de enable en jeka. Esta contraseña protege el acceso al modo privilegiado.<br>

S1> enable<br>
S1# configure terminal<br>
S1(config)# enable password jeka<br>
S1(config)# exit<br>
%SYS-5-CONFIG_I: Configured from console by console<br>
S1#<br>

<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/46cf0678-2767-4890-9843-9ac9ec710193">
</p>

### Verifica que el acceso al modo privilegiado sea seguro.
1. Introduce el comando exit nuevamente para cerrar la sesión del switch.
2. Presiona Enter; a continuación, se le pedirá que introduzca una contraseña:
User Access Verification
Password:
3. La primera contraseña es la contraseña de consola que configuró para line con 0. Introduzca esta contraseña para volver al modo EXEC del usuario.
4. Introduce el comando para acceder al modo privilegiado.
5. Introduce la segunda contraseña que configuró para proteger el modo EXEC privilegiado.
6. Verifica su configuración examinando el contenido del archivo de configuración en ejecución:
S1# show running-config
Ten en cuenta que la consola y las contraseñas de activación están en texto plano. Esto podría suponer un riesgo para la seguridad si alguien está mirando por encima de su hombro u obtiene acceso a los archivos de configuración almacenados en una ubicación de copia de seguridad. 

<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/4957d964-bd5d-4a50-802e-b83b98245af3">
</p>

### Configura una contraseña encriptada para proporcionar un acceso seguro al modo privilegiado.
La contraseña de enable se debe reemplazar por una nueva contraseña secreta encriptada mediante el comando enable secret. Configura la contraseña de enable secret como itsasecret.<br>

S1# config t<br>
S1(config)# enable secret itsasecret<br>
S1(config)# exit<br>
S1#<br>

**Nota:** La contraseña de enable secret sobrescribe la contraseña de enable password. Si ambos están configurados en el switch, debes ingresar la contraseña enable secret para ingresar al modo EXEC privilegiado. 

<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/197a3630-058a-4739-9d03-4c6d643840e6">
</p>

### Verifica si la contraseña de enable secret se agregó al archivo de configuración.
Introduce el comando show running-config nuevamente para verificar si la nueva contraseña de enable secret está configurada.<br>
Nota: Puedes abreviar show running-config como<br>

S1# show run<br>

**¿Qué se muestra como contraseña de enable secret?**
- $1$mERr$ILwq/b7kc.7X/ejA4Aosn0

**¿Por qué la contraseña de enable secret se ve diferente de lo que se configuró?**
- Porque la contraseña está encriptada.

<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/b46c0eb5-4ce1-4a20-aea7-ac4f161adb26">
</p>

### Encripta las contraseñas de consola y de enable
Como notó en el paso anterior, la contraseña enable secret estaba encriptada, pero las contraseñas enable y console todavía estaban en texto plano. Ahora encriptamos estas contraseñas de texto no cifrado con el comando service password-encryption.<br>
S1# config t<br>
S1(config)# service password-encryption<br>
S1(config)# exit<br>

<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/b8e033d4-819d-42af-8419-7fc24be685d4">
</p>

**Si configuras más contraseñas en el switch, ¿se mostrarán como texto no cifrado o en forma cifrada en el archivo de configuración? Explica.**
Las contraseñas se mostrarán en forma cifrada debido a que el comando de configuración se ejecuta solo una vez y automáticamente encripta todas las contraseñas ingresadas.

## Paso 3: Configure un aviso de MOTD
### Configura un aviso de mensaje del día (MOTD).
El conjunto de comandos de Cisco IOS incluye una característica que permite configurar los mensajes que cualquier persona puede ver cuando inicia sesión en el switch. Estos mensajes se denominan “mensajes del día” o “avisos de MOTD”. Coloca el texto del mensaje en citas o utilizando un delimitador diferente a cualquier carácter que aparece en la cadena de MOTD.<br>

S1# config t<br>
S1(config)# banner motd "This is a secure system. Authorized Access Only!<br>
S1(config)# exit<br>
%SYS-5-CONFIG_I: Configured from console by console<br>
S1#<br>

<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/b5be9353-a147-40fc-abd0-ff68c032e7f6">
</p>

**¿Cuándo se muestra este aviso?**
- Se muestra cuando quieres ingresar o iniciar sesión.

**¿Por qué todos los switches deben tener un aviso de MOTD?**
- Porque necesitamos evitar que personas no autorizadas no ingresen.

## Paso 4: Guarda y verifica archivos de configuración en NVRAM
### Verifica que la configuración sea precisa mediante el comando show run.
Guarda el archivo de configuración. Tu has completado la configuración básica del switch. Ahora haga una copia de seguridad del archivo de configuración en ejecución a NVRAM para garantizar que los cambios que se han realizado no se pierdan si el sistema se reinicia o se apaga.
S1# copy running-config startup-config Destination filename [startup-config]?[Enter]
Building configuration…
[OK]

<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/77cdb4b5-a3a4-4680-8ce6-acbe609d633f">
</p>

**¿Cuál es la versión abreviada más corta del comando copy running-config startup-config? Examine el archivo de configuración de inicio.¿Qué comando muestra el contenido de la NVRAM.**
- La versión abreviada más corta del comando copy running-config es cop r st.
- show startup-config.

**¿Todos los cambios realizados están grabados en el archivo?**
- Sí, están grabados y no se van a borrar.

## Paso 5: Configura S2
Hemos completado la configuración en S1. Ahora configura el S2. Si no recuerda los comandos, consulte las partes 1 a 4 para obtener ayuda.
Configura el S2 con los siguientes parámetros:
1. Device name: S2
2. Protege el acceso a la consola con la contraseña chalo.
3. Configure enable password como claudi y una contraseña enable secret como itsasecret.
4. Configura un mensaje apropiado para aquellos que inician sesión en el switch.
5. Encripta todas las contraseñas de texto no cifrado.
6. Asegúrate de que la configuración sea correcta.
7. Guarda el archivo de configuración para evitar perderlo si el switch se apaga.
8. Cierra la ventana de configuración para S2.

<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/9e73b9f6-be06-4824-85d6-ad2e6198b141">
</p>

<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/4d1a7c57-dff3-4a5f-9e32-1336c1d6222f">
</p>
