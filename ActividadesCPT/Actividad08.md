<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Actividad 8: Comunicaciones de TCP y UDP</h1>
</p>

## Paso 1: Genera tráfico de red en modo de simulación y vea multiplexación

### Genera tráfico para completar las tablas del protocolo de resolución de direcciones (ARP)
Realiza la siguiente tarea para reducir la cantidad de tráfico de red que se ve en la simulación.
1. Haz clic en MultiServer y luego haz click en Desktop tab > Command Prompt.
2. Ingresa el comando ping -n 1 192.168.1.255. Está haciendo ping a la dirección broadcast de la LAN del cliente. La opción de comando enviará sólo una solicitud de ping en lugar de las cuatro habituales. Esto tomará unos segundos ya que cada dispositivo en la red responde a la solicitud de ping de MultiServer.
3. Cierra la ventana MultiServer.

### Genera tráfico web (HTTP)
1. Cambia a modo de simulación.
2. Haz clic en Cliente HTTP y abre el Explorador Web desde el escritorio.
3. En el campo URL, introduce 192.168.1.254 y haz clic en Go (Ir). Los sobres (PDU) aparecerán en la ventana de topología.
4. Minimiza, pero no cierres, la ventana de configuración de HTTP Client. 
![image](https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297438/085933e2-4924-4a16-9a3d-4adf6e0f4806)
![image](https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297438/e5d90be3-354b-4281-8a5d-99b50ec50df6)

### Genera tráfico FTP.
1. Haz clic en FTP Client y abra el Command Prompt desde el escritorio
2. Introduce el comando ftp 192.168.1.254. Las PDU aparecerán en la ventana de simulación.
3. Minimiza, pero no cierres, la ventana de configuración de FTP Client.
![image](https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297438/a93e3728-78f3-4f60-a480-da095956bfb5)
![image](https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297438/74ca1217-39d3-470e-bd57-e72b1697fe61)

### Genera tráfico DNS.
1. Haz clic en DNS Client y abra el Command Prompt
2. Introduce el comando nslookup multiserver.pt.ptu. Aparecerá una PDU en la ventana de simulación.
3. Minimiza, pero no cierre, la ventana de configuración de DNS Client. 
![image](https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297438/2bdeaa46-0ecf-4ad1-8581-ec3b80e60eb2)
![image](https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297438/7555c3bd-a1e1-4043-b178-83747d397545)

### Genera tráfico de correo electrónico.
1. Haz clic en E-Mail Client y abre la herramienta E Mail desde el escritorio.
2. Haz clic en Compose (Redactar) y escribe la siguiente información:
- To: user@multiserver.pt.ptu
- Subject: Personalizar la línea de asunto
- E-Mail Body: personalizar el correo electrónico
3. Haz clic en Send (Enviar).
4. Minimiza, pero no cierres, la ventana de configuración de E-Mail Client. 
![image](https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297438/11c97a53-454f-438e-9e97-bd748d78ec39)
![image](https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297438/c1d524ae-be0a-4531-9df8-28ed20588e84)

### Verifica que se haya generado tráfico y que esté preparado para la simulación.
Ahora debería haber entradas de PDU en el panel de simulación para cada uno de los equipos cliente.
![image](https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297438/cc41aa5d-9cf0-47e3-afdc-26d69b396d3a)
![image](https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297438/7565f8cd-111c-4cb4-ba33-7e440348e226)

### Examina la multiplexación a medida que el tráfico cruza la red.
Ahora utilizarás el botón Capturar/Reenviar del Panel de Simulación para observar los diferentes protocolos que viajan por la red.

**Nota:** El botón Capture/Forward ' >| ' es una flecha pequeña que apunta a la derecha con una barra vertical al lado.

1. Haz clic una vez en Capture/Forward. Todas las PDU se transfieren al switch.
 ![image](https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297438/5ff64e2d-097e-4567-b0d0-110fb9ca168f)
  
2. Haz clic en Capturar/Reenviar seis veces y observe las PDU de los diferentes hosts mientras viajan por la red. Observe que solo una PDU puede cruzar un cable en cada dirección en un momento determinado.

