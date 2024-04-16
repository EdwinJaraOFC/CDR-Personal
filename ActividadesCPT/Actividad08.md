<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Actividad 8: Comunicaciones de TCP y UDP</h1>
</p>

## Paso 1: Genera tráfico de red en modo de simulación y vea multiplexación

### Genera tráfico para completar las tablas del protocolo de resolución de direcciones (ARP)
Realiza la siguiente tarea para reducir la cantidad de tráfico de red que se ve en la simulación.
1. Haz clic en MultiServer y luego haz click en **Desktop** tab > **Command Prompt**.
2. Ingresa el comando **ping -n 1 192.168.1.255**. Está haciendo ping a la dirección broadcast de la LAN del cliente. La opción de comando enviará sólo una solicitud de ping en lugar de las cuatro habituales. Esto tomará unos segundos ya que cada dispositivo en la red responde a la solicitud de ping de MultiServer.
3. Cierra la ventana **MultiServer**.

<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297452/89754dda-7968-47cb-9c50-8b62df82fed1">
</p>

**Nota:** El comando "-n 1" envía solo una solicitud de ping, aunque en el terminal se muestren cuatro envíos. Esto se debe a cómo funciona el comando en un prompt de Windows real, donde obedece al comando y envía una sola solicitud.

<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297452/e5096bd0-0ad1-44a5-acff-e1b735e84df0" height="200">
</p>

**Nota 2:** La cantidad de solicitudes enviadas depende del número especificado en el comando. Por ejemplo, si se utiliza el comando "n -2", se enviarán dos solicitudes en lugar de una.
<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150296803/471a851f-2d8d-4437-a20c-3fb3a9f4b57b" height="200">
</p>

### Genera tráfico web (HTTP)
1. Cambia a modo de simulación.
2. Haz clic en **Cliente HTTP** y abre el **Explorador Web** desde el escritorio.
3. En el campo URL, introduce **192.168.1.254** y haz clic en **Go** (Ir). Los sobres (PDU) aparecerán en la ventana de topología.
4. Minimiza, pero no cierres, la ventana de configuración de **HTTP Client**.

<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297438/085933e2-4924-4a16-9a3d-4adf6e0f4806" height="150">
  <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297438/e5d90be3-354b-4281-8a5d-99b50ec50df6" height="150">
</p>


### Genera tráfico FTP.
1. Haz clic en **FTP Client** y abra el **Command Prompt** desde el escritorio
2. Introduce el comando **ftp 192.168.1.254**. Las PDU aparecerán en la ventana de simulación.
3. Minimiza, pero no cierres, la ventana de configuración de **FTP Client**.


<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297438/a93e3728-78f3-4f60-a480-da095956bfb5" height="150">
  <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297438/74ca1217-39d3-470e-bd57-e72b1697fe61" height="150">
</p>


### Genera tráfico DNS.
1. Haz clic en DNS Client y abra el **Command Prompt**.
2. Introduce el comando **nslookup multiserver.pt.ptu**. Aparecerá una PDU en la ventana de simulación.
3. Minimiza, pero no cierre, la ventana de configuración de **DNS Client**.

<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297438/2bdeaa46-0ecf-4ad1-8581-ec3b80e60eb2" height="150">
  <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297438/7555c3bd-a1e1-4043-b178-83747d397545" height="150">
</p>

### Genera tráfico de correo electrónico.
1. Haz clic en **E-Mail Client** y abre la herramienta **E Mail** desde el escritorio.
2. Haz clic en **Compose** (Redactar) y escribe la siguiente información:<br>- **To:** user@multiserver.pt.ptu<br>- **Subject:** Personalizar la línea de asunto<br>- **E-Mail Body:** personalizar el correo electrónico
3. Haz clic en **Send** (Enviar).
4. Minimiza, pero no cierres, la ventana de configuración de **E-Mail Client**.

<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297438/11c97a53-454f-438e-9e97-bd748d78ec39" height="100">
  <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297438/c1d524ae-be0a-4531-9df8-28ed20588e84" height="100">
