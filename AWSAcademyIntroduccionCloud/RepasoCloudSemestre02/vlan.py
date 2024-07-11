class VLANManager:
    def __init__(self):
        self.vlans = {}

    def crear_vlan(self, vlan_id, nombre):
        if vlan_id in self.vlans:
            print(f"Error: Ya existe una VLAN con el ID {vlan_id}.")
            return False
        self.vlans[vlan_id] = {'nombre': nombre, 'dispositivos': []}
        print(f"VLAN {vlan_id} - '{nombre}' creada exitosamente.")
        return True

    def asignar_dispositivo(self, vlan_id, dispositivo):
        if vlan_id not in self.vlans:
            print(f"Error: No se encontró la VLAN con ID {vlan_id}.")
            return False
        if dispositivo in self.vlans[vlan_id]['dispositivos']:
            print(f"Error: El dispositivo {dispositivo} ya está asignado a la VLAN {vlan_id}.")
            return False
        self.vlans[vlan_id]['dispositivos'].append(dispositivo)
        print(f"Dispositivo {dispositivo} asignado a VLAN {vlan_id} exitosamente.")
        return True

    def listar_vlans(self):
        if not self.vlans:
            print("No hay VLANs registradas.")
            return
        print("Lista de VLANs:")
        for vlan_id, info in self.vlans.items():
            print(f"  VLAN ID: {vlan_id}, Nombre: {info['nombre']}, Dispositivos: {info['dispositivos']}")
        print()

    def eliminar_vlan(self, vlan_id):
        if vlan_id not in self.vlans:
            print(f"Error: No se encontró la VLAN con ID {vlan_id}.")
            return False
        del self.vlans[vlan_id]
        print(f"VLAN {vlan_id} eliminada exitosamente.")
        return True

    def modificar_nombre_vlan(self, vlan_id, nuevo_nombre):
        if vlan_id not in self.vlans:
            print(f"Error: No se encontró la VLAN con ID {vlan_id}.")
            return False
        self.vlans[vlan_id]['nombre'] = nuevo_nombre
        print(f"Nombre de VLAN {vlan_id} modificado exitosamente a '{nuevo_nombre}'.")
        return True

    def buscar_vlan_por_dispositivo(self, dispositivo):
        for vlan_id, info in self.vlans.items():
            if dispositivo in info['dispositivos']:
                print(f"Dispositivo {dispositivo} está asignado a VLAN ID: {vlan_id}, Nombre: {info['nombre']}")
                return vlan_id, info['nombre']
        print(f"Dispositivo {dispositivo} no está asignado a ninguna VLAN.")
        return None

    def exportar_configuracion(self, archivo):
        with open(archivo, 'w') as f:
            for vlan_id, info in self.vlans.items():
                f.write(f"{vlan_id},{info['nombre']},{','.join(info['dispositivos'])}\n")
        print(f"Configuración de VLANs exportada a {archivo} exitosamente.")

    def importar_configuracion(self, archivo):
        try:
            with open(archivo, 'r') as f:
                for linea in f:
                    partes = linea.strip().split(',')
                    vlan_id = int(partes[0])
                    nombre = partes[1]
                    dispositivos = partes[2:]
                    self.vlans[vlan_id] = {'nombre': nombre, 'dispositivos': dispositivos}
            print(f"Configuración de VLANs importada desde {archivo} exitosamente.")
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {archivo}.")

# Ejemplo de uso
if __name__ == "__main__":
    manager = VLANManager()

    manager.crear_vlan(1, "Producción")
    manager.crear_vlan(2, "Desarrollo")

    manager.asignar_dispositivo(1, "00:1A:2B:3C:4D:5E")
    manager.asignar_dispositivo(2, "00:1A:2B:3C:4D:5F")

    manager.listar_vlans()

    manager.modificar_nombre_vlan(1, "Producción Actualizada")
    manager.listar_vlans()

    manager.buscar_vlan_por_dispositivo("00:1A:2B:3C:4D:5E")

    manager.exportar_configuracion("vlans_config.txt")

    manager.eliminar_vlan(2)
    manager.listar_vlans()

    manager.importar_configuracion("vlans_config.txt")
    manager.listar_vlans()
