<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Actividad 6: Crear una red con un switch y un router - Modo Físico</h1>
</p>

## Topología

<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/6877acfb-6276-4a96-9c91-655d52a36416">
</p>

## Tabla de asignación de direcciones

<p align="center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/831bd556-cc46-4a98-8d6a-c55c2ca56ec4">
</p>

## Paso 1: Configura la topología de red
1. Mueva el router y el switch requeridos del Estante al Rack.
2. Mueva los PCs requeridos del Estante a la Mesa.
3. Conecta los dispositivos como se muestra en la Topologia y en la Tabla de asignación de
direcciones.
4. Encienda todos los dispositivos.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/11b93b28-5cc3-465c-9c09-42335d1a1cd5" width="500">
</p>

## Paso 2: Configurar los dispositivos y verificar la conectividad
En esta parte deberás configurar la topología de la red y los parámetros básicos, como las direcciones IP de las interfaces, el acceso de los dispositivos y las contraseñas. Consulte la Topología y la Tabla de asignación de direcciones que se encuentran al inicio de esta actividad para conocer los nombres de los dispositivos y la información de las direcciones.

### Asignar información de IP estática a las interfaces de la PC
1. Configura la dirección IP, la máscara de subred y los parámetros del gateway predeterminado en la PC-A.
2. Configura la dirección IP, la máscara de subred y los parámetros del gateway predeterminado en la PC-B.
3. En una ventana con el símbolo del sistema en la PC-A, haga ping a la PC-B.
#### ¿Por qué los pings no fueron correctos?

### Configura el router
1. Acceda al router mediante el puerto de consola y habilite el modo EXEC con privilegios.
2. Ingresa al modo de configuración.
3. Asigna el nombre de dispositivo al router.
4. Asigna class como la contraseña cifrada del modo EXEC privilegiado.
5. Asigna cisco como la contraseña de la consola y habilite el inicio de sesión.
6. Asigne cisco como la contraseña de vty y habilite el inicio de sesión.
7. Encripta las contraseñas de texto sin formato.
8. Crea un aviso que advierta a todo el que acceda al dispositivo que el acceso no autorizado está prohibido.
9. Configura y activa las dos interfaces en el router.
10. Configura una descripción de interfaz para cada interfaz e indique qué dispositivo está conectado.
11. Para habilitar el enrutamiento IPv6, ingrese el comando ipv6 unicast-routing.
12. Guardar la configuración en ejecución en el archivo de configuración de inicio
13. Configura el reloj en el router.<br>
**Nota:** Utiliza el signo de interrogación (?) para poder determinar la secuencia correcta de
parámetros necesarios para ejecutar este comando.
14. En una ventana con el símbolo del sistema en la PC-A, haga ping a la PC-B.<br>
**Nota:** Si los pings no son correctos, es posible que debas desactivar el Firewall.<br> **¿Fueron correctos los pings? Explica.**

### Configura el switch
En este paso, configura el nombre de host, la interfaz de VLAN 1 y su puerta de enlace predeterminada.
1. Acceda al switch mediante el puerto de consola y habilite al modo EXEC con privilegios.
2. Ingresa al modo de configuración.
3. Asigna un nombre de dispositivo al switch.
4. Configura y activa la interfaz VLAN en el switch S1.
5. Configura la puerta de enlace predeterminada para el switch S1.
6. Guarda la configuración en ejecución en el archivo de configuración de inicio

### Verifica la conectividad de extremo a extremo
1. Desde la PC-A, haga ping a la PC-B.
2. Desde S1, ping PC-B.<br>
Todos los pings deben tener éxito.

## Paso 3: Muestra la información del dispositivo
### Muestra la tabla de routing en el router
Utiliza el comando show ip route en R1 para responder las preguntas siguientes:
#### ¿Qué código se utiliza en la tabla de enrutamiento para indicar una red conectada directamente?
#### ¿Cuántas entradas de ruta están codificadas con un código C en la tabla de enrutamiento?
#### ¿Qué tipos de interfaces están asociadas a las rutas con código C?
Usa el comando show ipv6 route en R1 para ver las rutas de IPv6.

### Muestra la información de la interfaz en el R1
Utiliza el comando show interface g0/0/1 para responder las preguntas siguientes:
#### ¿Cuál es el estado operativo de la interfaz G0/0/1?
#### ¿Cuál es la dirección de control de acceso a los medios (MAC) de la interfaz G0/0/1?
#### ¿Cómo se muestra la dirección de Internet en este comando?
Para obtener información sobre IPv6, escribe el comando show ipv6 interface interface .

### Muestra una lista de resumen de las interfaces del router y del switch
Existen varios comandos que se pueden utilizar para verificar la configuración de interfaz. Uno de los más útiles es el comando show ip interface brief. El resultado del comando muestra una lista resumida de las interfaces en el dispositivo y brinda información inmediata sobre el estado de cada interfaz.
1. Ingresa el comando show ip interface brief en R1.
```
R1# show ip interface brief
```
2. Ingresa el comando show ipv6 interface brief en R1 para ver información de IPv6 de las interfaces.
```
R1# show ipv6 interface brief
```
3. Ingresa el comando show ip interface brief en S1.
```
S1# show ip interface brief
```
## Preguntas
#### Si la interfaz G0/0/1 se mostrará administratively down, ¿qué comando de configuración de interfaz usaría para activar la interfaz?
#### ¿Qué ocurriría si hubiera configurado incorrectamente la interfaz G0/0/1 en el router con una dirección IP 192.168.1.2?