</p>

### Verifica que se haya generado tráfico y que esté preparado para la simulación.
Ahora debería haber entradas de PDU en el panel de simulación para cada uno de los equipos cliente.

<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297438/cc41aa5d-9cf0-47e3-afdc-26d69b396d3a" height="300">
  <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297438/7565f8cd-111c-4cb4-ba33-7e440348e226" height="300">
</p>

### Examina la multiplexación a medida que el tráfico cruza la red.
Ahora utilizarás el **botón Capturar/Reenviar** del Panel de Simulación para observar los diferentes protocolos que viajan por la red.

1. Haz clic una vez en **Capture/Forward**. Todas las PDU se transfieren al switch.

<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297438/5ff64e2d-097e-4567-b0d0-110fb9ca168f" height="300">
</p>
   
2. Haz clic en **Capturar/Reenviar** seis veces y observe las PDU de los diferentes hosts mientras viajan por la red. Observe que solo una PDU puede cruzar un cable en cada dirección en un momento determinado.

<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150296803/de502acd-9be4-4288-805a-148979c937d3" height="300">
</p>

**¿Cómo se llama esto?**
- Se llama multiplexacion, esto es transmitir varios datos por un mismo medio, uno por uno.<br>

**Aparece una variedad de PDU en la lista de eventos en el Panel de simulación. ¿Cuál es el significado de los diferentes colores?**
- Los colores nos muestran los protocolos de cada PDU, sean HTTP, FTP, etc.

## Paso 2: Examinar la funcionalidad de los protocolos TCP y UDP

### Examinar el tráfico HTTP cuando los clientes se comunican con el servidor
1. Haz clic en **Reset Simulation (Restablecer simulación)**.
2. Filtrar el tráfico que se muestra actualmente sólo a las PDU **HTTP** y **TCP**. Para filtrar el
tráfico que se muestra actualmente:<br>- Haz clic en **Edit Filters** y alterna el botón **Show All/None**.<br>- Selecciona **HTTP** y **TCP**. Haz clic en la «x» roja en la esquina superior derecha del cuadro Editar filtros para cerrarla. Los eventos visibles ahora deberían mostrar solo las PDU **HTTP** y **TCP**.
3. Abre el navegador en HTTP Client e ingresa **192.168.1.254** en el campo URL. Haz clic en **Ir** para conectarse al servidor a través de HTTP. Minimiza HTTP Client window.
4. Haz clic en **Capturar/Reenviar** hasta que aparezca una PDU para HTTP. Tenga en cuenta que el color del envolvente de la ventana de topología coincide con el código de color de la PDU HTTP del Panel de simulación.

<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150296803/8846f5f9-29e3-4958-9362-8460390bb040" height="300">
</p>

**¿Por qué tardó tanto en aparecer la PDU HTTP?**
- Porque primero se debe establecer una conexión TCP entre el multiserver y el cliente, para que así el trafico HTTP pueda comenzar.

5. Haz clic en el sobre de la PDU para mostrar los detalles de la PDU. Haz clic en **Outbound
PDU Details** y desplácese hacia abajo hasta la segunda sección.

**¿Cómo se rotula la sección?**
- TCP<br>

**¿Se consideran confiables estas comunicaciones?**
- SI<br>

<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150296803/17a714dd-8525-4438-9cdb-cb28c5cbba09" height="300">
</p>

Registra los valores de **SRC PORT (PUERTO DE ORIGEN), DEST PORT (PUERTO DE DESTINO), SEQUENCE NUM (NÚMERO DE SECUENCIA) y ACK NUM (NÚMERO DE RECONOCIMIENTO)**.

<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150296803/4bd17b02-c899-4ce4-9a8d-3cdddfe22ff3" height="150">
</p>

**Nota:** Al dividirnos las partes de la actividad observamos que nuestros puertos de origen eran distintos, lo cual es normal ya que suele variar dependiendo de la simulación.