**¿Cómo se llama esto?**
- Se llama multiplexacion, esto es trasnmitir varios datos por un mismo medio uno por uno.
Aparece una variedad de PDU en la lista de eventos en el Panel de simulación.
**¿Cuál es el significado de los diferentes colores?**
- Los colores nos muestran los protocolos de cada PDU

## Paso 2: Examinar la funcionalidad de los protocolos TCP y UDP

### Examinar el tráfico HTTP cuando los clientes se comunican con el servidor
1. Haz clic en Reset Simulation (Restablecer simulación).
2. Filtrar el tráfico que se muestra actualmente sólo a las PDU HTTP y TCP . Para filtrar el
tráfico que se muestra actualmente:
- Haz clic en Edit Filters y alterna el botón Show All/None .
- Selecciona HTTP y TCP. Haz clic en la «x» roja en la esquina superior derecha del
cuadro Editar filtros para cerrarla. Los eventos visibles ahora deberían mostrar solo las
PDU HTTP y TCP .
3. Abre el navegador en HTTP Client e ingresa 192.168.1.254 en el campo URL. Haz clic en Ir
para conectarse al servidor a través de HTTP. Minimiza HTTP Client window.
4. Haz clic en Capturar/Reenviar hasta que aparezca una PDU para HTTP. Tenga en cuenta que el color del envolvente de la ventana de topología coincide con el código de color de la PDU HTTP del Panel de simulación.
![image](https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297438/943b7464-c4ca-41d5-9160-7f1b49912f52)

**¿Por qué tardó tanto en aparecer la PDU HTTP?**
- Porque primero se debe establecer una coneccion TCP entre el multiserver y el cliente  para que haci el trafico HTTP pueda comenzar.
5. Haz clic en el sobre de la PDU para mostrar los detalles de la PDU. Haz clic enOutbound
PDU Details y desplácese hacia abajo hasta la segunda sección.

- **¿Cómo se rotula la sección?**
- TCP
- **¿Se consideran confiables estas comunicaciones?**
- SI
Registra los valores de SRC PORT (PUERTO DE ORIGEN), DEST PORT (PUERTO DE DESTINO), SEQUENCE NUM (NÚMERO DE SECUENCIA) y ACK NUM (NÚMERO DE RECONOCIMIENTO).
![image](https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297438/2aeeb869-a161-4601-aa46-41f6508b6d8a)

Mira el valor en el campo Indicadores, que se encuentra junto al campo Ventana. Los valores ala
derecha de la «b» representan los indicadores TCP que se establecen para esta etapa de la
conversación de datos. Cada uno de los seis lugares corresponde a una bandera. La presencia de un
«1» en cualquier lugar indica que el indicador está establecido. Se puede configurar más de una
bandera a la vez. Los valores de las banderas se muestran a continuación.

![image](https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150296803/b16ab445-be18-44a9-b30b-44529dedacd0)
![image](https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150297438/ab9f340b-3abc-4dd3-bbe7-1aea06987ab6)

- ¿Qué indicadores TCP se establecen en esta PDU?
- ACK y PSH
- Cierra la PDU y Haz clic en Capture/Forward hasta que una PDU con una marca de verificación
regrese al HTTP Client.
- Cierra el sobre de PDU y seleccione Inbound PDU Details. ¿En qué cambiaron los números de
puerto y de secuencia? Haz clic en la PDU HTTP que HTTP Client ha preparado para enviar a
MultiServer. Este es el comienzo de la comunicación HTTP. Haz clic en este segundo sobre de PDU
y seleccione Outbound PDU Details (Detalles de PDU saliente).
- Pregunta:
- ¿Qué información aparece ahora en la sección TCP? ¿En qué se diferencian los números de puerto
y de secuencia con respecto a las dos PDU anteriores?

Restablece la simulación.


