import uuid

class SimuladorEBS:
    def __init__(self):
        self.volumes = {}
        self.snapshots = {}
        self.id_counter = 1  # Contador para IDs únicos

    def generate_unique_id(self):
        unique_id = str(uuid.uuid4())[:8]  # Genera un UUID único y toma los primeros 8 caracteres
        return unique_id

    def create_ebs_volume(self, size, availability_zone):
        volume_id = self.generate_unique_id()
        self.volumes[volume_id] = {
            'Size': size,
            'AvailabilityZone': availability_zone,
            'VolumeType': 'gp2'
        }
        print(f"Creado volumen EBS: {volume_id}")
        return volume_id

    def attach_ebs_volume(self, volume_id, instance_id, device):
        if volume_id in self.volumes:
            print(f"Adjuntado volumen {volume_id} a la instancia {instance_id} en dispositivo {device}")
            # Simulación de adjuntar volumen a instancia
        else:
            print(f"Volumen {volume_id} no encontrado")

    def create_snapshot(self, volume_id, description):
        if volume_id in self.volumes:
            snapshot_id = self.generate_unique_id()
            self.snapshots[snapshot_id] = {
                'SnapshotId': snapshot_id,
                'VolumeId': volume_id,
                'Description': description
            }
            print(f"Creada instantánea: {snapshot_id}")
            return snapshot_id
        else:
            print(f"Volumen {volume_id} no encontrado")

    def list_snapshots(self):
        for snapshot_id, snapshot_info in self.snapshots.items():
            print(f"ID: {snapshot_info['SnapshotId']}, Volume ID: {snapshot_info['VolumeId']}, Description: {snapshot_info['Description']}")

    def delete_ebs_volume(self, volume_id):
        if volume_id in self.volumes:
            del self.volumes[volume_id]
            # Eliminar instantáneas asociadas si es necesario
            print(f"Volumen EBS {volume_id} eliminado correctamente")
        else:
            print(f"Volumen EBS {volume_id} no encontrado")

    def delete_snapshot(self, snapshot_id):
        if snapshot_id in self.snapshots:
            del self.snapshots[snapshot_id]
            print(f"Instantánea {snapshot_id} eliminada correctamente")
        else:
            print(f"Instantánea {snapshot_id} no encontrada")

    def list_volumes(self):
        for volume_id, volume_info in self.volumes.items():
            print(f"ID: {volume_id}, Size: {volume_info['Size']} GiB, Availability Zone: {volume_info['AvailabilityZone']}")

    def describe_volume(self, volume_id):
        if volume_id in self.volumes:
            volume_info = self.volumes[volume_id]
            print(f"Volume ID: {volume_id}, Size: {volume_info['Size']} GiB, Availability Zone: {volume_info['AvailabilityZone']}")
        else:
            print(f"Volumen {volume_id} no encontrado")

    def describe_snapshot(self, snapshot_id):
        if snapshot_id in self.snapshots:
            snapshot_info = self.snapshots[snapshot_id]
            print(f"Snapshot ID: {snapshot_id}, Volume ID: {snapshot_info['VolumeId']}, Description: {snapshot_info['Description']}")
        else:
            print(f"Instantánea {snapshot_id} no encontrada")

    def modify_volume_size(self, volume_id, new_size):
        if volume_id in self.volumes:
            self.volumes[volume_id]['Size'] = new_size
            print(f"Tamaño del volumen {volume_id} actualizado a {new_size} GiB")
        else:
            print(f"Volumen {volume_id} no encontrado")

# Ejemplo de uso

simulador = SimuladorEBS() # Simulación de las operaciones
volume_id = simulador.create_ebs_volume(10, 'us-west-2a') # Crear un volumen EBS
simulador.attach_ebs_volume(volume_id, 'i-1234567890abcdef0', '/dev/sdf') # Adjuntar un volumen EBS a una instancia EC2 (simulación)
snapshot_id = simulador.create_snapshot(volume_id, 'Instantánea del volumen ' + volume_id) # Crear una instantánea del volumen EBS
simulador.list_snapshots() # Listar todas las instantáneas disponibles
simulador.delete_ebs_volume(volume_id) # Eliminar un volumen EBS
simulador.list_volumes() # Listar todos los volúmenes EBS

# Describir un volumen y una instantánea específica
simulador.describe_volume(volume_id)
simulador.describe_snapshot(snapshot_id)