<p align="justify">
Mira el valor en el campo Indicadores, que se encuentra junto al campo Ventana. Los valores ala derecha de la «b» representan los indicadores TCP que se establecen para esta etapa de la conversación de datos. Cada uno de los seis lugares corresponde a una bandera. La presencia de un «1» en cualquier lugar indica que el indicador está establecido. Se puede configurar más de una bandera a la vez. Los valores de las banderas se muestran a continuación.
</p>

<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150296803/b16ab445-be18-44a9-b30b-44529dedacd0" height="100">
  <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297438/ab9f340b-3abc-4dd3-bbe7-1aea06987ab6" height="100">
</p>

**¿Qué indicadores TCP se establecen en esta PDU?**
- ACK y PSH<br>

Cierra la PDU y Haz clic en **Capture/Forward** hasta que una PDU con una marca de verificación
regrese al **HTTP Client**.<br>

Cierra el sobre de PDU y seleccione **Inbound PDU Details**. ¿En qué cambiaron los números de
puerto y de secuencia? Haz clic en la **PDU HTTP** que **HTTP Client** ha preparado para enviar a
MultiServer. Este es el comienzo de la comunicación HTTP. Haz clic en este segundo sobre de PDU
y seleccione Outbound PDU Details (Detalles de PDU saliente).<br>

**¿Qué información aparece ahora en la sección TCP?¿En qué se diferencian los números de puerto
y de secuencia con respecto a las dos PDU anteriores?**
- Los puertos de origen y destino se invierten, cambia el número de secuencia y Ack, así como Flag

Restablece la simulación.

### Examinar el tráfico FTP cuando los clientes se comunican con el servidor.
1. Abre el símbolo del sistema en el escritorio del cliente FTP. Inicie una conexión FTP
ingresando ftp 192.168.1.254.
2. En el Panel de simulación, cambia Edit Filters para mostrar solo FTP y TCP.
  
<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297452/3f9a2747-46b6-45f9-8212-fc75d8659e6a">
</p>

3. Haz clic en Capture/Forward. Haz clic en el segundo sobre PDU para abrirlo.Haz clic en la
pestaña Outbound PDU Details y desplácese hacia abajo hasta la sección TCP.<br>

**¿Se consideran confiables estas comunicaciones?**
- Sí

4. Registra los valores de SRC PORT (PUERTO DE ORIGEN), DEST PORT (PUERTO DE DESTINO), SEQUENCE NUM (NÚMERO DE SECUENCIA) y ACK NUM (NÚMERO DE RECONOCIMIENTO).

<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297452/c78eff0b-f8ac-4187-906f-13fcab1d27c0" height="300">
</p>

**¿Cuál es el valor en el campo de bandera?**
- 0b00000010

5. Cierra la PDU y haz clic en Capture/Forward hasta que una PDU vuelva a FTP Client con
una marca de verificación.

<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297452/df3f33d2-cc70-4c60-9d9d-48c9af041d6a" >
</p>

6. Cierra el sobre de PDU y seleccione Inbound PDU Details.<br>
  
**¿En qué cambiaron los números de puerto y de secuencia?**
- Se invitieron el source y dest, así como un cambio en un dígito de la FLAG
    
7. Haz clic en la ficha de detalles de la PDU saliente.<br>

**¿En qué se diferencian los números de puerto y secuencia de los resultados anteriores?**

<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297452/e8e4e7e5-d2f8-4254-9944-92ede7b5f4aa" height="300">
</p>

8. Cierra la PDU y haz clic en Capture/Forward hasta que una segunda PDU vuelva a FTP
Client. La PDU es de un color diferente.

9. Abre la PDU y selecciona Inbound PDU Details. Desplázate hasta después de la sección
TCP.<br>

**¿Cuál es el mensaje del servidor?**
- El mensaje es "Message:Welcome to PT Ftp server "
  
10. Haz clic en Reset Simulation (Restablecer simulación).

### Examina el tráfico DNS cuando los clientes se comunican con el servidor.
1. Repita los pasos de la Parte 1 para crear tráfico DNS.
2. En el panel de simulación, modifique las opciones de Edit Filters para que solo se muestren
DNS y UDP.
3. Haz clic en el sobre de PDU para abrirlo.
4. Mire los detalles del modelo OSI para la PDU saliente.

