<p align="left">
  <img src="https://semanadelcannabis.cayetano.edu.pe/assets/img/logo-upch.png" width="150">
  <h1 align="center">Actividad 2: Implementación de una conectividad básica</h1>
</p>

## Tabla de direccionamiento
<p align= "center">
  <img src="https://github.com/EdwinJaraOFC/CDRGrupo5/assets/150296803/221dd40d-eb2a-4ea4-b5db-2210989b9c47">
</p>

# Paso 1: Realiza una configuración básica en el S1 y el S2
## Configura un nombre de host en el S1.
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

![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/fa17c053-2664-4300-a620-4e381435d44d)
![image](https://github.com/EdwinJaraOFC/CDRPersonal/assets/150296803/7441b08d-8617-43ac-b83d-47767ecccdf9)

### Configurar las PC
Configura la PC1 y la PC2 con direcciones IP.
### Configura ambas PC con direcciones IP
1. Haz clic en PC1 y luego en la ficha Escritorio.
2. Haz clic en Configuración de IP. En la tabla de direccionamiento anterior, puede ver que la dirección IP para la PC1 es 192.168.1.1 y la máscara de subred es 255.255.255.0. Introduzca esta información para la PC1 en la ventana Configuración de IP.
3. Repite los pasos 1a y 1b para la PC2.
### Prueba la conectividad a los switches.
1. Haz clic en PC1. Cierre la ventana Configuración de IP si todavía está abierta. En la ficha Escritorio, haga clic en Símbolo del sistema.
2. Escribe el comando ping y la dirección IP para S1 y presione Enter.
```
Packet Tracer PC Línea de comandos 1.0
PC> ping 192.168.1.253
```
#### ¿Tuviste éxito? Explica.
