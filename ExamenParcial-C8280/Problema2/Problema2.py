class ARP:
    def __init__(self):
        self.tabla = {}
    def ingresar_ip(self, ip):
        print(f"Direccion IP {ip} creada exitosamente.")
        return True
    def ingresar_MAC(self, MAC):
        print(f"Direccion MAC {MAC} creada exitosamente.")
        return True
    def mostrar_ARP(self):
        if not self.tabla:
            print("No existe la tabla ARP actualmente.")
        
# Demostracion de la clase ARP
if __name__=="__main__":
    tabla = ARP()
    tabla.ingresar_ip("192.180.000.000")
    tabla.ingresar_MAC("00:1A:2B:3C:4D:5E")
    tabla.mostrar_ARP()