**¿Qué es el protocolo de capa 4?**
- Es el protocolo UDP<br>

**¿Se consideran confiables estas comunicaciones?**
- No es confiable
  
5. Abra la ficha Detalles de PDU saliente y busque la sección UDP de los formatos de PDU. Registre los valores de SRC PORT y DEST PORT .

<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297452/0ac88765-2188-4d82-8dc7-1df99bf04afb" >
</p>

**¿Por qué no hay números de secuencia y reconocimiento?**
- Porque UDP, al no ser una conexión confiable, no necesita almacenar esos datos extra de seguridad

6. Cierre la PDU y haz clic en Capture/Forward hasta que una PDU con una marca de
verificación regrese al DNS Client.
7. Cierra el sobre de PDU y seleccione Inbound PDU Details.

**¿En qué cambiaron los números de puerto y de secuencia?**
- Se invirtieron al regresar y llegar desde un dispositivo diferente.

<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297452/e26d2ed7-2c8e-42bc-b6c4-a2d41aec2a8b">
</p>

8. Haz clic en Reset Simulation (Restablecer simulación).

### Examina el tráfico de correo electrónico cuando los clientes se comunican con el servidor
1. Repite los pasos de la Parte 1 para enviar un correo electrónico a user@multiserver.pt.ptu.
2. En el panel de simulación, modifique las opciones de Edit Filters para que solo se muestren
POP3, SMTP y TCP.
3. Haz clic en el primer sobre de la PDU para abrirlo.
4. Haz clic en la pestaña Outbound PDU Details y desplácese hacia abajo hasta la última
sección.

<p align="center">
    <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297452/7ce12f92-96cf-4768-8b63-82ff9346a84f">
</p>

**¿Qué protocolo de la capa de transporte utiliza el tráfico de correo electrónico? ¿Se
consideran confiables estas comunicaciones?**
- Usa TCP, que, como hemos visto anteriormente, es seguro debido a los valores extra que se guardan

5. Registra los valores de SRC PORT (PUERTO DE ORIGEN), DEST PORT (PUERTO DE
DESTINO), SEQUENCE NUM (NÚMERO DE SECUENCIA) y ACK NUM (NÚMERO DE
RECONOCIMIENTO). ¿Cuál es el valor del campo de bandera?

<p align="center">
    <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297452/f7aec8ea-8b86-492a-822e-1ada7a53530b">
</p>

6. Cierra la PDU y haz clic en Capture/Forward hasta que una PDU regrese al E-Mail Client
con una marca de verificación.
7. Haz clic en el sobre TCP PDU y seleccione Inbound PDU Details.

**¿En qué cambiaron los números de puerto y de secuencia?**

<p align="center">
    <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297452/861434d7-eda3-42d1-a333-f54d0503e104" height="150">
    <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297452/4c384b2c-3a85-4262-b2e8-f17e3906f9a4" height="150">
</p>

8. Haz clic en la ficha de detalles de la PDU saliente. **¿En qué se diferencian los números de
puerto y de secuencia con respecto a los dos resultados anteriores?**
- En el sq number, puesto que implementa, además de SYN, ACK

9. Hay una segunda PDU de un color diferente que E-Mail Client hha preparado para enviar a
MultiServer. Este es el comienzo de la comunicación de correo electrónico. Haz clic en este
segundo sobre de PDU y seleccione Outbound PDU Details.

**¿En qué se diferencian los números de puerto y de secuencia con respecto a las dos PDU
anteriores?**
- En el valor de la FLAG (0b00011000)

**¿Qué protocolo de correo electrónico se relaciona con el puerto TCP 25? ¿Qué protocolo se
relaciona con el puerto TCP 110?**
- Con el TCP25, asociamos el protocolo SMTP (Protocolo Simple de Transferencia de Correo) y con el puerto TCP110, el protocolo POP3 (Post Office Protocol).
