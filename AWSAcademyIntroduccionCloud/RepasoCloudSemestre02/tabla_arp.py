import time

# Tabla ARP estática inicial
arp_table = {
    '192.168.1.1': '00:1A:2B:3C:4D:5E',
    '192.168.1.2': '00:1A:2B:3C:4D:5F',
    '192.168.1.3': '00:1A:2B:3C:4D:60',
}

# Función para mostrar la tabla ARP actual
def imprimir_tabla_arp():
    print("Tabla ARP:")
    for ip, mac in arp_table.items():
        print(f"IP: {ip} -> MAC: {mac}")
    print()

# Función para buscar una dirección MAC en la tabla ARP
def buscar_arp(ip):
    mac = arp_table.get(ip)
    if mac:
        print(f"Dirección MAC para {ip} es {mac}")
    else:
        print(f"Solicitando ARP para {ip}...")
        simular_solicitud_arp(ip)

# Simulación de una solicitud ARP
def simular_solicitud_arp(ip):
    print(f"Enviando solicitud ARP para {ip}...")
    # Supongamos que recibimos una respuesta con una dirección MAC ficticia
    mac = f"00:1A:2B:3C:4D:{ip.split('.')[-1].zfill(2)}"
    print(f"Respuesta ARP recibida: {ip} -> {mac}")
    arp_table[ip] = mac
    imprimir_tabla_arp()

# Función para agregar una entrada en la tabla ARP
def agregar_entrada_arp(ip, mac):
    print(f"Agregando entrada ARP: {ip} -> {mac}")
    arp_table[ip] = mac
    imprimir_tabla_arp()

# Función para eliminar una entrada de la tabla ARP
def eliminar_entrada_arp(ip):
    if ip in arp_table:
        print(f"Eliminando entrada ARP para {ip}")
        del arp_table[ip]
        imprimir_tabla_arp()
    else:
        print(f"No se encontró una entrada ARP para {ip}")

# Función para envejecer y eliminar entradas antiguas
def envejecer_entradas_arp():
    print("Envejeciendo entradas ARP...")
    # Para simplificar, eliminamos todas las entradas
    arp_table.clear()
    imprimir_tabla_arp()

# Ejemplo de ejecución del simulador ARP
if __name__ == "__main__":
    imprimir_tabla_arp()
    buscar_arp('192.168.1.1')
    buscar_arp('192.168.1.4')
    agregar_entrada_arp('192.168.1.5', '00:1A:2B:3C:4D:61')
    eliminar_entrada_arp('192.168.1.2')
    time.sleep(2)  # Simula el paso del tiempo
    envejecer_entradas_arp()
    buscar_arp('192.168.1.3')
    buscar_arp('192.168.1.5')