### Examinar el tráfico FTP cuando los clientes se comunican con el servidor.
- Abre el símbolo del sistema en el escritorio del cliente FTP. Inicie una conexión FTP
ingresando ftp 192.168.1.254.
- En el Panel de simulación, cambia Edit Filters para mostrar solo FTP y TCP.
- Haz clic en Capture/Forward. Haz clic en el segundo sobre PDU para abrirlo.Haz clic en la
pestaña Outbound PDU Details y desplácese hacia abajo hasta la sección TCP.
Pregunta:
- ¿Se consideran confiables estas comunicaciones?
- Registra los valores de SRC PORT (PUERTO DE ORIGEN), DEST PORT (PUERTO DE
DESTINO), SEQUENCE NUM (NÚMERO DE SECUENCIA) y ACK NUM (NÚMERO DE
RECONOCIMIENTO).
Pregunta:
-¿Cuál es el valor en el campo de bandera?
- Cierra la PDU y haz clic en Capture/Forward hasta que una PDU vuelva a FTP Client con
una marca de verificación.
- Cierra el sobre de PDU y seleccione Inbound PDU Details.
-Pregunta:
   -¿En qué cambiaron los números de puerto y de secuencia?

- Haz clic en la ficha de detalles de la PDU saliente.
-Pregunta:
-¿En qué se diferencian los números de puerto y secuencia de los resultados anteriores?

- Cierra la PDU y haz clic en Capture/Forward hasta que una segunda PDU vuelva a FTP
Client. La PDU es de un color diferente.
- Abre la PDU y selecciona Inbound PDU Details. Desplázate hasta después de la sección
TCP.
-Pregunta:
- ¿Cuál es el mensaje del servidor?
- Haz clic en Reset Simulation (Restablecer simulación).
### 4 Examina el tráfico DNS cuando los clientes se comunican con el servidor.
- Repita los pasos de la Parte 1 para crear tráfico DNS.
- En el panel de simulación, modifique las opciones de Edit Filters para que solo se muestren
DNS y UDP.
- Haz clic en el sobre de PDU para abrirlo.
- Mire los detalles del modelo OSI para la PDU saliente.
- Pregunta:
- ¿Qué es el protocolo de capa 4?

- ¿Se consideran confiables estas comunicaciones?

- Abra la ficha Detalles de PDU saliente y busque la sección UDP de los formatos de PDU.
- Registre los valores de SRC PORT y DEST PORT .
- Pregunta:
- ¿Por qué no hay números de secuencia y reconocimiento?

- Cierre la PDU y haz clic en Capture/Forward hasta que una PDU con una marca de
verificación regrese al DNS Client.
- Cierra el sobre de PDU y seleccione Inbound PDU Details.
- Pregunta:
- ¿En qué cambiaron los números de puerto y de secuencia?
- Haz clic en Reset Simulation (Restablecer simulación).

### 4 Examina el tráfico de correo electrónico cuando los clientes se comunican con el servidor
- Repite los pasos de la Parte 1 para enviar un correo electrónico a user@multiserver.pt.ptu.
- En el panel de simulación, modifique las opciones de Edit Filters para que solo se muestren
POP3, SMTP y TCP.
- Haz clic en el primer sobre de la PDU para abrirlo.
- Haz clic en la pestaña Outbound PDU Details y desplácese hacia abajo hasta la última
sección.
-Preguntas:
-¿Qué protocolo de la capa de transporte utiliza el tráfico de correo electrónico? ¿Se
consideran confiables estas comunicaciones?
- Registra los valores de SRC PORT (PUERTO DE ORIGEN), DEST PORT (PUERTO DE
DESTINO), SEQUENCE NUM (NÚMERO DE SECUENCIA) y ACK NUM (NÚMERO DE
RECONOCIMIENTO). ¿Cuál es el valor del campo de bandera?
- Cierra la PDU y haz clic en Capture/Forward hasta que una PDU regrese al E-Mail Client
con una marca de verificación.
- Haz clic en el sobre TCP PDU y seleccione Inbound PDU Details.
-Pregunta:
-¿En qué cambiaron los números de puerto y de secuencia?
- Haz clic en la ficha de detalles de la PDU saliente. ¿En qué se diferencian los números de
puerto y de secuencia con respecto a los dos resultados anteriores?
- Hay una segunda PDU de un color diferente que E-Mail Client hha preparado para enviar a
MultiServer. Este es el comienzo de la comunicación de correo electrónico. Haz clic en este
segundo sobre de PDU y seleccione Outbound PDU Details.
- Preguntas:
- ¿En qué se diferencian los números de puerto y de secuencia con respecto a las dos PDU
anteriores?
- ¿Qué protocolo de correo electrónico se relaciona con el puerto TCP 25? ¿Qué protocolo se
relaciona con el puerto TCP 110?

