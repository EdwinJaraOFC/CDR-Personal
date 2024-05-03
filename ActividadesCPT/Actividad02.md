<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Actividad 2: Implementación de una conectividad básica</h1>
</p>

## Tabla de direccionamiento
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150296803/221dd40d-eb2a-4ea4-b5db-2210989b9c47">
</p>

# Paso 1: Realiza una configuración básica en el S1 y el S2
## Configura un nombre de host en el S1
1. Haz clic en S1 y luego en la ficha CLI.
2. Introduce el comando correcto para configurar el nombre de host S1.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/84659ff9-4531-46b2-8e31-ba45d3c48b20">
</p>

## Configura la consola y las contraseñas cifradas de modo EXEC privilegiado
1. Usa checha como la contraseña de la consola.
2. Usa jeka para la contraseña del modo EXEC privilegiado.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/09edb146-1a99-4095-bcb4-c2d306e2076a">
</p>

## Verifica la configuración de contraseñas para el S1.
#### ¿Cómo puedes verificar que ambas contraseñas se hayan configurado correctamente?
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/899e4a1d-d602-4008-8412-af0fcdfdef10">
</p>
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/75e2d8a4-99a6-4104-91ed-e6e8641e39eb">
</p>

## Configura un aviso de MOTD.
1. Utiliza un texto de aviso adecuado para advertir contra el acceso no autorizado. El siguiente texto es
un ejemplo:
```
Acceso autorizado únicamente. Los infractores se procesarán en la medida en que lo permita la ley.
```
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/255becca-974b-47d3-a5d4-84c88557c2b6">
</p>

2. Guarda el archivo de configuración en la NVRAM.
#### ¿Qué comando emite para realizar este paso?
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/cc4b7b0e-bb7d-4e4d-85b4-2922bf72ce2f">
</p>

## Paso 2: Repita los pasos 1 a 5 para el S2
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/fa17c053-2664-4300-a620-4e381435d44d">
</p>
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/7441b08d-8617-43ac-b83d-47767ecccdf9">
</p>

### Configura ambas PC con direcciones IP
1. Haz clic en PC1 y luego en la ficha Escritorio.
2. Haz clic en Configuración de IP. En la tabla de direccionamiento anterior, puede ver que la dirección IP para la PC1 es 192.168.1.1 y la máscara de subred es 255.255.255.0. Introduzca esta información para la PC1 en la ventana Configuración de IP.
3. Repite los pasos 1a y 1b para la PC2.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/d572b834-47e9-40cd-8371-fa10266110fa">
</p>

### Prueba la conectividad a los switches.
1. Haz clic en PC1. Cierre la ventana Configuración de IP si todavía está abierta. En la ficha Escritorio, haga clic en Símbolo del sistema.
2. Escribe el comando ping y la dirección IP para S1 y presione Enter.
```
Packet Tracer PC Línea de comandos 1.0
PC> ping 192.168.1.253
```
#### ¿Tuviste éxito? Explica.
No tuve éxito al enviar el ping, ya que todavía no he configurado una dirección IP para los switches.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/2cd6d2f0-cc22-4fdc-9176-7f57b9cf73f6">
</p>

## Paso 3: Configura la interfaz de administración de switches
### Configura el S1 con una dirección IP.
Los switches pueden usarse como dispositivos plug-and-play. Esto significa que no necesitan configurarse para que funcionen. Los switches reenvían información desde un puerto hacia otro sobre la base de direcciones de control de acceso al medio (MAC).
#### Si este es el caso, ¿por qué lo configuraremos con una dirección IP?
Tenemos que usar una dirección IP para poderlo administrar de manera remota.<br>
Usa los siguientes comandos para configurar el S1 con una dirección IP.
```
S1# configure terminal
  Enter configuration commands, one per line. Finalice con CNTL/Z.
S1(config)# interface vlan 1
S1(config-if)# ip address 192.168.1.253 255.255.255.0
S1(config-if)# no shutdown
  %LINEPROTO-5-UPDOWN: Line protocol on Interface Vlan1, changed state to up
S1(config-if)#
S1(config-if)# exit
S1#
```
#### ¿Por qué debe introducir el comando no shutdown?
Usamos "no shutdown" basicamente para que se habilite esta dirección en esta interfaz.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/abd593a5-eafb-4a37-8b17-003f894caca8">
</p>

### Configura el S2 con una dirección IP
Usa la información de la tabla de direccionamiento para configurar el S2 con una dirección IP.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/e385e026-4a02-4b49-93f0-af424a435f78">
</p>

### Verifica la configuración de direcciones IP en el S1 y el S2
Usa el comando show ip interface brief para ver la dirección IP y el estado de todos los puertos y las interfaces del switch. También puede utilizar el comando show running-config.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/e6e62ac1-7ea1-4f20-bb5e-980cc17b0f35">
</p>
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/cb46e352-f1db-4776-a9b6-22aa5e58af3b">
</p>

### Guarda la configuración para el S1 y el S2 en la NVRAM
#### ¿Qué comando se utiliza para guardar en la NVRAM el archivo de configuración que se encuentra en la RAM?
<div align="center"; style="display: flex; justify-content: space-between;">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/6880dc5e-b142-4c35-8f2c-eff7682c507b" width="420px">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/ab15721c-f89e-40c9-b690-06f73ea4c992" width="400px">
</div>

### Verifica la conectividad de la red
Puedes verificar la conectividad de la red mediante el comando ping. Es muy importante que haya conectividad en toda la red. Se deben tomar medidas correctivas si se produce una falla. Desde la PC1 y la PC2, haga ping al S1 y S2.

1. Haga clic en PC1 y luego en la ficha Escritorio.
2. Haga clic en Símbolo del sistema.
3. Haga ping a la dirección IP de la PC2.
4. Haga ping a la dirección IP del S1.
5. Haga ping a la dirección IP del S2
<div align="center"; style="display: flex; justify-content: space-between;">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/8a1247cb-99d4-40fa-9398-1121133eb8c6" width="320px">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/73855886-1efb-445c-a1e5-8a60a0e77723" width="320px">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/696f4605-6873-4d89-8355-d7d6f739597a" width="320px">
</div>

**Nota:** También usa el ping en la CLI del switch y en la PC2.
Todos los ping deben tener éxito. Si el resultado del primer ping es 80%, inténtelo otra vez. Ahora debería ser 100%. Más adelante, aprenderá por qué es posible que un ping falle la primera vez. Si no puede hacer ping a ninguno de los dispositivos, vuelva a revisar la configuración para detectar errores.
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/ea9e068f-a235-4a71-8bc4-439ba598e791">
</p>
