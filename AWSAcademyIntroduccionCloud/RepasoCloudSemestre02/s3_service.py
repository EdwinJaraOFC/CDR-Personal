class S3Bucket:
    """
    Simula la creación y gestión de buckets y objetos.
    """
    def __init__(self):
        self.buckets = {}  # Diccionario para almacenar los buckets
        
    def create_bucket(self, name):
        """
        Crea un nuevo bucket vacío con el nombre especificado.
        """
        self.buckets[name] = {}
        print(f"Bucket '{name}' creado exitosamente.")

    def put_object(self, bucket, key, data):
        """
        Agrega un nuevo objeto al bucket especificado.
        """
        if bucket in self.buckets:
            self.buckets[bucket][key] = data
            print(f"Objeto '{key}' agregado al bucket '{bucket}'.")

    def get_object(self, bucket, key):
        """
        Obtiene el contenido de un objeto en un bucket específico.
        """
        if bucket in self.buckets:
            if key in self.buckets[bucket]:
                return self.buckets.get(bucket, {}).get(key, None)
            else:
                print(f"No se encontró el objeto '{key}' en el bucket '{bucket}'.")
        else:
            print(f"No se encontró el bucket '{bucket}'.")

    def list_objects(self, bucket):
        """
        Lista todos los objetos en un bucket específico.
        """
        if bucket in self.buckets:
            objects = list(self.buckets[bucket].keys())
            print(f"Contenido del bucket '{bucket}': {objects}")
            return objects
        else:
            print(f"No hay objetos en el bucket '{bucket}'.")

    def delete_object(self, bucket, key):
        """
        Elimina un objeto específico de un bucket.
        """
        if bucket in self.buckets:
            if key in self.buckets[bucket]:
                del self.buckets[bucket][key]
                print(f"Objeto '{key}' eliminado del bucket '{bucket}'.")
            else:
                print(f"No se pudo encontrar el objeto '{key}' en el bucket '{bucket}'.")
        else:
            print(f"No se encontró el bucket '{bucket}'.")

class S3BucketWithPermissions(S3Bucket):
    """
    Simula el manejo de permisos mediante un diccionario de permisos.
    """
    def __init__(self):
        super().__init__()
        self.permissions = {}
    
    def set_permission(self, bucket, key, permission):
        """
        Establece permisos para un objeto específico en un bucket.
        """
        if bucket not in self.permissions:
            self.permissions[bucket] = {}
        self.permissions[bucket][key] = permission
        print(f"Permiso '{permission}' establecido para el objeto '{key}' en el bucket '{bucket}'.")

    def check_permission(self, bucket, key, action):
        """
        Verifica si un objeto en un bucket tiene un permiso específico.
        """
        if bucket in self.permissions and key in self.permissions[bucket]:
            if self.permissions[bucket][key] == action:
                print(f"El objeto '{key}' en el bucket '{bucket}' tiene permiso '{action}'.")
                return True
        print(f"El objeto '{key}' en el bucket '{bucket}' no tiene permiso '{action}'.")
        return False

class S3BucketWithVersioning(S3Bucket):
    """
    Extiende la clase S3Bucket para añadir versionamiento de objetos.
    """
    def __init__(self):
        super().__init__()
        self.versions = {}
    
    def put_object(self, bucket, key, data):
        """
        Agrega un objeto al bucket con versionamiento.
        """
        if bucket not in self.versions:
            self.versions[bucket] = {}
        if key not in self.versions[bucket]:
            self.versions[bucket][key] = []
        self.versions[bucket][key].append(data)
        print(f"Objeto '{key}' agregado al bucket '{bucket}' con versionamiento.")

    def get_object(self, bucket, key, version=None):
        """
        Obtiene el contenido de un objeto en un bucket, opcionalmente de una versión específica.
        """
        if version is None:
            latest_version = self.versions.get(bucket, {}).get(key, [])[-1]
            print(f"Contenido del objeto '{key}' en el bucket '{bucket}':\n{latest_version}")
            return latest_version
        else:
            specific_version = self.versions.get(bucket, {}).get(key, [])[version]
            print(f"Contenido de la versión {version} del objeto '{key}' en el bucket '{bucket}':\n{specific_version}")
            return specific_version

class S3BucketWithReplication(S3Bucket):
    """
    Simula la replicación de objetos entre dos buckets.
    """
    def replicate(self, source_bucket, target_bucket):
        """
        Replica objetos desde un bucket de origen a un bucket de destino.
        """
        if source_bucket in self.buckets and target_bucket in self.buckets:
            self.buckets[target_bucket] = self.buckets[source_bucket].copy()
            print(f"Objetos replicados de '{source_bucket}' a '{target_bucket}'.")

from cryptography.fernet import Fernet
class S3BucketWithEncryption(S3Bucket):
    """
    Simula la encriptación de objetos antes de almacenarlos.
    """
    def __init__(self, key):
        super().__init__()
        self.cipher = Fernet(key)
    
    def put_object(self, bucket, key, data):
        """
        Encripta y agrega un objeto al bucket.
        """
        encrypted_data = self.cipher.encrypt(data.encode())
        super().put_object(bucket, key, encrypted_data)
    
    def get_object(self, bucket, key):
        """
        Desencripta y obtiene un objeto del bucket.
        """
        encrypted_data = super().get_object(bucket, key)
        return self.cipher.decrypt(encrypted_data).decode()


# Ejemplos de uso

# Ejemplo de uso de S3Bucket básico
s3 = S3Bucket()
s3.create_bucket('Archivos')
s3.put_object('Archivos', 'documento.txt', 'Contenido del documento de texto.')
s3.get_object('Archivos', 'documento.txt')
s3.list_objects('Archivos')
s3.delete_object('Archivos', 'documento.txt')
print("")

# Ejemplo de uso de S3BucketWithPermissions
s3p = S3BucketWithPermissions()
s3p.create_bucket('Documentos')
s3p.put_object('Documentos', 'informe.pdf', 'Contenido del informe en PDF.')
s3p.set_permission('Documentos', 'informe.pdf', 'read')
s3p.check_permission('Documentos', 'informe.pdf', 'read')
s3p.get_object('Documentos', 'informe.pdf')
s3p.list_objects('Documentos')
s3p.delete_object('Documentos', 'informe.pdf')
print("")

# Ejemplo de uso de S3BucketWithVersioning
s3v = S3BucketWithVersioning()
s3v.create_bucket('Fotos')
s3v.put_object('Fotos', 'vacaciones.jpg', 'Contenido de la foto de vacaciones.')
s3v.put_object('Fotos', 'vacaciones.jpg', 'Nueva versión de la foto de vacaciones.')
s3v.get_object('Fotos', 'vacaciones.jpg')
s3v.get_object('Fotos', 'vacaciones.jpg', 0)
print("")

# Ejemplo de uso de S3BucketWithReplication
s3r = S3BucketWithReplication()
s3r.create_bucket('Backup')
s3r.replicate('Fotos', 'Backup')
s3r.list_objects('Backup')
print("")

# Ejemplo de uso de S3BucketWithEncryption
key = Fernet.generate_key()
s3e = S3BucketWithEncryption(key)
s3e.create_bucket('Privado')
s3e.put_object('Privado', 'secreto.txt', 'Este es un secreto.')
s3e.get_object('Privado', 'secreto.txt')
