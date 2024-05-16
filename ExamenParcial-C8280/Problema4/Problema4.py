class VLANManager:
    def __init__(self):
        self.vlans = {}
    def crear_vlan(self,vlan_id,nombre):
        if vlan_id in self.vlans:
            print(f"Error: Ya existe una VLAN con el ID {vlan_id}.")
            return False
        self.vlans[vlan_id] = {'nombre': nombre, 'dispositivos': []}
        print(f"VLAN{vlan_id}-'{nombre}' creada exitosamente.")
        return True
    def asignar_dispositivo(self, vlan_id, dispositivo):
        if vlan_id not in self.vlans:
            print(f"Error: No se encontró la VLAN con ID {vlan_id}.")
            return False
        if dispositivo in self.vlans[vlan_id]['dispositivos']:
            print(f"Error: El dispositivo {dispositivo} ya está asignado a la VLAN {vlan_id}.")
            return False
        self.vlans[vlan_id]['dispositivos'].append(dispositivo)
        print(f"Dispositivo {dispositivo} asignado a la VLAN {vlan_id} exitosamente.")
        return True
    def listar_vlans(self):
        if not self.vlans:
            print("No hay VLANS registradas.")
            return
        for vlan_id, info in self.vlans.items():
            print(f"VLAN ID:{vlan_id}, Nombre: {info['nombre']}, Dispositivos: {info['dispositivos']}")
            return
    def eliminar_vlan(self, vlan_id):
        if vlan_id not in self.vlans:
            print(f"Error: No se encontró la VLAN con ID {vlan_id}.")
            return False
        
    # Crearé una función que permit modificar el nombre de una VLAN existente
    def modificar_nombre_vlan(self, vlan_id, nuevonombre): # Recibimos como parámetros el ID y el nombre a cambiar
        if vlan_id not in self.vlans: # Verificar si se encuentra o no la VLAN con el ID correspondiente
            print(f"Error: No se encontró la VLAN con ID {vlan_id}.")
            return False
        self.vlans[vlan_id]['nombre'] = nuevonombre # Se actualiza el nombre de la VLAN
        print(f"Nombre de VLAN{vlan_id} cambiado a {nuevonombre}.")
        return True

    # Crearé una función que permite buscar en que VLAN está asignado un dispositivo dado su direccion MAC
    def buscar_vlan(self, vlan_id, dispositivo):
        if vlan_id not in self.vlans: # Verificar si se encuentra o no la VLAN con el ID correspondiente
            print(f"Error: No se encontró la VLAN con ID {vlan_id}.")
            return False
        # Buscamos si la direccion MAC del dispositivo se encuentra en la ID solicitada
        if dispositivo in self.vlans[vlan_id]['dispositivos']:
            print(f"Error: El dispositivo {dispositivo} está asignado a la VLAN {vlan_id}.")
            return False
        elif dispositivo not in self.vlans[vlan_id]['dispositivos']:
            print(f"Error: El dispositivo {dispositivo} no está asignado a la VLAN {vlan_id}.")
            return False
# Demostración del uso de la clase VLANManager
if __name__=="__main__":
    manager = VLANManager()
    manager.crear_vlan(1, "Produccion")
    manager.crear_vlan(2, "Desarrollo")
    manager.asignar_dispositivo(1, "00:1A:2B:3C:4D:5E")
    manager.asignar_dispositivo(2, "00:1A:2B:3C:4D:5F")
    manager.listar_vlans()
    manager.modificar_nombre_vlan(1, "Produccion2")
    manager.eliminar_vlan(2)
    manager.listar_vlans()
    manager.buscar_vlan(1, "00:1A:2B:3C:4D:5E")
    manager.buscar_vlan(2, "00:1A:2B:3C:4D:5E")
